from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from tronpy import Tron

from app.api.dao import WalletRequestDAO

router = APIRouter(prefix='/api', tags=['API'])

@router.post("/wallet-info/", response_class=JSONResponse)
async def get_wallet_info(wallet_address: str):
    client = Tron()  # инициализация клиента Tron

    try:
        # инфо о кошелке
        balance = client.get_account_balance(wallet_address)
        bandwidth = client.get_bandwidth(wallet_address)
        energy = client.get_energy(wallet_address)

        # сохранение в БД
        await WalletRequestDAO.add(wallet_address=wallet_address)

        return {
            "wallet_address": wallet_address,
            "balance": balance,
            "bandwidth": bandwidth,
            "energy": energy
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.get("/wallet-requests/")
async def get_wallet_requests():
    requests = await WalletRequestDAO.find_all()
    return requests