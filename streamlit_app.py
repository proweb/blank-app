import streamlit as st
import urllib3
from urllib3.exceptions import HTTPError
from bs4 import BeautifulSoup

# Disable SSL warnings (not recommended for production)
urllib3.disable_warnings()

@st.cache_data
def fetch_url_content(url):
    """Fetch content from a given URL"""
    http = urllib3.PoolManager()
    try:
        response = http.request('GET', url)
        if response.status == 200:
            return response.data.decode('utf-8')
        else:
            return f"Error: Received status code {response.status}"
    except HTTPError as e:
        return f"HTTP Error: {str(e)}"
    except Exception as e:
        return f"Error: {str(e)}"
    
def extract_assets(html_content):
    """Extract CSS and JS links from HTML content"""
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Extract CSS links
    css_links = [link['href'] for link in soup.find_all('link', rel='stylesheet') if link.get('href')]
    
    # Extract JS links
    js_links = [script['src'] for script in soup.find_all('script') if script.get('src')]
    
    return css_links, js_links

# App title
st.title("URL Content Fetcher")

# Create form
with st.form("url_form"):
    url = st.text_input("Enter URL:",value=None, placeholder="https://example.com", type="default")
    submit_button = st.form_submit_button("Fetch Content")

# When form is submitted
if submit_button and url:
    st.write("Fetching content from:", url)
    
    with st.spinner("Loading..."):
        content = fetch_url_content(url)

    css_links, js_links = extract_assets(content)
    
    # Display CSS links
    with st.expander(f"CSS Files ({len(css_links)})"):
            if css_links:
                for css in css_links:
                    st.code(css, language='text')
            else:
                st.info("No CSS links found")
        
        # Display JS links
    with st.expander(f"JavaScript Files ({len(js_links)})"):
            if js_links:
                for js in js_links:
                    st.code(js, language='text')
            else:
                st.info("No JavaScript links found")
    
    
    with st.expander("Source code"):
        st.caption(":blue[HTML code]")
        st.code(content, language='html', line_numbers=True)
  
elif submit_button and not url:
    st.warning("Please enter a URL!")