import streamlit as st

def render_hitl_panel(api_client):
    st.subheader("🛡️ Human-in-the-Loop (HITL) Approvals")
    st.markdown("Review and authorize sensitive write operations requested by the autonomous agent before execution.")

    pending_action = "Execute WRITE operation: Update corporate policy record in PostgreSQL database."
    
    st.warning(f"Pending Agent Action: {pending_action}")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Approve & Execute", type="primary"):
            st.success("Action approved by human supervisor. Tool execution resumed!")
    with col2:
        if st.button("Reject / Halt"):
            st.error("Action rejected and safely halted by supervisor.")