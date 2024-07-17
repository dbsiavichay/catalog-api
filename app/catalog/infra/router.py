from typing import Annotated, Optional

from fastapi import APIRouter, Depends

from app.catalog.domain.entities import Product, UpdatedProduct
from app.dependencies import product_port
from app.user.domain.entities import User
from app.user.infra.router import get_current_user, get_current_user_optional

router = APIRouter()


@router.post("/product", response_model=Product)
async def create_product(
    product: Product, current_user: Annotated[User, Depends(get_current_user)]
) -> Product:
    return product_port.create(product)


@router.get("/product/{sku}", response_model=Product)
async def get_product(
    sku: str, current_user: Optional[User] = Depends(get_current_user_optional)
) -> Product:
    breakpoint()
    return product_port.retrieve(sku=sku)


@router.put("/product/{sku}", response_model=Product)
async def update_product(
    sku: str,
    product: UpdatedProduct,
    current_user: Annotated[User, Depends(get_current_user)],
) -> Product:
    return product_port.update(sku=sku, product=product)


@router.delete("/product/{sku}")
async def delete_product(
    sku: str, current_user: Annotated[User, Depends(get_current_user)]
):
    product_port.delete(sku=sku)
    return {"ok": True}
