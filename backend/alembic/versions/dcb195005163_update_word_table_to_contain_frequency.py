"""Update Word table to contain frequency

Revision ID: dcb195005163
Revises: 30f7603b8038
Create Date: 2020-08-29 08:11:40.354695

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'dcb195005163'
down_revision = '30f7603b8038'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('word', sa.Column('frequency', sa.INTEGER()))
    pass


def downgrade():
    op.drop_column("word", "frequency")
    pass
