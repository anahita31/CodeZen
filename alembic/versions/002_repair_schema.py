"""repair missing database schema

Revision ID: 002
Revises: 001
"""

from alembic import op
import app.models.models_init
from app.core.database import Base


revision = "002"
down_revision = "001"
branch_labels = None
depends_on = None


def upgrade() -> None:
    bind = op.get_bind()
    Base.metadata.create_all(bind=bind)


def downgrade() -> None:
    pass
