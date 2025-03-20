class UserConfig:
    """
    Class to store user configuration preferences for LinkedIn posts
    """
    def __init__(self, post_style="", sample_posts=""):
        """
        Initialize user configuration
        
        Args:
            post_style (str): User's preferred post style
            sample_posts (str): Sample LinkedIn posts for few-shot learning
        """
        self.post_style = post_style
        self.sample_posts = sample_posts
