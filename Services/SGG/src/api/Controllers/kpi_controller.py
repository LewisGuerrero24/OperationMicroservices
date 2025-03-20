from fastapi import APIRouter
from application.kpi_service import GraphService

router = APIRouter()

@router.get("/generate-graph")
def generate_graph():
    service = GraphService()
    service.generate_example_chart()
    return {"message": "Gráfico generado y guardado como 'output_chart.html'"}
