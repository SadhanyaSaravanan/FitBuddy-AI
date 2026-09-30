from ..schemas import UserInput, WorkoutPlan, WorkoutDay, Exercise


def generate_workout_gemini(user: UserInput) -> WorkoutPlan:

    days = [
        ("Day 1", "Full Body"),
        ("Day 2", "Cardio"),
        ("Day 3", "Upper Body"),
        ("Day 4", "Recovery"),
        ("Day 5", "Lower Body"),
        ("Day 6", "Core & Cardio"),
        ("Day 7", "Full Body & Stretching"),
    ]

    workout_days = []

    for day_name, focus in days:

        if focus == "Recovery":
            exercises = [
                Exercise(
                    name="Light Walking",
                    duration_minutes=20,
                    notes="Easy comfortable pace.",
                ),
                Exercise(
                    name="Gentle Stretching",
                    duration_minutes=15,
                    notes="Do not force any stretch.",
                ),
            ]

        elif focus == "Cardio":
            exercises = [
                Exercise(
                    name="Brisk Walking",
                    duration_minutes=20,
                    notes="Maintain a comfortable pace.",
                ),
                Exercise(
                    name="Jumping Jacks",
                    sets=3,
                    reps="15",
                    rest_seconds=45,
                ),
            ]

        elif focus == "Upper Body":
            exercises = [
                Exercise(
                    name="Push-ups",
                    sets=3,
                    reps="8-12",
                    rest_seconds=60,
                ),
                Exercise(
                    name="Bodyweight Rows",
                    sets=3,
                    reps="8-12",
                    rest_seconds=60,
                ),
                Exercise(
                    name="Shoulder Taps",
                    sets=3,
                    reps="10 each side",
                    rest_seconds=45,
                ),
            ]

        elif focus == "Lower Body":
            exercises = [
                Exercise(
                    name="Bodyweight Squats",
                    sets=3,
                    reps="12-15",
                    rest_seconds=60,
                ),
                Exercise(
                    name="Reverse Lunges",
                    sets=3,
                    reps="10 each leg",
                    rest_seconds=60,
                ),
                Exercise(
                    name="Glute Bridges",
                    sets=3,
                    reps="15",
                    rest_seconds=45,
                ),
            ]

        elif focus == "Core & Cardio":
            exercises = [
                Exercise(
                    name="Plank",
                    sets=3,
                    duration_minutes=1,
                    rest_seconds=45,
                ),
                Exercise(
                    name="Mountain Climbers",
                    sets=3,
                    reps="20",
                    rest_seconds=45,
                ),
                Exercise(
                    name="Brisk Walking",
                    duration_minutes=15,
                ),
            ]

        else:
            exercises = [
                Exercise(
                    name="Bodyweight Squats",
                    sets=3,
                    reps="12-15",
                    rest_seconds=60,
                ),
                Exercise(
                    name="Push-ups",
                    sets=3,
                    reps="8-12",
                    rest_seconds=60,
                ),
                Exercise(
                    name="Glute Bridges",
                    sets=3,
                    reps="15",
                    rest_seconds=45,
                ),
            ]

        workout_days.append(
            WorkoutDay(
                day=day_name,
                focus=focus,
                warmup="5-10 minutes of light walking and dynamic stretching.",
                exercises=exercises,
                cooldown="5-10 minutes of gentle stretching.",
                recovery_tip="Stay hydrated and allow adequate recovery.",
            )
        )

    return WorkoutPlan(
        title=f"7-Day {user.goal.title()} Workout Plan",
        overview=(
            f"This plan is designed for {user.name}, "
            f"with a goal of {user.goal} and "
            f"{user.intensity} workout intensity."
        ),
        days=workout_days,
        safety_note=(
            "Start gradually and stop if you experience pain, "
            "dizziness, or unusual discomfort. "
            "Consult a qualified professional for personalized medical advice."
        ),
    )
