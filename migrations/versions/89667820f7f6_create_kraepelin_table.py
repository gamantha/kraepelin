"""create-kraepelin-table

Revision ID: 89667820f7f6
Revises: 
Create Date: 2018-08-13 18:47:20.783749

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '89667820f7f6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('kraepelins',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('user_id', sa.String(255)),
        sa.Column('answers', sa.Text),
        sa.Column('questions', sa.Text),
        sa.Column('correct_count', sa.Integer),
        sa.Column('answer_count', sa.Integer),
        sa.Column('created_at', sa.DateTime),
        sa.Column('updated_at', sa.DateTime)
        )

def downgrade():
    op.drop_table('kraepelins')
