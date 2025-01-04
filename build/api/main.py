from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
import json
import os
from dotenv import load_dotenv
from openai import OpenAI
import requests
from bs4 import BeautifulSoup

load_dotenv()

app = FastAPI()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def scrape_website():
    try:
        url = "https://cv.ricco.ai"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        # Extract text content while preserving some structure
        content = ' '.join([p.get_text(strip=True) for p in soup.find_all(['p', 'h1', 'h2', 'h3', 'li', 'div'])])
        print("Successfully scraped website content")
        return content
    except Exception as e:
        print(f"Error scraping website: {e}")
        return ""

# Initialize website content
website_content = scrape_website()

# Add a test route
@app.get("/")
async def root():
    return {"message": "Server is running"}

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: str):
    await websocket.accept()
    
    system_prompt = f"""[RICCO_YEUNG_CV_PAGE_ASSISTANT_ONLY]
    You are Ricco Yeung's CV assistant. Here is his CV content:
    {website_content}
    
    CRITICAL RULES:
    1. You are ONLY allowed to discuss Ricco's CV, background, and experience
    2. If anyone asks about ricco.AI business services, say "For business inquiries, please visit ricco.AI"
    3. Your responses must be based on the CV content above
    4. Keep responses short and complete
    5. Be specific about companies and dates from Ricco's career history

    FORBIDDEN:
    - Never give business advice
    - Never suggest consultations or meetings
    - Never discuss anything not related to Ricco Yeung or the companies he worked for or projects he worked on"""

    conversation_history = [
        {"role": "system", "content": system_prompt}
    ]
    
    try:
        while True:
            message = await websocket.receive_text()
            await websocket.send_text("typing")
            
            response = client.chat.completions.create(
                model="gpt-4-turbo-preview",
                messages=conversation_history + [
                    {"role": "user", "content": message},
                    {
                        "role": "system",
                        "content": "Format your response as a complete message that fits within 75 tokens. If you need more space, end with a natural stopping point and ask if they want more details."
                    }
                ],
                functions=[{
                    "name": "send_chat_response",
                    "description": "Send a complete chat response",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "response": {
                                "type": "string",
                                "description": "The complete response that must fit within space and not cut off mid-sentence"
                            }
                        },
                        "required": ["response"]
                    }
                }],
                function_call={"name": "send_chat_response"},
                max_tokens=75,
                temperature=0.7
            )
            
            # Extract the response from the function call
            function_response = response.choices[0].message.function_call.arguments
            ai_response = json.loads(function_response)["response"]
            
            conversation_history.append({"role": "user", "content": message})
            conversation_history.append({"role": "assistant", "content": ai_response})
            
            await websocket.send_text(ai_response)
            
    except Exception as e:
        print(f"Error: {e}")
        await websocket.close()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 