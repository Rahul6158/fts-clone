import streamlit as st
import pandas as pd

def upload_page():
    st.title("Dataset Handler - Upload")
    uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

    if uploaded_file is not None:
        st.session_state.uploaded_data = pd.read_csv(uploaded_file)
        st.success("File uploaded successfully!")
        st.session_state.page = "Data Details"

def data_details_page():
    st.title("Dataset Handler - Data Details")
    df = st.session_state.uploaded_data

    # Display basic details about the dataset
    st.subheader("Dataset Information:")
    st.write(f"Number of Rows: {df.shape[0]}")
    st.write(f"Number of Columns: {df.shape[1]}")
    st.write("Preview of the Dataset:")
    st.write(df.head())

    # Show null value counts
    st.subheader("Null Values in the Dataset:")
    st.write(df.isnull().sum())

    # Button to clear null values
    if st.button("Clear Null Values"):
        modified_df = df.dropna()  # Remove rows with null values
        st.session_state.modified_data = modified_df
        st.success("Null values cleared successfully!")
        st.session_state.page = "Modified Data"

def modified_data_page():
    st.title("Dataset Handler - Modified Data")
    modified_df = st.session_state.modified_data

    # Display modified data
    st.write("Modified Dataset:")
    st.write(modified_df.head())

    # Download the modified dataset as CSV
    if st.button("Download Modified Dataset"):
        csv_file = modified_df.to_csv(index=False)
        b64 = base64.b64encode(csv_file.encode()).decode()
        href = f'<a href="data:file/csv;base64,{b64}" download="modified_dataset.csv">Download Modified Dataset</a>'
        st.markdown(href, unsafe_allow_html=True)

def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Upload", "Data Details", "Modified Data"])

    if "uploaded_data" not in st.session_state:
        st.session_state.uploaded_data = None
    if "modified_data" not in st.session_state:
        st.session_state.modified_data = None
    if "page" not in st.session_state:
        st.session_state.page = "Upload"

    if page == "Upload":
        upload_page()
    elif page == "Data Details":
        data_details_page()
    elif page == "Modified Data":
        modified_data_page()

if __name__ == "__main__":
    main()
