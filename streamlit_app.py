import streamlit as st
import urllib3
from urllib3.exceptions import HTTPError

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

    with st.expander("Source code"):
        st.caption(":blue[HTML code]")
        st.code(content, language='html', line_numbers=True)
    # Тут будут список CSS
    with st.expander("CSS Links"):
        st.write(''' **Тут ссылки на CSS из документа**''')
    with st.expander("JS Links"):
        st.write(''' **Тут ссылки на JS из документа**''')
    
    
    
  
    
    
elif submit_button and not url:
    st.warning("Please enter a URL!")