# Streamlit URL Content Fetcher

## Overview
A simple web application built with Streamlit that fetches content from any URL and extracts CSS and JavaScript asset links from the HTML.

## Features
- Fetch content from any URL using urllib3
- Extract and display CSS stylesheet links
- Extract and display JavaScript file links
- View full HTML source code with syntax highlighting
- Clean, expandable interface for viewing results

## Project Structure
```
.
├── streamlit_app.py          # Main application file
├── requirements.txt          # Python dependencies
├── .streamlit/
│   └── config.toml          # Streamlit configuration for Replit
└── replit.md                # This documentation file
```

## Dependencies
- **streamlit**: Web application framework
- **beautifulsoup4**: HTML parsing and asset extraction
- **urllib3**: HTTP client for fetching URL content

## Configuration
The application is configured to run on Replit with:
- Port: 5000
- Host: 0.0.0.0
- CORS disabled for iframe compatibility
- XSRF protection disabled for Replit environment

## Usage
1. Enter a URL in the text input field
2. Click "Fetch Content" to retrieve the page
3. View extracted CSS files, JavaScript files, and full HTML source in expandable sections

## Deployment
This application is configured for autoscale deployment on Replit, which is ideal for stateless web applications that don't need to maintain server state.

## Recent Changes
- **December 7, 2025**: Initial project import and Replit environment setup
  - Configured Streamlit for Replit (port 5000, host 0.0.0.0)
  - Set up workflow for development server
  - Configured autoscale deployment settings

## Notes
- SSL warnings are disabled for development purposes
- The application uses caching to improve performance for repeated URL fetches
