from infrastructure.adapters.kpi_adapter import GraphPlotlyAdapter
from domain.Entities.kpi_entity import GraphData

class GraphService:
    def generate_example_chart(self):
        # Datos de ejemplo (pueden venir de una base de datos)
        x_data = [1, 2, 3, 4, 5]
        y_data = [10, 15, 13, 17, 22]
        
        # Crea una instancia de GraphData
        graph_data = GraphData(
            x=x_data,
            y=y_data,
            title="Ejemplo de Gráfico con Plotly",
            x_label="Eje X",
            y_label="Eje Y"
        )
        
        # Genera el gráfico usando el adaptador
        GraphPlotlyAdapter.create_line_chart(graph_data, "output_chart.html")
