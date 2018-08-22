"""add_filled_count_column

Revision ID: 2d054ba80ea5
Revises: 89667820f7f6
Create Date: 2018-08-22 11:16:48.534863

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2d054ba80ea5'
down_revision = '89667820f7f6'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('kraepelins', sa.Column('filled_count', sa.TEXT))

def downgrade():
    op.drop_column('kraepelins', 'filled_count')
