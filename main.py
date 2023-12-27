import streamlit as st
import page1
import page2
import page3
import datetime
import pandas as pd

# Read the CSV file containing the quotes and authors
quotes_df = pd.read_csv('AnimeQuotes.csv')  # Replace 'path_to_your_csv_file.csv' with your file path

# Function to get the quote and author for the day based on the date
def get_daily_quote():
    today = datetime.datetime.now()
    quote_index = today.day % len(quotes_df)
    daily_quote = quotes_df.iloc[quote_index]
    return daily_quote['Quote'], daily_quote['Character']  # Assuming 'Quote' and 'Author' are column names

# Function to display the daily quote and author
def display_quote():
    st.header("Daily Quote:")
    quote, author = get_daily_quote()
    quote_html = f'<p style="color:red"><strong>{quote}</strong></p>'
    author_html = f'<p style="color:blue"><em>- {author}</em></p>'

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
    return page_choice
# Use the custom sidebar method
page_choice = custom_sidebar()

# Display the daily quote and author
display_quote()

if page_choice == "Document and Pdf Translation":
    page1.main()  # Call the main function for Page 1
elif page_choice == "Text Translation":
    page2.main()
elif page_choice == "Text Summarization":
    page3.main()  # Call the main function for Page 3
