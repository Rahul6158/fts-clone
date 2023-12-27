import streamlit as st
import page1
import page2
import page3
import datetime
import pandas as pd
from itertools import cycle

# Read the CSV file containing the quotes and authors
quotes_df = pd.read_csv('AnimeQuotes.csv')  # Replace 'AnimeQuotes.csv' with your file path

# Colors to rotate for quotes and authors
quote_colors = cycle(["red", "blue", "green", "purple","orange","White","brown","black"])  # Add more colors as needed
author_colors = cycle(["blue", "green", "purple", "red"])  # Corresponding colors for authors

# Function to get the quote and author based on the current hour
def get_hourly_quote():
    current_hour = datetime.datetime.now().hour
    quote_index = current_hour % len(quotes_df)
    hourly_quote = quotes_df.iloc[quote_index]
    return hourly_quote['Quote'], hourly_quote['Character']  # Assuming 'Quote' and 'Character' are column names

# Function to display the hourly quote and author with rotating colors
def display_quote():
    st.sidebar.title("Daily Quote:")
    quote, author = get_hourly_quote()
    
    # Get next color in rotation for the quote and author
    quote_color = next(quote_colors)
    author_color = next(author_colors)
    
    quote_html = f'<p style="color:{quote_color}; font-family: Lucida Console, Monaco, monospace; font-size: 20px;"><strong>{quote}</strong></p>'
    author_html = f'<p style="color:{author_color}; font-family: Lucida Console, Monaco, monospace; font-size: 16px;"><em>- {author}</em></p>'
    full_html = quote_html + author_html
    
    st.sidebar.markdown(full_html, unsafe_allow_html=True)  # Display the combined quote and author in the sidebar

def custom_sidebar():
    st.sidebar.title("Features")
    st.sidebar.header("Available Options")  # Add a sidebar title
    # Create radio button group
    page_choice = st.sidebar.radio("", ["Document and Pdf Translation", "Text Translation", "Text Summarization"])

    names = ["Sai Annapurna", "Kalyan Ram Chegondi", "Vinay Bhaskar Bonam", "Karthik Vasa", "Tusha Rahul Bellamkonda", "Pindi Sushmitha Devi"]
    st.sidebar.title("Developed By :")
    for name in names:
        st.sidebar.write(name)
    st.sidebar.title("Under The Guidance of :")
    st.sidebar.write("Dr. Bomma Ramakrishna")
    
    # Display the hourly quote and author
    display_quote()
    
    return page_choice

# Initialize session state to store the last updated hour
if 'last_updated_hour' not in st.session_state:
    st.session_state.last_updated_hour = -1

# Use the custom sidebar method
page_choice = custom_sidebar()

# Check if an hour has passed to update the quote
current_hour = datetime.datetime.now().hour
if current_hour != st.session_state.last_updated_hour:
    st.session_state.last_updated_hour = current_hour
    st.experimental_rerun()  # Rerun the app to update the displayed quote

# Depending on the selected choice, call the respective main function
if page_choice == "Document and Pdf Translation":
    page1.main()  # Call the main function for Page 1
elif page_choice == "Text Translation":
    page2.main()
elif page_choice == "Text Summarization":
    page3.main()  # Call the main function for Page 3
