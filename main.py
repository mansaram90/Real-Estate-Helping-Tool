# @Author: Dhaval Patel Copyrights Codebasics Inc. and LearnerX Pvt Ltd.

import streamlit as st
from rag import process_urls, generate_answer

st.title("Real Estate Research Tool")

if "urls_processed" not in st.session_state:
    st.session_state.urls_processed = False

url1 = st.sidebar.text_input("URL 1")
url2 = st.sidebar.text_input("URL 2")
url3 = st.sidebar.text_input("URL 3")

status_placeholder = st.empty()

process_url_button = st.sidebar.button("Process URLs")
if process_url_button:
    st.session_state.urls_processed = False
    urls = [url for url in (url1, url2, url3) if url!='']
    if len(urls) == 0:
        status_placeholder.warning("You must provide at least one valid url")
    else:
        for status in process_urls(urls):
            status_placeholder.info(status)
            if status.startswith("Done adding"):
                st.session_state.urls_processed = True

query = st.text_input("Question")
if query:
    if not st.session_state.urls_processed:
        st.warning("Process URLs first, then ask your question.")
    else:
        try:
            answer, sources = generate_answer(query)
            st.header("Answer:")
            st.write(answer)

            if sources:
                st.subheader("Sources:")
                for source in sources.split("\n"):
                    st.write(source)
        except RuntimeError as e:
            st.warning(str(e))
