import logging

from fastapi import APIRouter

from app.catalog.domain.entities import Product
from app.dependencies import product_adapter

logger = logging.getLogger(__name__)

router = APIRouter()


@router.post("/product", response_model=Product)
async def create_product(product: Product) -> Product:
    return product_adapter.create(product)


@router.put("/product")
async def update_product(payload: dict = None):
    pass
