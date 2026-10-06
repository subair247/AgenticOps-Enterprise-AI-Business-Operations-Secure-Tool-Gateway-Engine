import streamlit as st

def render_chat_box(api_client):
    st.subheader("💬 Interactive Agent Chat")
    
    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("Ask the agent anything..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            with st.spinner("Agent is thinking & executing loop..."):
                try:
                    response = api_client.run_agent(goal=prompt)
                    if response.status_code == 200:
                        output = response.json().get("output", "Completed.")
                    else:
                        output = f"Error {response.status_code}: {response.text}"
                except Exception as e:
                    output = f"Failed to reach backend: {str(e)}"
                
                st.markdown(output)
        st.session_state.messages.append({"role": "assistant", "content": output})