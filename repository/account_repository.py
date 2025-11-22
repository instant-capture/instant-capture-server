from fastapi import Depends
from sqlalchemy.orm import Session
from database import get_db
from schema import Account

class AccountRepository:
    def __init__(self, db: Session = Depends(get_db)):
        self.db = db

    def create_account(self, userName: str, userImage: bytes) -> Account:
        account = Account(userName=userName, userImage=userImage)
        self.db.add(account)
        self.db.commit()
        self.db.refresh(account)

        return account