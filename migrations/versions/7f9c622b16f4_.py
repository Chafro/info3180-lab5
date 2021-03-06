"""empty message

Revision ID: 7f9c622b16f4
Revises: adf1b29b9dff
Create Date: 2020-03-03 00:21:04.958273

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7f9c622b16f4'
down_revision = 'adf1b29b9dff'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user_profiles', 'password')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_profiles', sa.Column('password', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
