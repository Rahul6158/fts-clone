import streamlit as st
import page1
import page2
import page3
import datetime
import pandas as pd
import time

# Read the CSV file containing the quotes and authors
quotes_df = pd.read_csv('AnimeQuotes.csv')  # Replace 'AnimeQuotes.csv' with your file path

# Function to get the quote and author based on the current time
def get_quote():
    current_time = datetime.datetime.now().strftime('%H:%M')
    quote_index = hash(current_time) % len(quotes_df)
    hourly_quote = quotes_df.iloc[quote_index]
    return hourly_quote['Quote'], hourly_quote['Character']  # Assuming 'Quote' and 'Character' are column names

# Function to display the quote and author
def display_quote():
    quote, author = get_quote()
    
    quote_html = f'<h3 style="color:black; font-family: Lucida Console, Monaco, monospace;">Timepass Quotes:</h3>'
    quote_html += f'<p style="font-family: Lucida Console, Monaco, monospace; font-size: 20px;"><strong>{quote}</strong></p>'
    author_html = f'<p style="font-family: Lucida Console, Monaco, monospace; font-size: 16px;"><em>- {author}</em></p>'
    
    full_html = quote_html + author_html
    st.sidebar.markdown(full_html, unsafe_allow_html=True)  # Display the combined quote and author in the sidebar

def custom_sidebar():
    st.sidebar.title("Features")
    st.sidebar.header("Available Options")  # Add a sidebar title
    # Create radio button group
    page_choice = st.sidebar.radio("", ["Document and Pdf Translation", "Text Translation", "Text Summarization"])

    return page_choice

# Use the custom sidebar method
page_choice = custom_sidebar()

# Display the logo at the top of the main page
st.image('logo.png', width=700)  # Replace 'logo.png' with your logo file and adjust the width as needed

# Loop to update the quote every minute
while True:
    display_quote()
    time.sleep(60)  # Update the quote every minute

# Depending on the selected choice, call the respective main function
if page_choice == "Document and Pdf Translation":
    page1.main()  # Call the main function for Page 1
elif page_choice == "Text Translation":
    page2.main()
elif page_choice == "Text Summarization":
    page3.main()  # Call the main function for Page 3
