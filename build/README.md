# Ricco's Portfolio Website

A modern, interactive portfolio website built with Astro, React, and FastAPI, featuring an AI-powered chatbot and dynamic content management.

## 🚀 Features

- **Modern UI/UX**: Built with Astro and React for optimal performance and user experience
- **AI Chatbot**: Interactive AI assistant powered by OpenAI
- **Dynamic Content**: Content management through Sanity.io
- **Real-time Communication**: WebSocket support for live interactions
- **Responsive Design**: Mobile-friendly interface with smooth animations
- **SEO Optimized**: Built with search engine optimization in mind

## 🛠️ Tech Stack

### Frontend
- [Astro](https://astro.build/) - Modern static site builder
- [React](https://reactjs.org/) - UI library
- [AOS](https://michalsnik.github.io/aos/) - Animate On Scroll library
- [Hero Icons](https://heroicons.com/) - Beautiful hand-crafted SVG icons

### Backend
- [FastAPI](https://fastapi.tiangolo.com/) - Modern Python web framework
- [WebSockets](https://websockets.readthedocs.io/) - Real-time communication
- [OpenAI](https://openai.com/) - AI/ML capabilities
- [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/) - Web scraping capabilities

### Content Management
- [Sanity.io](https://www.sanity.io/) - Headless CMS

## 📦 Installation

1. Clone the repository:
```bash
git clone https://github.com/riccoai/cvricco.git
cd cvricco
```

2. Install frontend dependencies:
```bash
npm install
```

3. Install Python dependencies:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

4. Set up environment variables:
Create a `.env` file in the root directory with the following variables:
```env
OPENAI_API_KEY=your_openai_api_key
SANITY_PROJECT_ID=your_sanity_project_id
SANITY_DATASET=your_sanity_dataset
SANITY_API_VERSION=your_sanity_api_version
SANITY_TOKEN=your_sanity_token
```

## 🚀 Development

1. Start the frontend development server:
```bash
npm run dev
```

2. Start the backend server:
```bash
uvicorn api.main:app --reload
```

The frontend will be available at `http://localhost:4321` and the backend at `http://localhost:8000`.

## 🏗️ Building for Production

1. Build the frontend:
```bash
npm run build
```

2. The production-ready files will be in the `dist` directory.

## 📝 Project Structure

```
├── api/              # Backend FastAPI application
├── public/           # Static assets
├── src/             # Frontend source code
│   ├── components/  # React components
│   ├── layouts/     # Page layouts
│   └── pages/       # Astro pages
├── schemas/         # Sanity.io schemas
└── dist/            # Production build output
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👥 Contact

For any questions or suggestions, please open an issue in the GitHub repository.

```sh
npm create astro@latest -- --template basics
```

[![Open in StackBlitz](https://developer.stackblitz.com/img/open_in_stackblitz.svg)](https://stackblitz.com/github/withastro/astro/tree/latest/examples/basics)
[![Open with CodeSandbox](https://assets.codesandbox.io/github/button-edit-lime.svg)](https://codesandbox.io/p/sandbox/github/withastro/astro/tree/latest/examples/basics)
[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/withastro/astro?devcontainer_path=.devcontainer/basics/devcontainer.json)

> 🧑‍🚀 **Seasoned astronaut?** Delete this file. Have fun!

![just-the-basics](https://github.com/withastro/astro/assets/2244813/a0a5533c-a856-4198-8470-2d67b1d7c554)

## 🚀 Project Structure

Inside of your Astro project, you'll see the following folders and files:

```text
/
├── public/
│   └── favicon.svg
├── src/
│   ├── components/
│   │   └── Card.astro
│   ├── layouts/
│   │   └── Layout.astro
│   └── pages/
│       └── index.astro
└── package.json
```

Astro looks for `.astro` or `.md` files in the `src/pages/` directory. Each page is exposed as a route based on its file name.

There's nothing special about `src/components/`, but that's where we like to put any Astro/React/Vue/Svelte/Preact components.

Any static assets, like images, can be placed in the `public/` directory.

## 🧞 Commands

All commands are run from the root of the project, from a terminal:

| Command                   | Action                                           |
| :------------------------ | :----------------------------------------------- |
| `npm install`             | Installs dependencies                            |
| `npm run dev`             | Starts local dev server at `localhost:4321`      |
| `npm run build`           | Build your production site to `./dist/`          |
| `npm run preview`         | Preview your build locally, before deploying     |
| `npm run astro ...`       | Run CLI commands like `astro add`, `astro check` |
| `npm run astro -- --help` | Get help using the Astro CLI                     |

## 👀 Want to learn more?

Feel free to check [our documentation](https://docs.astro.build) or jump into our [Discord server](https://astro.build/chat).
