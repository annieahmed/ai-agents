import streamlit as st
from agents.password_checker import PasswordChecker
from agents.scam_detector import ScamDetector
from dotenv import load_dotenv
load_dotenv()
from agents.tips_generator import TipsGenerator
from agents.behavior_analyzer import BehaviorAnalyzer

st.set_page_config(page_title="CyberSafe AI", layout="centered")
st.title("🛡️ CyberSafe AI – Stay Safe Online")

menu = st.sidebar.radio("Choose Tool", ["🕵️ Scam Detector", "🔐 Password Checker", "📊 Digital Habit Checker", "💡 Safety Tip"])

if menu == "🕵️ Scam Detector":
    msg = st.text_area("Paste message, email or link:")
    if st.button("Analyze"):
        agent = ScamDetector()
        st.success(agent.analyze(msg))

elif menu == "🔐 Password Checker":
    pwd = st.text_input("Enter password (we won't save it)", type="password")
    if st.button("Check Strength"):
        agent = PasswordChecker()
        st.info(agent.check_strength(pwd))

elif menu == "📊 Digital Habit Checker":
    habit = st.text_input("Describe your online habit (e.g. 'I use same password')")
    if st.button("Check"):
        agent = BehaviorAnalyzer()
        st.warning(agent.analyze(habit))

elif menu == "💡 Safety Tip":
    agent = TipsGenerator()
    if st.button("Give Me a Tip"):
        st.success(agent.get_tip())
