from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from utils.db import db


class Contact(db.Model):
    __tablename__ = "contacts"
    id: Mapped[int] = mapped_column(primary_key=True)
    fullname:  Mapped[str] = mapped_column(String(100))
    email:  Mapped[str] = mapped_column(String(100))
    phone: Mapped[str] = mapped_column(String(100))
    
    def __init__(self, fullname, email, phone):
        self.fullname = fullname
        self.email = email
        self.phone = phone