import pytest
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.database import async_session_maker
from app.api.models import WalletRequest
from app.api.dao import WalletRequestDAO

@pytest.mark.asyncio
async def test_add_wallet_request():
    wallet_address = "TXYZ1234567890abcdefghijklmnopqrstuvw"
    new_request = await WalletRequestDAO.add(wallet_address=wallet_address)

    assert new_request.id is not None
    assert new_request.wallet_address == wallet_address

    # проерка в БД
    async with async_session_maker() as session:
        result = await session.execute(select(WalletRequest).where(WalletRequest.id == new_request.id))
        saved_request = result.scalars().first()
        assert saved_request is not None
        assert saved_request.wallet_address == wallet_address