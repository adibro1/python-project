    import streamlit as st
    from extractive import extractive_summaryhttp://localhost:8501/streamlit run app.py

    from abstractive import abstractive_summary

    st.title("📝 AI-Powered Notes Summarizer")

    text = st.text_area("Enter your notes here:", height=200)

    summary_type = st.radio("Choose summarization type:", ("Extractive", "Abstractive"))

    if st.button("Summarize"):
        if text.strip() == "":
            st.warning("Please enter some text to summarize.")
        else:
            if summary_type == "Extractive":
                summary = extractive_summary(text, num_sentences=3)
            else:
                summary = abstractive_summary(text)

            st.subheader("Summary:")
            st.write(summary)
