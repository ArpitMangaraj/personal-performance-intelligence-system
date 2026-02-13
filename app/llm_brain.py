import ollama


def generate_ai_advice(student_data, productivity_score):
    """
    Uses local LLM to generate intelligent productivity advice.
    """

    prompt = f"""
    You are an elite performance coach.

    A student has the following lifestyle data:

    Study Hours: {student_data['study']}
    Sleep Hours: {student_data['sleep']}
    Screen Time: {student_data['screen']}
    Mood: {student_data['mood']}
    Exercise Minutes: {student_data['exercise']}
    Caffeine Cups: {student_data['caffeine']}
    Daily Expenses: {student_data['expenses']}

    Their predicted productivity score is: {productivity_score}

    Give practical, science-backed advice to improve their productivity.
    Keep it structured and actionable.
    """

    response = ollama.chat(
        model="gemma3:4b",
        messages=[{"role": "user", "content": prompt}]
    )

    return response['message']['content']
