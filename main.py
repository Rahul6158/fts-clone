import streamlit as st
import page1
import page2
import page3
import datetime
import pandas as pd
from PIL import Image
from itertools import cycle

logo = Image.open('logo.png')
# Read the CSV file containing the quotes and authors
quotes_df = pd.read_csv('AnimeQuotes.csv')  # Replace 'AnimeQuotes.csv' with your file path

# Colors to rotate for quotes and authors
quote_colors = cycle(["red", "blue", "green", "purple", "orange", "white", "brown", "black"])  # Add more colors as needed
author_colors = cycle(["blue", "green", "purple", "red"])  # Corresponding colors for authors

# Function to get the quote and author based on the current hour
def get_hourly_quote():
    current_hour = datetime.datetime.now().hour
    quote_index = current_hour % len(quotes_df)
    hourly_quote = quotes_df.iloc[quote_index]
    return hourly_quote['Quote'], hourly_quote['Character']  # Assuming 'Quote' and 'Character' are column names

# Function to display the hourly quote and author with rotating colors
def display_quote():
    quote, author = get_hourly_quote()
    
    # Get next color in rotation for the quote and author
    quote_color = next(quote_colors)
    author_color = next(author_colors)
    
    tp_html = '<p style="color:black; font-family: Lucida Console, Monaco, monospace; font-size: 20px;"><br><br><strong>TimePass Quotes : </strong></p>'
    quote_html = f'<p style="color:{quote_color}; font-family: Lucida Console, Monaco, monospace; font-size: 20px;"><strong>{quote}</strong></p>'
    author_html = f'<p style="color:{author_color}; font-family: Lucida Console, Monaco, monospace; font-size: 16px;"><em>- {author}</em></p>'
    
    full_html = tp_html + quote_html + author_html
    st.sidebar.markdown(full_html, unsafe_allow_html=True)   # Display the combined quote and author in the sidebar

def custom_sidebar():
    st.sidebar.title("Features")
    st.sidebar.header("Available Options")  # Add a sidebar title
    # Create radio button group
    page_choice = st.sidebar.radio("", ["Document and Pdf Translation", "Text Translation", "Text Summarization"])
    
    return page_choice

# Display the logo at the top of the main page 
st.image(logo, use_column_width=True)

# Use the custom sidebar method
page_choice = custom_sidebar()

# Display the project description in the sidebar
project_description = '''
### Project Description
The Streamlit app is a language magician, effortlessly translating your text into a variety of languages using Google Translate. Not stopping there, it converts your translated text into spoken words, offering an audio player and download options. It's a one-stop-shop with an elegant interface featuring an image, a word count display, and a language selector, making language translation and speech synthesis a seamless experience. This handy tool ensures you can listen and download your translated speech in a snap, catering to different operating systems with ease.
'''
st.sidebar.markdown(project_description, unsafe_allow_html=True)

# Display the daily quote and author in the sidebar
display_quote()



# Depending on the selected choice, call the respective main function
if page_choice == "Document and Pdf Translation":
    page1.main()  # Call the main function for Page 1
elif page_choice == "Text Translation":
    page2.main()
elif page_choice == "Text Summarization":
    page3.main()  # Call the main function for Page 3
