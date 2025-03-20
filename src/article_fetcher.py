import os
from datetime import datetime, timedelta
from newsapi import NewsApiClient

def fetch_articles_by_topic(topic, count=10):
    """
    Fetch trending articles based on the selected topic
    
    Args:
        topic (str): The topic to search for
        count (int): The number of articles to return
        
    Returns:
        list: A list of article dictionaries
    """
    try:
        # Initialize News API client
        news_api_key = os.getenv("NEWS_API_KEY")
        if not news_api_key:
            raise ValueError("NEWS_API_KEY environment variable is not set")
            
        newsapi = NewsApiClient(api_key=news_api_key)
        
        # Calculate date range (last 7 days)
        end_date = datetime.now()
        start_date = end_date - timedelta(days=7)
        
        # Format dates for the API
        from_date = start_date.strftime('%Y-%m-%d')
        to_date = end_date.strftime('%Y-%m-%d')
        
        # Fetch articles
        response = newsapi.get_everything(
            q=topic,
            language='en',
            sort_by='popularity',
            from_param=from_date,
            to=to_date,
            page_size=count
        )
        
        return response['articles']
        
    except Exception as e:
        # For demo purposes, return mock data if API call fails
        print(f"Error fetching articles: {e}")
        return [
            {
                'source': {'name': 'Example Source'},
                'author': 'Author Name',
                'title': f'Example Article about {topic} #{i}',
                'description': f'This is a sample description for an article about {topic}.',
                'url': 'https://example.com',
                'urlToImage': None,
                'publishedAt': datetime.now().isoformat(),
                'content': f'Sample content about {topic}.'
            }
            for i in range(1, count + 1)
        ]
