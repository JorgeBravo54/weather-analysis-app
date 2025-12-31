# Weather Analysis App 

A data analysis and visualization application built with **Python, SQLite, Pandas, Matplotlib, and Streamlit**.  
The app allows users to explore historical weather data from multiple cities and extract information through various plots.

---

## Features

- Average temperature analysis by city and year
- Temperature trends over time
- Weather type frequency analysis
- Min–max temperature variation by city
- Latitude vs temperature correlation
- SQLite database integration
- Streamlit interface with multi-page navigation

## How It Works

The application is built as a modular Streamlit web app with a centralized SQLite database.

### Application Flow

1. **Entry Point**
   - The app starts from `app.py`, which initializes the Streamlit interface and gives the user basic information about the page

2. **Navigation**
   - A menu-based navigation system allows users to switch between different functions.
   - Each page corresponds to a dedicated Python module inside the `pages` directory.

3. **Deployment**
   - The application is deployed on Streamlit Cloud and runs directly from the GitHub repository.
   - Dependencies are installed automatically using `requirements.txt`.

This ensures modularity, maintainability, and easy extensibility for additional analyses.
