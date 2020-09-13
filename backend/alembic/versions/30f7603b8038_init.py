"""Init

Revision ID: 30f7603b8038
Revises: 
Create Date: 2020-08-28 19:16:22.868464

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


# revision identifiers, used by Alembic.
revision = '30f7603b8038'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # Ideally we would have a composite key as the PK of Job + Word
    # but that may break things in a scenario a company reposts the same job a year later.

    op.create_table('word',
        sa.Column('id', sa.INTEGER, primary_key=True, autoincrement=True),
        sa.Column('word', sa.VARCHAR),
        sa.Column('jobs_fk', sa.INTEGER),
        sa.Column('frequency', sa.INTEGER()))

    op.create_table('job',
        sa.Column('job_id', sa.INTEGER, primary_key=True, autoincrement=True),
        sa.Column('job_title', sa.VARCHAR),
        sa.Column('company_id', sa.INTEGER),
        sa.Column('date_posted', sa.VARCHAR),
        sa.Column('contents', sa.VARCHAR))


    op.create_table('company',
        sa.Column('company_id', sa.INTEGER, primary_key=True, autoincrement=True),
        sa.Column('name', sa.VARCHAR))


    # Constraints

    op.create_foreign_key(u'company_job', 'job', 'company', ['company_id'], ['company_id'])
    pass


def downgrade():
    print("No rollback base commit!")
    pass
