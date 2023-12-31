"""Initial migration

Revision ID: 2f7325572789
Revises: d1502b138087
Create Date: 2023-12-28 13:36:19.058431

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2f7325572789'
down_revision: Union[str, None] = 'd1502b138087'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        'debtors',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('full_name', sa.String),
        sa.Column('inn', sa.String),
        sa.Column('birth_date', sa.Date),
        sa.Column('birth_place', sa.String),
        sa.Column('region', sa.String),
        sa.Column('city', sa.String),
        sa.Column('street', sa.String),
        sa.Column('building', sa.String),
        sa.Column('apartment', sa.String)
    )

    op.create_table(
        'obligatory_payment',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String),
        sa.Column('sum', sa.Numeric)
    )

    op.create_table(
        'banks',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String),
        sa.Column('bik', sa.String)
    )

    op.create_table(
        'monetary_obligations',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('debtor_id', sa.Integer, sa.ForeignKey('debtors.id')),
        sa.Column('creditor_name', sa.String),
        sa.Column('total_sum', sa.Numeric),
        sa.Column('debt_sum', sa.Numeric),
        sa.Column('content', sa.String),
        sa.Column('basis', sa.String)
    )

    op.create_table(
        'extrajudicial_bankruptcy_message',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('number', sa.Integer),
        sa.Column('type', sa.String),
        sa.Column('publish_date', sa.Date)
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
