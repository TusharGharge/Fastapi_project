"""create content

Revision ID: 0d8405ed337b
Revises: ee181ec7df3b
Create Date: 2024-01-25 11:06:10.020652

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0d8405ed337b'
down_revision: Union[str, None] = 'ee181ec7df3b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column('posts',sa.Column('content',sa.String,nullable=False))
    pass


def downgrade():
    op.drop_column('posts','content')
    pass
