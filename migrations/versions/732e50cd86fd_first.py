"""First

Revision ID: 732e50cd86fd
Revises: 
Create Date: 2024-07-22 17:07:19.714712

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '732e50cd86fd'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # 테이블 생성
    op.create_table(
        'TB_DAY',
        sa.Column('day_id', sa.Integer, primary_key=True)
    )
    op.create_table(
       'TB_TODO',
       sa.Column('todo_id', sa.Integer, primary_key=True),
       sa.Column('context', sa.Text, nullable=False),
       sa.Column('created_at', sa.DateTime, nullable=False),
       sa.Column('modified_at', sa.DateTime, nullable=False)
   )


def downgrade() -> None:
    pass
