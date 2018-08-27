"""add quota to user table

Revision ID: d0185884232e
Revises: be3156c96409
Create Date: 2018-08-27 08:45:51.534028

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd0185884232e'
down_revision = 'be3156c96409'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('users', sa.Column('quota', sa.Integer, default=0))    


def downgrade():
    op.drop_column('users', 'quota')    
