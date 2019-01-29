"""add quota table

Revision ID: e283500f48c3
Revises: 409248a6c7b3
Create Date: 2019-01-29 06:44:33.659809

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e283500f48c3'
down_revision = '409248a6c7b3'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('quota',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('user_id', sa.Integer),
        sa.Column('quota', sa.Integer, default=0),
        )


def downgrade():
    op.drop_table('quota')

