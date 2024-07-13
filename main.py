import logging

from fastapi import FastAPI
from fastapi.responses import RedirectResponse

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(name)s  - %(message)s")

app = FastAPI()


# app.include_router(webhooks_router)


@app.get("/")
async def root():
    return RedirectResponse("/docs")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=3000)
