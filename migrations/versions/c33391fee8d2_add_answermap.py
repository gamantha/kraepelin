"""add answermap

Revision ID: c33391fee8d2
Revises: e283500f48c3
Create Date: 2019-03-11 19:04:24.101045

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c33391fee8d2'
down_revision = 'e283500f48c3'
branch_labels = None
depends_on = None

def upgrade():
    op.add_column('kraepelins', sa.Column('answer_map', sa.TEXT))

def downgrade():
    op.drop_column('kraepelins', 'answer_map')
