import os
from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate
from src.prompts import SYSTEM_TEMPLATE, USER_TEMPLATE, get_few_shot_examples

def generate_linkedin_post(article, user_config):
    """
    Generate a LinkedIn post based on article content and user preferences
    
    Args:
        article (dict): Article data dictionary
        user_config (UserConfig): User configuration object
        
    Returns:
        str: Generated LinkedIn post content
    """
    try:
        # Initialize Groq LLM
        llm = ChatGroq(
            api_key=os.getenv("GROQ_API_KEY", "GROQ_API_KEY is missing in the environment variables"), # type: ignore
            model=os.getenv("GROQ_MODEL", "GROQ_MODEL is missing in the environment variables")
        )
        
        # Create prompt template using imported templates
        # Add few-shot examples if available
        few_shot = get_few_shot_examples(user_config)
        
        # Create the prompt
        prompt = ChatPromptTemplate.from_messages([
            ("system", SYSTEM_TEMPLATE),
            ("user", USER_TEMPLATE)
        ])
        
        # Create the chain using the modern approach
        chain = prompt | llm
        
        # Generate the post
        response = chain.invoke({
            "title": article['title'],
            "source": article['source']['name'],
            "description": article['description'] or "No description available",
            "style_preferences": user_config.post_style or "Professional, engaging LinkedIn style",
            "few_shot_examples": few_shot
        })

        # Extract content from LangChain response object
        if hasattr(response, 'content') and isinstance(response.content, str):
            return response.content.strip()
        elif isinstance(response, str):
            return response.strip()
        elif isinstance(response, dict) and 'content' in response:
            return response['content'].strip()
        else:
            return str(response).strip()
        
    except Exception as e:
        print(f"Error generating post: {e}")
        return f"""
        📰 I just read this interesting article: "{article['title']}"

        The key insights from this piece really got me thinking about the implications for our industry.

        What are your thoughts on this topic? I'd love to hear different perspectives!

        #ProfessionalDevelopment #{article['source']['name'].replace(' ', '')}
        """
