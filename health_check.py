# Deployment Health Check Endpoint
import os
import sys

def health_check():
    """Simple health check for deployment platforms"""
    try:
        # Check if required environment variables are set
        required_env_vars = ['GROQ_API_KEY', 'NEWS_API_KEY']
        missing_vars = [var for var in required_env_vars if not os.getenv(var)]
        
        if missing_vars:
            print(f"Missing environment variables: {', '.join(missing_vars)}")
            return False
            
        # Try importing main modules
        from src.article_fetcher import fetch_articles_by_topic
        from src.post_generator import generate_linkedin_post
        from src.user_config import UserConfig
        
        print("Health check passed - all systems operational")
        return True
        
    except Exception as e:
        print(f"Health check failed: {str(e)}")
        return False

if __name__ == "__main__":
    if health_check():
        sys.exit(0)
    else:
        sys.exit(1)