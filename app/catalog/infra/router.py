from typing import Annotated, Optional

from fastapi import APIRouter, Depends, HTTPException, status

from app.catalog.domain.entities import Product, ProductCreate, ProductUpdate
from app.dependencies import product_port
from app.user.domain.entities import User
from app.user.infra.router import get_current_admin_user, get_current_user_optional

router = APIRouter()


@router.post("/product", response_model=Product)
async def create_product(
    product: ProductCreate,
    current_user: Annotated[User, Depends(get_current_admin_user)],
) -> Product:
    return product_port.create(product)


@router.get("/product/{sku}", response_model=Product)
async def get_product(
    sku: str, current_user: Optional[User] = Depends(get_current_user_optional)
) -> Product:
    product = product_port.retrieve(sku, current_user)
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product does not exist",
        )
    return product


@router.put("/product/{sku}", response_model=Product)
async def update_product(
    sku: str,
    product: ProductUpdate,
    current_user: Annotated[User, Depends(get_current_admin_user)],
) -> Product:
    return product_port.update(sku=sku, product=product)


@router.delete("/product/{sku}")
async def delete_product(
    sku: str, current_user: Annotated[User, Depends(get_current_admin_user)]
):
    product_port.delete(sku=sku)
    return {"ok": True}
