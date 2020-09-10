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
    op.execute('ALTER TABLE JOB ALTER COLUMN job_id Type INTEGER USING job_id::integer; ')
    op.execute('ALTER TABLE COMPANY ALTER COLUMN company_id Type INTEGER USING company_id::integer;')
    op.execute('ALTER TABLE JOB ALTER COLUMN contents Type VARCHAR USING contents::VARCHAR;')
    pass


def downgrade():
    op.execute('ALTER TABLE word ALTER COLUMN jobs_fk TYPE character varying[];')
    op.execute('ALTER TABLE JOB ALTER COLUMN job_id TYPE character VARCHAR;')
    op.execute('ALTER TABLE COMPANY ALTER COLUMN company_id TYPE VARCHAR;')
    pass
