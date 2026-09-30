from ..schemas import NutritionTip


def generate_nutrition_tip_with_flash(goal: str) -> NutritionTip:

    tips = {
        "weight loss": NutritionTip(
            tip="Prioritize protein and vegetables in your meals.",
            rationale=(
                "Protein can help support muscle maintenance and "
                "satiety while vegetables provide useful nutrients "
                "and dietary fiber."
            ),
            practical_actions=[
                "Include a protein source in each main meal.",
                "Add vegetables to lunch and dinner.",
                "Drink enough water throughout the day.",
            ],
        ),

        "muscle gain": NutritionTip(
            tip="Include a quality protein source after training.",
            rationale=(
                "Protein provides amino acids that support muscle "
                "repair and adaptation after exercise."
            ),
            practical_actions=[
                "Include eggs, fish, chicken, beans or yogurt.",
                "Eat balanced meals consistently.",
                "Stay hydrated during the day.",
            ],
        ),

        "flexibility": NutritionTip(
            tip="Support recovery with balanced meals and hydration.",
            rationale=(
                "Adequate nutrition and hydration can support "
                "normal exercise recovery."
            ),
            practical_actions=[
                "Drink water regularly.",
                "Eat fruits and vegetables.",
                "Include protein in your meals.",
            ],
        ),

        "general wellness": NutritionTip(
            tip="Focus on balanced meals and consistent hydration.",
            rationale=(
                "A varied diet can provide the nutrients needed "
                "to support general health and activity."
            ),
            practical_actions=[
                "Eat a variety of vegetables and fruits.",
                "Include protein with meals.",
                "Drink water regularly.",
            ],
        ),
    }

    return tips.get(
        goal,
        tips["general wellness"],
    )
