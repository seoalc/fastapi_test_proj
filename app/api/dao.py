from app.dao.base import BaseDAO
from app.api.models import WalletRequest

class WalletRequestDAO(BaseDAO):
    model = WalletRequest
