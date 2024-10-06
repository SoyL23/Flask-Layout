from config.db import Base
from models.user_model import User
from sqlalchemy import (
    Column,
    Integer,
    DateTime,
    func,
    Enum,
    ForeignKey,
    Boolean,
    String,
)
import enum


class LogEvents(enum.Enum):
    LOGIN = "LOGIN"
    LOGOUT = "LOGOUT"


class AuthLogs(Base):
    __tablename__ = "auth_logs"

    id = Column(Integer(), primary_key=True, autoincrement=True)
    event = Column(Enum(LogEvents), nullable=False)
    date = Column(DateTime(), nullable=False, server_default=func.now())
    success = Column(Boolean(), nullable=False)
    ip = Column(String(12), nullable=False)
    user_id = Column(Integer(), ForeignKey("Users.User_id"), nullable=True)

    def to_dict(self):
        return {
            "id": self.id,
            "event": self.event.value,
            "date": self.date.isoformat() if self.date else None,
            "success": self.success,
            "ip": self.ip,
            "user_id": self.user_id,
        }
