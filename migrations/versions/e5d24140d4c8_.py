"""empty message

Revision ID: e5d24140d4c8
Revises: 
Create Date: 2022-05-07 19:53:21.104585

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e5d24140d4c8'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('author',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name_db', sa.Text(), nullable=True),
    sa.Column('last_name_db', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('rent',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('rent_db', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_rent_rent_db'), 'rent', ['rent_db'], unique=False)
    op.create_table('book',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title_db', sa.String(length=100), nullable=True),
    sa.Column('description_db', sa.String(length=200), nullable=True),
    sa.Column('date_db', sa.String(length=100), nullable=True),
    sa.Column('booklist', sa.String(length=100), nullable=True),
    sa.ForeignKeyConstraint(['booklist'], ['rent.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_book_date_db'), 'book', ['date_db'], unique=False)
    op.create_index(op.f('ix_book_description_db'), 'book', ['description_db'], unique=False)
    op.create_index(op.f('ix_book_title_db'), 'book', ['title_db'], unique=True)
    op.create_table('book_list',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('book_id_db', sa.Integer(), nullable=True),
    sa.Column('author_id_db', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['author_id_db'], ['author.id'], ),
    sa.ForeignKeyConstraint(['book_id_db'], ['book.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('book_list')
    op.drop_index(op.f('ix_book_title_db'), table_name='book')
    op.drop_index(op.f('ix_book_description_db'), table_name='book')
    op.drop_index(op.f('ix_book_date_db'), table_name='book')
    op.drop_table('book')
    op.drop_index(op.f('ix_rent_rent_db'), table_name='rent')
    op.drop_table('rent')
    op.drop_table('author')
    # ### end Alembic commands ###
