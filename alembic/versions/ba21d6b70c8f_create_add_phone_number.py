"""create add phone number

Revision ID: ba21d6b70c8f
Revises: dbdbcf2dec3f
Create Date: 2024-01-25 12:12:47.588329

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ba21d6b70c8f'
down_revision: Union[str, None] = 'dbdbcf2dec3f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column('users',sa.Column('Phone_number',sa.Integer(),nullable=False))
    pass


def downgrade():
    op.drop_column('users','Phone_number')
    pass
