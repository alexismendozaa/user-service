from fastapi import FastAPI
from app.routes.select_routes import router as select_router

app = FastAPI()

# Incluir las rutas en la aplicación
app.include_router(select_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=4001)
