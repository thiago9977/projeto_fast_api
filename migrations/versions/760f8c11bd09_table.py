"""table

Revision ID: 760f8c11bd09
Revises: b6da37304758
Create Date: 2024-09-08 00:18:01.458833

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '760f8c11bd09'
down_revision: Union[str, None] = 'b6da37304758'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'updated_at')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('updated_at', sa.DATETIME(), nullable=False))
    # ### end Alembic commands ###
