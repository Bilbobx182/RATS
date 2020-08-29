"""Update Job table

Revision ID: a75aa22b4649
Revises: cc14c453e91e
Create Date: 2020-08-29 09:56:01.004406

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a75aa22b4649'
down_revision = 'cc14c453e91e'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('job', sa.Column('title', sa.VARCHAR, nullable=True))
    pass


def downgrade():
    op.drop_column("job", "title")
    pass
