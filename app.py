import streamlit as st
from transformers import pipeline
st.set_page_config(page_title="Text Summarization",layout="wide")


#summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
#summarizer.save_pretrained("./bart-large-cnn")

st.header("Summarize Extensive Text into Essential Ideas!")
input=st.text_area("Enter the text you need to summarize")
st.sidebar.markdown("Utilize our AI-powered summarization tool to effortlessly extract key points from any text, making information digestible and easy to understand.")
st.sidebar.markdown("----")
st.sidebar.subheader("Config model")
max_length = st.sidebar.number_input("Max Length of Summary", min_value=10, max_value=500, value=130)
min_length = st.sidebar.number_input("Min Length of Summary", min_value=1, max_value=100, value=30)

st.subheader("Select summary format")
summaryformat=st.radio('',('Short paragraph','Point wise'))


if st.button("Submit"):
   if input:
      summarizer = pipeline("summarization", model="./bart-large-cnn")
      with st.spinner("Generating summary... Please wait."):
         text=summarizer(input,max_length=max_length, min_length=min_length, do_sample=False)
         summary=text[0]["summary_text"]
         st.subheader("Summary:")
         if summaryformat=="Point wise":
            text1=summary.split(".")
            summary="\n- ".join(bp for bp in text1 if bp.strip())
            st.write(f"{summary}")
         else:
            st.markdown(summary)

   else:
      st.warning("Enter some text to summarize!!")

st.markdown("---")