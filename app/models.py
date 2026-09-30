from datetime import datetime

from sqlalchemy import DateTime, Float, ForeignKey, Integer, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .database import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True,
    )

    user_id: Mapped[str] = mapped_column(
        String(80),
        unique=True,
        index=True,
    )

    name: Mapped[str] = mapped_column(
        String(120)
    )

    age: Mapped[int] = mapped_column(
        Integer
    )

    weight_kg: Mapped[float] = mapped_column(
        Float
    )

    goal: Mapped[str] = mapped_column(
        String(40)
    )

    intensity: Mapped[str] = mapped_column(
        String(20)
    )

    experience: Mapped[str] = mapped_column(
        String(30),
        default="beginner",
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
    )

    plans: Mapped[list["WorkoutPlan"]] = relationship(
        back_populates="user",
        cascade="all, delete-orphan",
    )


class WorkoutPlan(Base):
    __tablename__ = "workout_plans"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True,
    )

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        index=True,
    )

    original_plan: Mapped[str] = mapped_column(
        Text
    )

    updated_plan: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    nutrition_tip: Mapped[str] = mapped_column(
        Text
    )

    last_feedback: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
    )

    user: Mapped[User] = relationship(
        back_populates="plans"
    )
