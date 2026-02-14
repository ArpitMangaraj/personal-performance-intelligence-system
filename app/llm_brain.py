import os
import ollama
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

MODEL_NAME = os.getenv("OLLAMA_MODEL", "gemma3:4b")


def generate_ai_advice(student_data, productivity_score):
    """
    Uses local LLM to generate intelligent productivity advice.
    """

    # Safe dictionary access
    study = student_data.get("study", 0)
    sleep = student_data.get("sleep", 0)
    screen = student_data.get("screen", 0)
    mood = student_data.get("mood", 0)
    exercise = student_data.get("exercise", 0)
    caffeine = student_data.get("caffeine", 0)
    expenses = student_data.get("expenses", 0)

    prompt = f"""
You are an elite productivity performance coach.

Carefully analyze the student's lifestyle data and productivity score.

Student Data:
- Study Hours: {study}
- Sleep Hours: {sleep}
- Screen Time: {screen}
- Mood Level: {mood}
- Exercise Minutes: {exercise}
- Caffeine Cups: {caffeine}
- Daily Expenses: {expenses}

Predicted Productivity Score: {productivity_score:.2f}

Your Tasks:
1. Identify 2 strengths.
2. Identify 2 weaknesses.
3. Provide 3 specific actionable improvements.
4. Keep it structured and professional.
"""

    try:
        response = ollama.chat(
            model=MODEL_NAME,
            messages=[{"role": "user", "content": prompt}]
        )

        return response["message"]["content"]

    except Exception as e:
        return f"AI service temporarily unavailable.\n\nError: {str(e)}"
