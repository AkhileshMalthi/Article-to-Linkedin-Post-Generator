# Article-to-Linkedin-Post-Generator
A Personalized AI content writer for LinkedIn posts

## Overview
This application helps users create engaging LinkedIn posts based on trending articles. Select a topic of interest, browse trending articles, and generate personalized LinkedIn posts with just a few clicks.

## Features
- Browse trending articles by topic
- View article details and visit original sources
- Generate personalized LinkedIn posts from selected articles
- Customize post generation style with personal preferences
- Support for few-shot learning with sample posts

## Tech Stack
- LLM: GroqAPI for AI-powered content generation
- Frameworks: Streamlit for UI, LangChain for LLM orchestration
- Dependency Management: Poetry

## Setup Instructions

### Local Development
1. Clone this repository
2. Install dependencies: `poetry install` or `pip install -r requirements.txt`
3. Copy `.env.example` to `.env` and add your API keys:
   ```bash
   GROQ_API_KEY=your_groq_api_key_here
   NEWS_API_KEY=your_news_api_key_here
   ```
4. Run the application: `poetry run streamlit run app.py` or `streamlit run app.py`

### � Railway Deployment
This application is optimized for deployment on Railway. See [DEPLOYMENT.md](DEPLOYMENT.md) for detailed instructions.

#### Quick Deploy to Railway
[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/new/template)

**Required Environment Variables:**
- `GROQ_API_KEY` - Your Groq API key
- `NEWS_API_KEY` - Your News API key

## Usage
1. Select a topic of interest from the dropdown
2. Browse trending articles in the selected category
3. Click on an article to view details and summary
4. Generate a personalized LinkedIn post from the selected article
5. Customize your post style and preferences in the sidebar
6. Copy the generated post to your clipboard and share on LinkedIn
