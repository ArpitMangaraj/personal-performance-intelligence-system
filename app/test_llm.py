from llm_brain import generate_ai_advice

student = {
    "study": 5,
    "sleep": 6,
    "screen": 8,
    "mood": 6,
    "exercise": 20,
    "caffeine": 2,
    "expenses": 200
}

productivity_score = 72.5

advice = generate_ai_advice(student, productivity_score)

print("\n AI Performance Coach Says:\n")
print(advice)
