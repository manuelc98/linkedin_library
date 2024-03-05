import streamlit as st
import pandas as pd
import time

# Display header
header1, header2= st.columns([1,9])
header1.image("https://upload.wikimedia.org/wikipedia/commons/thumb/8/81/LinkedIn_icon.svg/2048px-LinkedIn_icon.svg.png")
header2.title("Linkedin Library")
st.info("Got feedbacks? Happy to [connect](https://www.linkedin.com/in/manuel-cellier-821325166/)", icon ="ℹ️")

# Scrape the data
st.markdown("### 🛠️ Retrieve your Linkedin saved items")
st.markdown("👉 Follow this [step by step guide](https://github.com/manuelc98/linkedin_library/tree/main)")

# Read the data
st.markdown("### 🔍 Upload your data")
uploaded_file = st.file_uploader("Choose a file")


st.markdown("### 🎉 Enjoy your library")

if uploaded_file is not None:
    library_content = pd.read_csv(uploaded_file)
    library_content['optional_post_pic_link'] = library_content['optional_post_pic_link'].fillna("None")
    st.success('Data loaded successfully!')
    
    # Display data preview
    st.write("Data preview")
    st.write(library_content.head())

    if len(library_content) > 0:
        # Get unique authors from dataframe
        authors = library_content['author'].unique()

        st.markdown("## Data Summary")
        # Display total number of posts
        st.markdown(f"💡 You saved **{len(library_content)} posts** from **{len(authors)} authors**")

        # Display top 3 authors
        st.markdown("💥 Your Top 3 authors")
        top_3_authors = pd.DataFrame(library_content['author'].value_counts().sort_values(ascending=False)).head(3)
        top_3_authors = top_3_authors.rename(columns={"author": "Author", "count": "# Saved posts"})
        st.write(top_3_authors)

        # Consume your data
        with st.expander("Expand to see all your posts or search below"):
            for index, row in library_content.iterrows():
                with st.container():
                    st.image(row['profile_pic_link'])
                    st.markdown(row['author'])
                    if row['optional_post_pic_link'] != "None":
                        st.image(row['optional_post_pic_link'])
                    st.write(row['post_content'])
                    st.divider()

        search1, search2 = st.columns([1,1])

        with search1:
            # Author selection
            st.markdown('## Author')

            # Create a multiselect widget for selecting authors
            selected_authors = st.multiselect('Select authors', authors)

        with search2:
            # Display header
            st.markdown("## Content")

            # Search input
            search_query = st.text_input("Type keywords then press Enter")

        filtered_df = library_content.copy()

        # Filter dataframe based on search query
        if len(search_query)>0:
            filtered_df = library_content[library_content['post_content'].str.contains(search_query, case=False, na=False)]

        # Filter dataframe based on selected authors
        if len(selected_authors) > 0:
            filtered_df = library_content[library_content['author'].isin(selected_authors)]

        if len(search_query) > 0 or len(selected_authors) > 0:
            # Display posts for selected authors
            for index, row in filtered_df.iterrows():
                with st.container():
                    st.image(row['profile_pic_link'])
                    st.markdown(row['author'])
                    if row['optional_post_pic_link'] != "None":
                        st.image(row['optional_post_pic_link'])
                    st.write(row['post_content'])
                    st.divider()
