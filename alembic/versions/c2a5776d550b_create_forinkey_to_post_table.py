"""create forinkey to post table

Revision ID: c2a5776d550b
Revises: 1e92b7f3e306
Create Date: 2024-01-25 11:20:01.207242

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c2a5776d550b'
down_revision: Union[str, None] = '1e92b7f3e306'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column('posts',sa.Column('owner_id',sa.Integer(),nullable=False))
    op.create_foreign_key('post_user_fk',source_table="posts",referent_table="users",local_cols=['owner_id'],remote_cols=['id'],ondelete="CASCADE")
    pass


def downgrade():
    op.drop_constraint('post_user_fk',table_name='posts')
    op.drop_column('posts','owner_id')
    pass
