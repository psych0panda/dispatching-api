import requests
from fastapi import Depends, APIRouter, HTTPException, status, Request
from app.utils.dependencies import get_current_user
import httpx

router = APIRouter()


@router.get("/heat-meter-reading")
async def get_heat_meter_reading(request: Request, serial_number: str, current_user=Depends(get_current_user)):
    heat_meters_url = f"http://10.2.33.21:8000/result/heat/1/{serial_number}"
    headers = {"authorization": request.headers["authorization"]}
    async with httpx.AsyncClient() as client:
        heat_meter = await client.get(heat_meters_url, headers=headers)
        if heat_meter.status_code == 200:
            return heat_meter.json()

    return {
        "access_no": 50,
        "identification": "00000001",
        "manufacturer": "NIK",
        "medium": 4,
        "records": [
            {
                "type": "Date time general",
                "unit": "date time",
                "value": "2000-05-09T21:29"
            },
            {
                "type": "Energy wh",
                "unit": "WH",
                "value": 8015300
            },
            {
                "type": "Volume",
                "unit": "m^3",
                "value": 249.207999999999998408384271897375583648681640625
            },
            {
                "type": "Power w",
                "unit": "W",
                "value": 0
            },
            {
                "type": "Volume flow",
                "unit": "m^3/h",
                "value": 0
            },
            {
                "type": "Flow temperature",
                "unit": "C",
                "value": 24.21000000000000085265128291212022304534912109375
            },
            {
                "type": "Return temperature",
                "unit": "C",
                "value": 24.03999999999999914734871708787977695465087890625
            },
            {
                "type": "Temperature difference",
                "unit": "K",
                "value": 0.1700000000000000122124532708767219446599483489990234375
            },
            {
                "type": "On time",
                "unit": "seconds",
                "value": 8343980
            },
            {
                "type": "Operating time",
                "unit": "seconds",
                "value": 7556140
            },
            {
                "type": "Reserved",
                "unit": "none",
                "value": 4882
            }
        ]
    }
