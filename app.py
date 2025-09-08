import os
import streamlit as st

# ✅ Set env vars from Streamlit secrets BEFORE importing agent_runner
if "GEMINI_API_KEY" in st.secrets:
    os.environ["GEMINI_API_KEY"] = st.secrets["GEMINI_API_KEY"]
# set GOOGLE_API_KEY too, for compatibility with google-genai
if "GOOGLE_API_KEY" in st.secrets:
    os.environ["GOOGLE_API_KEY"] = st.secrets["GOOGLE_API_KEY"]
elif "GEMINI_API_KEY" in st.secrets:
    os.environ["GOOGLE_API_KEY"] = st.secrets["GEMINI_API_KEY"]

import json
from agents.agent_runner import run_scenario_text

st.set_page_config(page_title="Synapse Agent Demo", layout="wide")

st.title("🤖 Project Synapse Demo")
st.write("Interactive demo of the Synapse agent. Choose a scenario or enter your own.")

# Sidebar for inputs
st.sidebar.header("Scenario Selection")
scenario_choice = st.sidebar.radio(
    "Pick a scenario:",
    ["Overloaded Restaurant", "Damaged Packaging Dispute", "Recipient Unavailable", "Traffic Obstruction", "Custom"]
)

scenario_text = ""
if scenario_choice == "Overloaded Restaurant":
    scenario_text = "An order is placed, but get_merchant_status() shows 40-min kitchen prep time."
elif scenario_choice == "Damaged Packaging Dispute":
    scenario_text = "At delivery, dispute arises over spilled drink; unclear if merchant packaging or driver fault."
elif scenario_choice == "Recipient Unavailable":
    scenario_text = "Driver arrives at destination but recipient is unavailable to receive package."
elif scenario_choice == "Traffic Obstruction":
    scenario_text = "Passenger is on urgent trip; check_traffic() detects major accident on planned route."
else:
    scenario_text = st.sidebar.text_area("Describe your scenario:")

# Run agent button
if st.sidebar.button("Run Scenario"):
    if scenario_text.strip() == "":
        st.warning("Please enter a scenario.")
    else:
        with st.spinner("Running Synapse agent..."):
            result = run_scenario_text(scenario_text)
        
        # ✅ SHOW FINAL PLAN FIRST
        st.subheader("✅ Final Plan")
        if result["final_plan"]:
            st.success(result["final_plan"])
        else:
            st.info("No final plan generated.")
        
        # ✅ SHOW AGENT TRACE SECOND (with expander for better UX)
        with st.expander("🔍 View Detailed Agent Trace", expanded=False):
            steps = result["trace"].splitlines()
            for line in steps:
                if line.startswith("THOUGHT:"):
                    st.markdown(f"🧠 **{line}**")
                elif line.startswith("ACTION:"):
                    st.markdown(f"🔧 `{line}`")
                elif line.startswith("OBSERVATION:"):
                    try:
                        obs = json.loads(line.replace("OBSERVATION:", "").strip())
                        st.json(obs)
                    except:
                        st.write(line)
                elif line.startswith("POLICY:"):
                    try:
                        pol = json.loads(line.replace("POLICY:", "").strip())
                        color = "red" if pol.get("escalate") else "green"
                        st.markdown(f"🛡️ **POLICY (conf {pol['confidence']})**")
                        st.json(pol)
                    except:
                        st.write(line)
                elif line.startswith("FINAL_PLAN:"):
                    st.success(line)
