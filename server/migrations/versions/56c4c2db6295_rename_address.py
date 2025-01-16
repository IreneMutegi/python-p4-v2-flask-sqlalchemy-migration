"""rename address

Revision ID: 56c4c2db6295
Revises: b1ea6920dfcf
Create Date: 2025-01-17 00:23:04.216031

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '56c4c2db6295'
down_revision = 'b1ea6920dfcf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('departments', schema=None) as batch_op:
        batch_op.add_column(sa.Column('location', sa.String(), nullable=True))
        batch_op.drop_column('address')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('departments', schema=None) as batch_op:
        batch_op.add_column(sa.Column('address', sa.VARCHAR(), nullable=True))
        batch_op.drop_column('location')
    # ### end Alembic commands ###
