"""relationship_task

Revision ID: ff2ec91ada93
Revises: 03ce8545cdcc
Create Date: 2024-02-16 11:19:58.956054

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ff2ec91ada93'
down_revision: Union[str, None] = '03ce8545cdcc'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tasks', sa.Column('created_at', sa.TIMESTAMP(), server_default=sa.text('now()'), nullable=True))
    op.add_column('tasks', sa.Column('updated_at', sa.TIMESTAMP(), server_default=sa.text('now()'), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('tasks', 'updated_at')
    op.drop_column('tasks', 'created_at')
    # ### end Alembic commands ###