import os
import streamlit as st
from dotenv import load_dotenv
from src.article_fetcher import fetch_articles_by_topic
from src.post_generator import generate_linkedin_post
from src.user_config import UserConfig

# Load environment variables
load_dotenv()

st.set_page_config(
    page_title="Article to LinkedIn Post Generator",
    page_icon="📝",
    layout="wide"
)

# Initialize session state
if 'user_config' not in st.session_state:
    st.session_state.user_config = UserConfig()
if 'articles' not in st.session_state:
    st.session_state.articles = []
if 'selected_article' not in st.session_state:
    st.session_state.selected_article = None
if 'generated_post' not in st.session_state:
    st.session_state.generated_post = ""

# App title
st.title("Article to LinkedIn Post Generator")
st.markdown("Transform trending articles into personalized LinkedIn posts")

# Sidebar for user configuration
with st.sidebar:
    st.header("User Preferences")
    
    # Global post style preferences
    st.subheader("Post Style")
    post_style = st.text_area(
        "Describe your preferred LinkedIn post style:",
        value=st.session_state.user_config.post_style,
        help="Example: 'Professional tone with emojis, 3-4 paragraphs with bullet points'"
    )
    
    # Sample posts for few-shot learning
    st.subheader("Sample Posts (Optional)")
    sample_posts = st.text_area(
        "Add sample LinkedIn posts for reference:",
        value=st.session_state.user_config.sample_posts,
        help="Paste 1-3 of your previous LinkedIn posts to guide the AI"
    )
    
    # Save config button
    if st.button("Save Preferences"):
        st.session_state.user_config.post_style = post_style
        st.session_state.user_config.sample_posts = sample_posts
        st.success("Preferences saved!")

# Main content area - two columns
col1, col2 = st.columns([1, 1])

# Column 1: Topic selection and article browsing
with col1:
    st.header("Find Trending Articles")
    
    # Topic selection
    topics = ["Technology", "Business", "Science", "Health", "Finance", "Marketing", "AI", "Career Development"]
    selected_topic = st.selectbox("Select a topic:", topics)
    
    if st.button("Find Articles"):
        with st.spinner("Fetching trending articles..."):
            st.session_state.articles = fetch_articles_by_topic(selected_topic)
            st.success(f"Found {len(st.session_state.articles)} articles on {selected_topic}")
    
    # Display articles
    if st.session_state.articles:
        st.subheader("Trending Articles")
        for i, article in enumerate(st.session_state.articles):
            with st.container():
                col_img, col_text = st.columns([1, 3])
                with col_img:
                    if article['urlToImage']:
                        st.image(article['urlToImage'], width=100)
                    else:
                        st.markdown("📄")
                with col_text:
                    st.markdown(f"**{article['title']}**")
                    st.markdown(f"*{article['source']['name']} · {article['publishedAt'][:10]}*")
                    if st.button("Select Article", key=f"select_{i}"):
                        st.session_state.selected_article = article
                st.markdown("---")

# Column 2: Article view and post generation
with col2:
    if st.session_state.selected_article:
        st.header("Selected Article")
        selected = st.session_state.selected_article
        
        # Display article details
        st.subheader(selected['title'])
        st.markdown(f"*Source: {selected['source']['name']} · {selected['publishedAt'][:10]}*")
        
        if selected['urlToImage']:
            st.image(selected['urlToImage'])
            
        st.markdown(selected['description'] if selected['description'] else "")
        st.markdown(f"[Read the full article]({selected['url']})")
        
        # Generate LinkedIn post
        if st.button("Generate LinkedIn Post"):
            with st.spinner("Generating your LinkedIn post..."):
                generated_post = generate_linkedin_post(
                    article=selected,
                    user_config=st.session_state.user_config
                )
                st.session_state.generated_post = generated_post
                
        # Display generated post
        if st.session_state.generated_post:
            st.header("Your LinkedIn Post")
            post_container = st.container(border=True)
            with post_container:
                st.markdown(st.session_state.generated_post)
            
            # Regenerate and copy buttons
            col_regen, col_copy = st.columns(2)
            with col_regen:
                if st.button("Regenerate Post"):
                    with st.spinner("Regenerating post..."):
                        st.session_state.generated_post = generate_linkedin_post(
                            article=selected,
                            user_config=st.session_state.user_config
                        )
            with col_copy:
                if st.button("Copy to Clipboard"):
                    st.code(st.session_state.generated_post)
                    st.success("Post copied to clipboard! Ready to paste on LinkedIn.")
    else:
        st.info("Select an article from the left panel to generate a LinkedIn post.")
