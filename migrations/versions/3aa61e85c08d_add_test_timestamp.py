"""add test timestamp

Revision ID: 3aa61e85c08d
Revises: c929513ba306
Create Date: 2018-08-31 11:13:57.918978

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3aa61e85c08d'
down_revision = 'c929513ba306'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('kraepelins', sa.Column('starttime', sa.DateTime))
    op.add_column('kraepelins', sa.Column('endtime', sa.DateTime))
    


def downgrade():
    op.drop_column('kraepelins', 'starttime')
    op.drop_column('kraepelins', 'endtime')
    
