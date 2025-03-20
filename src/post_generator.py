import os
from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate
from langchain.chains import LLMChain

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
        groq_api_key = os.getenv("GROQ_API_KEY")
        if not groq_api_key:
            raise ValueError("GROQ_API_KEY environment variable is not set")
        
        llm = ChatGroq(
            api_key=groq_api_key, 
            model="llama3-70b-8192"
        )
        
        # Create prompt template
        system_template = """
        You are a professional LinkedIn post generator. 
        Your task is to create engaging LinkedIn posts based on articles.
        The post should be informative, engaging, and match the user's style preferences.
        """
        
        user_template = """
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
        
        # Add few-shot examples if available
        few_shot = ""
        if user_config.sample_posts:
            few_shot = "Here are sample posts from the user for reference:\n\n" + user_config.sample_posts
        
        # Create the prompt
        prompt = ChatPromptTemplate.from_messages([
            ("system", system_template),
            ("user", user_template)
        ])
        
        # Create LLM chain
        chain = LLMChain(llm=llm, prompt=prompt)
        
        # Generate the post
        response = chain.run(
            title=article['title'],
            source=article['source']['name'],
            description=article['description'] or "No description available",
            style_preferences=user_config.post_style or "Professional, engaging LinkedIn style",
            few_shot_examples=few_shot
        )
        
        return response.strip()
        
    except Exception as e:
        print(f"Error generating post: {e}")
        return f"""
        📰 I just read this interesting article: "{article['title']}"

        The key insights from this piece really got me thinking about the implications for our industry.

        What are your thoughts on this topic? I'd love to hear different perspectives!

        #ProfessionalDevelopment #{article['source']['name'].replace(' ', '')}
        """
