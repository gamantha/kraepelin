"""add-basic-user-table

Revision ID: be3156c96409
Revises: 2d054ba80ea5
Create Date: 2018-08-26 13:23:53.420503

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'be3156c96409'
down_revision = '2d054ba80ea5'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('email', sa.String(255)),
        sa.Column('created_at', sa.DateTime),
        sa.Column('updated_at', sa.DateTime)
        )

def downgrade():
    op.drop_table('users')
