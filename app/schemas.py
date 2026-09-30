from typing import Literal

from pydantic import BaseModel, ConfigDict, Field, field_validator


Goal = Literal[
    "weight loss",
    "muscle gain",
    "general wellness",
    "flexibility",
]

Intensity = Literal[
    "low",
    "medium",
    "high",
]

Experience = Literal[
    "beginner",
    "intermediate",
    "advanced",
]


class UserInput(BaseModel):
    model_config = ConfigDict(
        str_strip_whitespace=True
    )

    user_id: str = Field(
        min_length=2,
        max_length=80,
    )

    name: str = Field(
        min_length=1,
        max_length=120,
    )

    age: int = Field(
        ge=13,
        le=100,
    )

    weight_kg: float = Field(
        gt=20,
        le=500,
    )

    goal: Goal

    intensity: Intensity

    experience: Experience = "beginner"

    @field_validator("user_id")
    @classmethod
    def validate_user_id(cls, value: str) -> str:
        allowed = set(
            "abcdefghijklmnopqrstuvwxyz"
            "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            "0123456789-_"
        )

        if not set(value) <= allowed:
            raise ValueError(
                "User ID may contain only letters, numbers, "
                "hyphens and underscores."
            )

        return value


class FeedbackRequest(BaseModel):
    model_config = ConfigDict(
        str_strip_whitespace=True
    )

    user_id: str = Field(
        min_length=2,
        max_length=80,
    )

    feedback: str = Field(
        min_length=5,
        max_length=2000,
    )


class Exercise(BaseModel):
    name: str

    sets: int | None = Field(
        default=None,
        ge=1,
        le=10,
    )

    reps: str | None = None

    duration_minutes: int | None = Field(
        default=None,
        ge=1,
        le=180,
    )

    rest_seconds: int | None = Field(
        default=None,
        ge=0,
        le=600,
    )

    notes: str | None = None


class WorkoutDay(BaseModel):
    day: str
    focus: str
    warmup: str
    exercises: list[Exercise]
    cooldown: str
    recovery_tip: str


class WorkoutPlan(BaseModel):
    title: str
    overview: str
    days: list[WorkoutDay] = Field(
        min_length=7,
        max_length=7,
    )
    safety_note: str


class NutritionTip(BaseModel):
    tip: str
    rationale: str
    practical_actions: list[str] = Field(
        min_length=1,
        max_length=5,
    )
