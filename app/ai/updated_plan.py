from ..schemas import WorkoutPlan


def update_workout_plan(
    original_plan: WorkoutPlan,
    feedback: str,
) -> WorkoutPlan:

    updated = original_plan.model_copy(deep=True)

    feedback_text = feedback.strip()

    updated.overview = (
        original_plan.overview
        + f" Updated based on user feedback: {feedback_text}"
    )

    updated.safety_note = (
        original_plan.safety_note
        + " Changes should be introduced gradually."
    )

    return updated
