"""
LinkedIn Post Generation Prompt Templates

This module contains the prompt templates used for generating LinkedIn posts
from articles using AI language models.
"""

# System prompt template for the AI assistant
SYSTEM_TEMPLATE = """
You are a professional LinkedIn post generator. 
Your task is to create engaging LinkedIn posts based on articles.
The post should be informative, engaging, and match the user's style preferences.
"""

# User prompt template with placeholders for article content and user preferences
USER_TEMPLATE = """
Generate a LinkedIn post based on this article:

Title: {title}
Source: {source}
Description: {description}

User Style Preferences:
{style_preferences}

{few_shot_examples}

Create an engaging LinkedIn post that summarizes key insights from the article,
adds thoughtful commentary, and encourages engagement. Include relevant hashtags.
"""

def get_few_shot_examples(user_config):
    """
    Generate few-shot examples string based on user configuration
    
    Args:
        user_config: UserConfig object containing sample posts
        
    Returns:
        str: Formatted few-shot examples or empty string
    """
    if user_config.sample_posts:
        return "Here are sample posts from the user for reference:\n\n" + user_config.sample_posts
    return ""