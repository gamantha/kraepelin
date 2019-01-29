"""delete user table

Revision ID: 409248a6c7b3
Revises: b4fa674f404a
Create Date: 2019-01-29 06:42:32.490845

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '409248a6c7b3'
down_revision = 'b4fa674f404a'
branch_labels = None
depends_on = None


def upgrade():
    op.drop_table('users')    


def downgrade():
    op.create_table('users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('email', sa.String(255)),
        sa.Column('quota', sa.Integer, default=0),
        sa.Column('created_at', sa.DateTime),
        sa.Column('updated_at', sa.DateTime)
        )

