import logging

from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from app.catalog.infra.router import router as product_router
from app.user.infra.router import router as user_router

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(name)s  - %(message)s")

app = FastAPI()


app.include_router(product_router)
app.include_router(user_router)


@app.get("/")
async def root():
    return RedirectResponse("/docs")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=3000)
