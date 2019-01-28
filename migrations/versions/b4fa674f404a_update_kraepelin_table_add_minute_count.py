"""update kraepelin table add minute count

Revision ID: b4fa674f404a
Revises: 0301ae6543cd
Create Date: 2019-01-28 19:10:55.215767

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b4fa674f404a'
down_revision = '0301ae6543cd'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('kraepelins', sa.Column('minute_count', sa.Text))    


def downgrade():
    op.drop_column('kraepelins', 'minute_count')    
