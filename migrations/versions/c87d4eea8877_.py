"""empty message

Revision ID: c87d4eea8877
Revises: 
Create Date: 2023-04-27 10:35:33.212873

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c87d4eea8877'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('restaurant',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('rating', sa.Integer(), nullable=True),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('cuisine', sa.String(), nullable=True),
    sa.Column('distance_from_ada', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('restaurant')
    # ### end Alembic commands ###