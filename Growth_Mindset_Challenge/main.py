import streamlit as st
import random




st.markdown("## 🌱 Growth Mindset Challenge")
st.write("Boost your mindset with a daily challenge that inspires growth, learning, and self-improvement.")

challenges = [
    "✨ Try something new today, even if it scares you a little.",
    "📚 Learn from a mistake you made recently.",
    "💪 Turn a failure into a lesson.",
    "🧠 Replace 'I can’t do this' with 'I can’t do this **yet**.'",
    "🎯 Set a small goal and take one step towards it.",
    "🌟 Praise the effort, not just the result.",
    "🔄 Ask for feedback today—and use it to grow.",
    "📖 Read about someone who overcame big challenges.",
    "📝 Write down one thing you learned today.",
    "💬 Share a positive thought with someone else."
]

if st.button("🎁 Give mine challenge!"):
    challenge = random.choice(challenges)
    st.markdown(challenge)

st.markdown('<p style = "text-align : right;">Built by ❤️ Muzna Amir Zubairi</p>', unsafe_allow_html=True)
