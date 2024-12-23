"""Add imageUrl column to Project model

Revision ID: 03eb7356e1e1
Revises: 7460454b26dd
Create Date: 2024-12-19 16:08:43.771104

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '03eb7356e1e1'
down_revision = '7460454b26dd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('project', schema=None) as batch_op:
        batch_op.add_column(sa.Column('imageUrl', sa.Text(), nullable=False, server_default=''))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('project', schema=None) as batch_op:
        batch_op.drop_column('imageUrl')

    # ### end Alembic commands ###
