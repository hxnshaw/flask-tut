"""empty message

Revision ID: ac3b8f8eabb6
Revises: 21d83fe2743a
Create Date: 2024-07-16 14:22:34.737145

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ac3b8f8eabb6'
down_revision = '21d83fe2743a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('uid', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.Column('role', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('uid')
    )
    op.drop_table('people')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('people',
    sa.Column('pid', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.TEXT(), nullable=False),
    sa.Column('age', sa.INTEGER(), nullable=True),
    sa.Column('job', sa.TEXT(), nullable=True),
    sa.PrimaryKeyConstraint('pid')
    )
    op.drop_table('users')
    # ### end Alembic commands ###
