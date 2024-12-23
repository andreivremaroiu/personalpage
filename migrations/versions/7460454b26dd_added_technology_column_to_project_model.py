"""Added technology column to Project model

Revision ID: 7460454b26dd
Revises: 
Create Date: 2024-12-17 16:28:11.872675

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7460454b26dd'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('project',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=False),
    sa.Column('description', sa.Text(), nullable=False),
    sa.Column('technology', sa.String(length=100), nullable=False),
    sa.Column('yearCreated', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('project')
    # ### end Alembic commands ###
