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
    op.create_table('word',
        sa.Column('word_id', sa.VARCHAR, primary_key=True),
        sa.Column('jobs_fk',  postgresql.ARRAY(sa.String()), nullable=True))

    op.create_table('job',
        sa.Column('job_id', sa.INTEGER, primary_key=True, autoincrement=True),
        sa.Column('company_id', sa.INTEGER,nullable=True),
       # TODO Have a pay min and pay max. But right now a range string is enough.
        sa.Column('pay', sa.VARCHAR, nullable=True),
        sa.Column('date_posted', sa.VARCHAR, nullable=True),
        sa.Column('has_pension', sa.BOOLEAN, nullable=True),
        sa.Column('has_healthcare', sa.BOOLEAN, nullable=True),
        sa.Column('has_stock', sa.BOOLEAN, nullable=True),
        # TODO Deal with edge case later of "London and Dublin" type role. >:(
        sa.Column('locations_id', sa.INTEGER, nullable=True),
        sa.Column('contents', sa.JSON, nullable=True),)

    # TODO Implement job engagement for analytics
    # op.create_table('job_engagement',
    #     sa.Column('job_id', sa.VARCHAR, primary_key=True, autoincrement=True),
    #     sa.Column('applied',  postgresql.ARRAY(sa.String()), nullable=True),
    #     sa.Column('views', postgresql.ARRAY(sa.String()), nullable=True))

    op.create_table('company',
        sa.Column('company_id', sa.INTEGER, primary_key=True, autoincrement=True),
        sa.Column('name', sa.VARCHAR, nullable=True),
         sa.Column('location_id', sa.INTEGER, nullable=True),
        sa.Column('jobs_fk',   sa.VARCHAR, nullable=True))

    op.create_table('location',
        sa.Column('location_id',  sa.INTEGER, primary_key=True, autoincrement=True),
        sa.Column('country', sa.VARCHAR, nullable=True),
        sa.Column('state', sa.VARCHAR, nullable=True),
        # TODO Implement GPS at a later point. Convert Address to GPS for maps.
        #sa.Column('gps', sa.VARCHAR, nullable=True)
        sa.Column('city', sa.VARCHAR, nullable=True))


    # Constraints

    op.create_foreign_key(u'company_job', 'job', 'company', ['company_id'], ['company_id'])
    op.create_foreign_key(u'company_location', 'company', 'location', ['location_id'], ['location_id'])
    pass


def downgrade():
    print("No rollback base commit!")
    pass
