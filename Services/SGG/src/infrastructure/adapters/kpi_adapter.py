import plotly.graph_objects as go
from domain.Entities.kpi_entity import GraphData

class GraphPlotlyAdapter:
    @staticmethod
    def create_line_chart(graph_data: GraphData, output_file: str):
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=graph_data.x, y=graph_data.y, mode='lines+markers', name='Data'))
        
        fig.update_layout(
            title=graph_data.title,
            xaxis_title=graph_data.x_label,
            yaxis_title=graph_data.y_label
        )
        
        fig.write_html(output_file)  # Exporta el gráfico a un archivo HTML
        print(f"Gráfico exportado a: {output_file}")
