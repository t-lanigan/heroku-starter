"""empty message

Revision ID: 6858a90c738a
Revises: 5348a0a108bf
Create Date: 2020-06-14 14:23:08.034123

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6858a90c738a'
down_revision = '5348a0a108bf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('peoples')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('peoples',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('catchphrase', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='peoples_pkey')
    )
    # ### end Alembic commands ###
