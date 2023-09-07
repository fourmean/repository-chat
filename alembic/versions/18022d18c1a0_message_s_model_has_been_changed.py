"""Message's model has been changed

Revision ID: 18022d18c1a0
Revises: 841162bfdae0
Create Date: 2023-09-06 18:22:25.481769

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '18022d18c1a0'
down_revision: Union[str, None] = '841162bfdae0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('messages', sa.Column('chat_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'messages', 'chats', ['chat_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'messages', type_='foreignkey')
    op.drop_column('messages', 'chat_id')
    # ### end Alembic commands ###
