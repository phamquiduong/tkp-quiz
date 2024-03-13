import sqlalchemy as sa
from sqlalchemy.orm import relationship

from database import Base


class User(Base):
    __tablename__ = 'users'

    id = sa.Column(sa.Integer, primary_key=True)

    email = sa.Column(sa.String(255), unique=True)
    password = sa.Column(sa.String(255), nullable=False)

    is_teacher = sa.Column(sa.Boolean, default=False)

    group_id = sa.Column(sa.Integer(), sa.ForeignKey('groups.id'))
    group = relationship('Group', back_populates='users')
