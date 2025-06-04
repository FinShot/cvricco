from fastapi import FastAPI, WebSocket, WebSocketDisconnect
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
    
    try:
        while True:
            message = await websocket.receive_text()
            await websocket.send_text("typing")
            
            try:
                response = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "You are Ricco Yeung's CV assistant. Answer questions about his background and experience professionally."},
                        {"role": "user", "content": message}
                    ],
                    max_tokens=100
                )
                
                ai_response = response.choices[0].message.content
                await websocket.send_text(ai_response)
                
            except Exception as e:
                await websocket.send_text("Sorry, I'm having trouble right now. Please try again.")
            
    except WebSocketDisconnect:
        pass
    except Exception:
        pass

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 