"""create user table

Revision ID: 1e92b7f3e306
Revises: 0d8405ed337b
Create Date: 2024-01-25 11:10:33.536095

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1e92b7f3e306'
down_revision: Union[str, None] = '0d8405ed337b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table('users',
                    sa.Column('id',sa.Integer(),nullable=False),
                              sa.Column('email',sa.String(),nullable=False),
                              sa.Column('password',sa.String(),nullable=False),
                              sa.Column('created_at',sa.TIMESTAMP(timezone=True),server_default=sa.text('now()'),nullable=False),
                              sa.PrimaryKeyConstraint('id'),sa.UniqueConstraint('email'))
    pass


def downgrade():
    op.drop_table('users')
    pass
