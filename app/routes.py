import json
from pathlib import Path

from fastapi import APIRouter, Depends, Form, Request
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from .ai.gemini_flash_generator import (
    generate_nutrition_tip_with_flash,
)
from .ai.gemini_generator import (
    generate_workout_gemini,
)
from .ai.updated_plan import (
    update_workout_plan,
)
from .database import get_db
from .models import User, WorkoutPlan
from .schemas import (
    FeedbackRequest,
    UserInput,
    WorkoutPlan as WorkoutPlanSchema,
)


router = APIRouter()

BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATE_DIR = BASE_DIR / "templates"

templates = Jinja2Templates(
    directory=str(TEMPLATE_DIR)
)


@router.get("/")
def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={},
    )


@router.post("/generate-workout")
def generate_workout(
    request: Request,
    user_id: str = Form(...),
    name: str = Form(...),
    age: int = Form(...),
    weight_kg: float = Form(...),
    goal: str = Form(...),
    intensity: str = Form(...),
    experience: str = Form("beginner"),
    db: Session = Depends(get_db),
):
    try:
        user_input = UserInput(
            user_id=user_id,
            name=name,
            age=age,
            weight_kg=weight_kg,
            goal=goal,
            intensity=intensity,
            experience=experience,
        )

        workout_plan = generate_workout_gemini(
            user_input
        )

        nutrition = generate_nutrition_tip_with_flash(
            user_input.goal
        )

        user = (
            db.query(User)
            .filter(User.user_id == user_input.user_id)
            .first()
        )

        if user is None:
            user = User(
                user_id=user_input.user_id,
                name=user_input.name,
                age=user_input.age,
                weight_kg=user_input.weight_kg,
                goal=user_input.goal,
                intensity=user_input.intensity,
                experience=user_input.experience,
            )

            db.add(user)
            db.commit()
            db.refresh(user)

        else:
            user.name = user_input.name
            user.age = user_input.age
            user.weight_kg = user_input.weight_kg
            user.goal = user_input.goal
            user.intensity = user_input.intensity
            user.experience = user_input.experience

            db.commit()

        plan_record = WorkoutPlan(
            user_id=user.id,
            original_plan=workout_plan.model_dump_json(),
            nutrition_tip=nutrition.model_dump_json(),
        )

        db.add(plan_record)
        db.commit()
        db.refresh(plan_record)

        return templates.TemplateResponse(
            request=request,
            name="result.html",
            context={
                "user": user_input,
                "plan": workout_plan,
                "nutrition": nutrition,
                "plan_record_id": plan_record.id,
                "updated": False,
            },
        )

    except Exception as exc:
        return templates.TemplateResponse(
            request=request,
            name="error.html",
            context={
                "error": str(exc),
            },
            status_code=500,
        )


@router.post("/submit-feedback")
def submit_feedback(
    request: Request,
    user_id: str = Form(...),
    feedback: str = Form(...),
    db: Session = Depends(get_db),
):
    try:
        feedback_data = FeedbackRequest(
            user_id=user_id,
            feedback=feedback,
        )

        user = (
            db.query(User)
            .filter(User.user_id == feedback_data.user_id)
            .first()
        )

        if user is None:
            raise ValueError("User not found.")

        plan_record = (
            db.query(WorkoutPlan)
            .filter(WorkoutPlan.user_id == user.id)
            .order_by(WorkoutPlan.id.desc())
            .first()
        )

        if plan_record is None:
            raise ValueError("Workout plan not found.")

        original_plan = WorkoutPlanSchema.model_validate(
            json.loads(plan_record.original_plan)
        )

        updated_plan = update_workout_plan(
            original_plan,
            feedback_data.feedback,
        )

        plan_record.updated_plan = (
            updated_plan.model_dump_json()
        )

        plan_record.last_feedback = (
            feedback_data.feedback
        )

        db.commit()
        db.refresh(plan_record)

        nutrition = json.loads(
            plan_record.nutrition_tip
        )

        return templates.TemplateResponse(
            request=request,
            name="result.html",
            context={
                "user": UserInput(
                    user_id=user.user_id,
                    name=user.name,
                    age=user.age,
                    weight_kg=user.weight_kg,
                    goal=user.goal,
                    intensity=user.intensity,
                    experience=user.experience,
                ),
                "plan": original_plan,
                "updated_plan": updated_plan,
                "nutrition": nutrition,
                "plan_record_id": plan_record.id,
                "updated": True,
                "feedback": feedback_data.feedback,
            },
        )

    except Exception as exc:
        return templates.TemplateResponse(
            request=request,
            name="error.html",
            context={
                "error": str(exc),
            },
            status_code=500,
        )


@router.get("/view-all-users")
def view_all_users(
    request: Request,
    db: Session = Depends(get_db),
):
    users = db.query(User).all()

    return templates.TemplateResponse(
        request=request,
        name="all_users.html",
        context={
            "users": users,
        },
    )
