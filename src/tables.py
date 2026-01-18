from sqlalchemy import String, Text, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

class Base(DeclarativeBase):
    pass

class Users(Base):
    __tablename__ = "users"
    
    email: Mapped[str] = mapped_column(String(200), primary_key=True)

    groups: Mapped[list["Groups"]] = relationship(
        back_populates="user",
        cascade="all, delete-orphan"
    )


class Groups(Base):
    __tablename__ = "groups"

    id: Mapped[str] = mapped_column(String(36), primary_key=True)
    name: Mapped[str] = mapped_column(String(120))
    description: Mapped[str] = mapped_column(Text)

    user_email: Mapped[str] = mapped_column(
        ForeignKey("users.email"),
        nullable=False
    )

    user: Mapped["Users"] = relationship(
        back_populates="groups"
    )

    tasks: Mapped[list["Items"]] = relationship(
        back_populates="group",
        cascade="all, delete-orphan"
    )


class Items(Base):
    __tablename__ = "items"
    
    id: Mapped[str] = mapped_column(String(36), primary_key=True)
    text: Mapped[str] = mapped_column(Text)

    group_id: Mapped[str] = mapped_column(
        ForeignKey("groups.id"),
        nullable=False
    )

    group: Mapped["Groups"] = relationship(
        back_populates="tasks"
    )
