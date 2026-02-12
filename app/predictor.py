import joblib
import pandas as pd

# Load trained model
model = joblib.load("productivity_model.pkl")


# ---------------------------
# Prediction Function
# ---------------------------
def predict_productivity(study, sleep, screen, mood, exercise, caffeine, expenses):

    data = pd.DataFrame({
        "study_hours": [study],
        "sleep_hours": [sleep],
        "screen_time": [screen],
        "mood": [mood],
        "exercise_minutes": [exercise],
        "caffeine_cups": [caffeine],
        "expenses": [expenses]
    })

    prediction = model.predict(data)[0]

    return round(prediction, 2)


# ---------------------------
# Advisor Function
# ---------------------------
def productivity_advisor(study, sleep, screen, mood, exercise, caffeine, expenses):

    score = predict_productivity(study, sleep, screen, mood, exercise, caffeine, expenses)

    advice = []

    if study < 4:
        advice.append("Increase study hours.")

    if sleep < 6:
        advice.append("Improve sleep schedule.")

    if screen > 5:
        advice.append("Reduce screen time.")

    if exercise < 20:
        advice.append("Try adding some physical activity.")

    if mood < 5:
        advice.append("Focus on mental wellness.")

    return score, advice


# ---------------------------
# MAIN PROGRAM (This Runs Everything)
# ---------------------------
if __name__ == "__main__":

    print("\n📊 Personal Productivity Intelligence System")
    print("-------------------------------------------")

    study = float(input("Study hours: "))
    sleep = float(input("Sleep hours: "))
    screen = float(input("Screen time (hrs): "))
    mood = float(input("Mood (1-10): "))
    exercise = float(input("Exercise minutes: "))
    caffeine = float(input("Caffeine cups: "))
    expenses = float(input("Daily expenses: "))

    score, advice = productivity_advisor(
        study, sleep, screen, mood, exercise, caffeine, expenses
    )

    print("\n⭐ Predicted Productivity Score:", score)

    if advice:
        print("\n🧠 Suggestions to Improve:")
        for tip in advice:
            print("-", tip)
    else:
        print("\n🎉 Great lifestyle balance! Keep it up!")

