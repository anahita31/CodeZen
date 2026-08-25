"""repair missing database schema

Revision ID: 002
Revises: 001
"""

from alembic import op
import sqlalchemy as sa

revision = "002"
down_revision = "001"
branch_labels = None
depends_on = None


def upgrade() -> None:
    bind = op.get_bind()

    # Create missing tables from the initial schema.
    # This is safe because existing tables are checked first.
    from app.core.database import Base
    import app.models.models_init

    Base.metadata.create_all(bind=bind)


def downgrade() -> None:
    pass
