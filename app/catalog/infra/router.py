import logging

from fastapi import APIRouter

from app.catalog.domain.entities import Product, UpdatedProduct
from app.dependencies import product_adapter

logger = logging.getLogger(__name__)

router = APIRouter()


@router.post("/product", response_model=Product)
async def create_product(product: Product) -> Product:
    return product_adapter.create(product)


@router.get("/product/{sku}", response_model=Product)
async def get_product(sku: str) -> Product:
    return product_adapter.retrieve(sku=sku)


@router.put("/product/{sku}", response_model=Product)
async def update_product(sku: str, product: UpdatedProduct) -> Product:
    return product_adapter.update(sku=sku, product=product)


@router.delete("/product/{sku}")
async def delete_product(sku: str):
    product_adapter.delete(sku=sku)
    return {"ok": True}
