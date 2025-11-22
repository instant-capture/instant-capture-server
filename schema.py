from sqlalchemy import ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy.dialects.mysql import INTEGER, VARCHAR, BOOLEAN, DATETIME, MEDIUMBLOB
from typing import List
from datetime import datetime

class Base(DeclarativeBase):
    pass

class Account(Base):
    __tablename__ = "account"

    userId: Mapped[int] = mapped_column(INTEGER(unsigned=True), primary_key=True, autoincrement=True)
    userName: Mapped[str] = mapped_column(VARCHAR(20), nullable=False)
    userImage: Mapped[bytes] = mapped_column(MEDIUMBLOB, nullable=False)

    sessions: Mapped[List["TrainSession"]] = relationship("TrainSession", back_populates="account")

class TrainSession(Base):
    __tablename__ = "train_session"

    sessionId: Mapped[int] = mapped_column(INTEGER(unsigned=True), primary_key=True, autoincrement=True)
    startedAt: Mapped[datetime] = mapped_column(DATETIME, nullable=False)
    endedAt: Mapped[datetime] = mapped_column(DATETIME, nullable=False)
    totalHit: Mapped[int] = mapped_column(INTEGER, nullable=False)
    userId: Mapped[int] = mapped_column(INTEGER(unsigned=True), ForeignKey("account.userId"), nullable=False)

    account: Mapped["Account"] = relationship("Account", back_populates="sessions")

    hits: Mapped[List["Hit"]] = relationship("Hit", back_populates="train_session")

class Hit(Base):
    __tablename__ = "hit"

    hitId: Mapped[int] = mapped_column(INTEGER(unsigned=True), primary_key=True)
    sessionId: Mapped[int] = mapped_column(INTEGER(unsigned=True), ForeignKey("train_session.sessionId"), nullable=False)
    hitAt: Mapped[datetime] = mapped_column(DATETIME, nullable=False)
    isHit: Mapped[bool] = mapped_column(BOOLEAN, nullable=False)
    
    train_session: Mapped["TrainSession"] = relationship("TrainSession", back_populates="hits")

if __name__ == "__main__":
    from database import engine
    
    Base.metadata.create_all(bind=engine)
    # Base.metadata.drop_all(bind=engine)