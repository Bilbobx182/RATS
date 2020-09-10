"""WordFKUpdate

Revision ID: 5764e4fcd5ff
Revises: a75aa22b4649
Create Date: 2020-09-10 10:44:20.865271

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5764e4fcd5ff'
down_revision = 'a75aa22b4649'
branch_labels = None
depends_on = None


def upgrade():
    op.execute('ALTER TABLE word ALTER COLUMN jobs_fk Type INTEGER USING jobs_fk::integer;')
    pass


def downgrade():
    op.execute('ALTER TABLE word ALTER COLUMN jobs_fk TYPE character varying[];')
    pass
