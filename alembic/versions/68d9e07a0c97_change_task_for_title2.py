"""change_task_for_title2

Revision ID: 68d9e07a0c97
Revises: 99e88e06c6b9
Create Date: 2024-02-13 20:45:03.224142

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '68d9e07a0c97'
down_revision: Union[str, None] = '99e88e06c6b9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('tasks', 'status',
               existing_type=postgresql.ENUM('PENDING', 'DONE', name='status_type'),
               type_=sa.String(length=20),
               existing_nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('tasks', 'status',
               existing_type=sa.String(length=20),
               type_=postgresql.ENUM('PENDING', 'DONE', name='status_type'),
               existing_nullable=True)
    # ### end Alembic commands ###
