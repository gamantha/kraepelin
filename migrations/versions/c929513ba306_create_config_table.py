"""create config table

Revision ID: c929513ba306
Revises: d0185884232e
Create Date: 2018-08-31 09:36:32.483510

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c929513ba306'
down_revision = 'd0185884232e'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('config',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('column', sa.Integer),
        sa.Column('row', sa.Integer),
        )


def downgrade():
    op.drop_table('config')
