from typing import TYPE_CHECKING


from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Text, ForeignKey

from .base import Base
from .mixins import UserRelationMixin

if TYPE_CHECKING:
    from.user import User


class Post(UserRelationMixin, Base):
    _user_back_populates = "posts"

    title: Mapped[str] = mapped_column(String(100), unique=True)
    body: Mapped[str] = mapped_column(
        Text, 
        default="",
        server_default="",
    )
    
    
