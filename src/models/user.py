import sqlalchemy as sa
from sqlalchemy.orm import relationship

from db import Base


class User(Base):
    __tablename__ = 'users'

    email = sa.Column(sa.String(255), primary_key=True)
    password = sa.Column(sa.String(255), nullable=False)

    group_id = sa.Column(sa.Integer(), sa.ForeignKey('groups.id'))
    group = relationship('Group', back_populates='users')
