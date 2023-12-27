import streamlit as st
import page1
import page2
import page3
import datetime
import pandas as pd

# Read the CSV file containing the quotes
quotes_df = pd.read_csv('AnimeQuotes.csv')  # Replace 'path_to_your_csv_file.csv' with your file path

# Function to get the quote for the day based on the date
def get_daily_quote():
    today = datetime.datetime.now()
    quote_index = today.day % len(quotes_df)
    return quotes_df.iloc[quote_index]['Quote']  # Assuming 'Quote' is the column containing the quotes

# Function to display the quote at the top of the page
def display_quote():
    st.title("Daily Quote:")
    quote = get_daily_quote()
    st.write(quote)

def custom_sidebar():
    st.sidebar.title("Features")
    # ... (your existing sidebar code)

# Use the custom sidebar method
page_choice = custom_sidebar()

# Display the daily quote
display_quote()

if page_choice == "Document and Pdf Translation":
    page1.main()  # Call the main function for Page 1
elif page_choice == "Text Translation":
    page2.main()
elif page_choice == "Text Summarization":
    page3.main()  # Call the main function for Page 3
