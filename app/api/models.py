from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base, int_pk

class WalletRequest(Base):
    __tablename__ = "wallet_requests"
    id: Mapped[int_pk]
    wallet_address: Mapped[str] = mapped_column(String)

    extend_existing = True

    def __repr__(self):
        return f"{self.__class__.__name__}(id={self.id})"