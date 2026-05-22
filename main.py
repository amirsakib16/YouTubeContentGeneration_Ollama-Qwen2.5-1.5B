import streamlit as st
from config import YOUTUBE_API_KEY
from agents.orchestrator import ContentOrchestrator

st.set_page_config(
    page_title="AI YouTube Content Generator", layout="wide")

st.title("Agentic AI YouTube Content Generator")
if st.button("Generate Content Ideas"):
    if not YOUTUBE_API_KEY:
        st.error("Missing YOUTUBE_API_KEY in .env file")
        st.stop()
    with st.spinner("Agents are analyzing YouTube trends..."):
        orchestrator = ContentOrchestrator(YOUTUBE_API_KEY)
        result = orchestrator.run()

        st.subheader("Trending Topics")
        st.write(result["trends"])

        st.subheader("Content Strategy")
        st.write(result["strategy"])

        st.subheader("Scripts & Captions")
        st.write(result["scripts"])

        st.subheader("SEO Suggestions")
        st.write(result["seo"])