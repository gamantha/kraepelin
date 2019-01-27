"""update kraepelin table

Revision ID: 0301ae6543cd
Revises: 3aa61e85c08d
Create Date: 2019-01-27 07:21:57.339232

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0301ae6543cd'
down_revision = '3aa61e85c08d'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('kraepelins', sa.Column('unfilled_count', sa.Text))
    op.add_column('kraepelins', sa.Column('incorrect_count', sa.Text))
    op.drop_column('kraepelins', 'correct_count')
    op.add_column('kraepelins', sa.Column('correct_count', sa.Text))

def downgrade():
    op.drop_column('kraepelins', 'unfilled_count')
    op.drop_column('kraepelins', 'incorrect_count')
    op.drop_column('kraepelins', 'correct_count')
    op.add_column('kraepelins', sa.Column('correct_count', sa.Integer))
    