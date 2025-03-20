from fastapi import FastAPI
from api.Controllers.kpi_controller import router as kpi_router


app = FastAPI()

# Registrar las rutas
app.include_router(kpi_router, prefix="/api")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
