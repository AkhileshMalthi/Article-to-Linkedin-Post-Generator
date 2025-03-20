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
1. Clone this repository
2. Install dependencies: `poetry install`
3. Set up your GroqAPI key in `.env` file
4. Run the application: `poetry run streamlit run app.py`

## Usage
1. Select a topic of interest
2. Browse trending articles
3. Click on an article to view details
4. Generate a LinkedIn post from the selected article
5. Customize your post as needed
6. Copy the post to your clipboard and share on LinkedIn
