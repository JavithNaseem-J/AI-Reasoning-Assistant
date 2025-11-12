import streamlit as st
from core.rag_pipeline import RAGPipeline

st.set_page_config(page_title="AI Reasoning Assistant", layout="wide")
st.title("🧠 AI Reasoning Assistant (Agentic RAG System)")

query = st.text_input("Ask a question about your documents:")
if st.button("Run Reasoning"):
    if query:
        pipeline = RAGPipeline()
        with st.spinner("Reasoning in progress..."):
            result = pipeline.run(query)
        st.subheader("🪄 Final Answer")
        st.write(result["summary"])
        with st.expander("See Reasoning Steps"):
            st.write(result["analysis"])
        with st.expander("Evaluator Feedback"):
            st.write(result["evaluation"])
