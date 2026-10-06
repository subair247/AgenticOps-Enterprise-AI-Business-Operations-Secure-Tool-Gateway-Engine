import streamlit as st
import requests

st.set_page_config(
    page_title="AI-Ops Agent Platform",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Business Operations Agent Platform")
st.markdown("Enterprise-grade Autonomous Workflow System with Harness & Security Guardrails.")

with st.sidebar:
    st.header("Configuration")
    api_base_url = st.text_input("FastAPI Backend URL", value="http://localhost:8000/api/v1")
    api_key = st.text_input("API Key (X-API-Key)", type="password", value="dev_token_123")
    
    st.divider()
    agent_role = st.selectbox("Agent Role", ["standard_agent", "restricted_agent"])

st.subheader("Autonomous Task Execution Panel")
user_goal = st.text_area("Enter your business goal or operational request:", placeholder="e.g., Check company policy regarding remote work and summarize Q4 sales targets.")

if st.button("Run Agent Workflow", type="primary"):
    if not user_goal.strip():
        st.warning("Please enter a valid goal before running the agent.")
    else:
        with st.spinner("Agent is planning, executing, and checking the loop..."):
            try:
                headers = {"X-API-Key": api_key}
                payload = {"goal": user_goal, "role": agent_role}
                response = requests.post(f"{api_base_url}/run", json=payload, headers=headers, timeout=30)
                
                if response.status_code == 200:
                    data = response.json()
                    st.success("Agent Workflow Completed Successfully!")
                    st.markdown("### Execution Result:")
                    st.write(data.get("output"))
                else:
                    st.error(f"Error {response.status_code}: {response.json().get('detail', 'Unknown error occurred.')}")
            except Exception as e:
                st.error(f"Failed to connect to backend server: {str(e)}")