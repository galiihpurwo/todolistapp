"""relate user have many tasks

Revision ID: dfa42bd4c9c4
Revises: c23dcae52190
Create Date: 2020-01-03 01:13:12.728873

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dfa42bd4c9c4'
down_revision = 'c23dcae52190'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('task', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'task', 'users', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'task', type_='foreignkey')
    op.drop_column('task', 'user_id')
    # ### end Alembic commands ###