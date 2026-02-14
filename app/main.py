import streamlit as st
import pandas as pd
import os
from datetime import datetime

from predictor import productivity_advisor
from llm_brain import generate_ai_advice


st.set_page_config(
    page_title="Personal Performance Intelligence System",
    layout="centered"
)

st.title("Personal Performance Intelligence System")
st.markdown("AI-powered productivity analysis using ML + LLM")

st.divider()

# User Inputs
study = st.slider("Study Hours", 0, 12, 5)
sleep = st.slider("Sleep Hours", 0, 12, 6)
screen = st.slider("Screen Time (hrs)", 0, 15, 4)
mood = st.slider("Mood (1-10)", 1, 10, 6)
exercise = st.slider("Exercise Minutes", 0, 120, 20)
caffeine = st.slider("Caffeine Cups", 0, 10, 2)
expenses = st.number_input("Daily Expenses", min_value=0.0, value=200.0)

file_path = "data/daily_logs.csv"

if st.button("Analyze My Productivity"):

    # ---- ML Prediction ----
    score, basic_advice = productivity_advisor(
        study, sleep, screen, mood, exercise, caffeine, expenses
    )

    # ---- Save Daily Record ----
    record = {
        "date": datetime.now(),
        "study": study,
        "sleep": sleep,
        "screen": screen,
        "mood": mood,
        "exercise": exercise,
        "caffeine": caffeine,
        "expenses": expenses,
        "productivity_score": score
    }

    df = pd.DataFrame([record])

    if os.path.exists(file_path):
        df.to_csv(file_path, mode="a", header=False, index=False)
    else:
        df.to_csv(file_path, index=False)

    # ---- LLM Dictionary ----
    student_data = {
        "study": study,
        "sleep": sleep,
        "screen": screen,
        "mood": mood,
        "exercise": exercise,
        "caffeine": caffeine,
        "expenses": expenses
    }

    # ---- Proper Spinner (FIXED) ----
    with st.spinner("AI is analyzing your lifestyle..."):
        ai_advice = generate_ai_advice(student_data, score)

    # ---- Display Results ----
    st.subheader("Predicted Productivity Score")
    st.success(f"{score:.2f}")

    st.subheader("Basic ML Suggestions")
    for tip in basic_advice:
        st.write(f"- {tip}")

    st.subheader("AI Insights (LLM Powered)")
    st.info(ai_advice)


# ---- Productivity Trend Section ----
if os.path.exists(file_path):
    history = pd.read_csv(file_path)

    st.divider()
    st.subheader("📈 Productivity Trend Over Time")

    st.line_chart(history["productivity_score"])
