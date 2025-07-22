import pandas as pd
import plotly.graph_objects as go
import streamlit as st

st.header("Visualización de la composición relativa de géneros bacterianos")

# Cargar el archivo CSV
df_top20_genus = pd.read_csv(
    'C:/Users/Mijail/Documents/Python/TripleTen/Sprint 7/Proyecto_7/df_top20_genus.csv',
    index_col=0
)

# Casilla para gráfico de barras 100% apiladas
show_bar_chart = st.checkbox('Mostrar gráfico 100% apilado por muestra')

if show_bar_chart:
    st.write("Composición relativa de los 20 géneros más abundantes por muestra")

    fig = go.Figure()

    for genus in df_top20_genus.columns:
        label = genus if genus == "Otros" else f"<i>{genus}</i>"
        fig.add_trace(go.Bar(
            name=label,
            x=df_top20_genus.index.astype(str),
            y=df_top20_genus[genus]
        ))

    fig.update_layout(
        barmode='stack',
        title='Composición relativa de géneros por muestra',
        xaxis_title='Muestra',
        yaxis_title='Abundancia relativa (%)',
        xaxis_tickangle=-45,
        legend_title='Género',
        height=600
    )

    st.plotly_chart(fig, use_container_width=True)

# Casilla para gráfico de dispersión por género
show_scatter = st.checkbox('Mostrar gráfico de dispersión por género')

if show_scatter:
    st.write("Visualización individual de la abundancia relativa por género")

    selected_genus = st.selectbox(
        "Selecciona un género", df_top20_genus.columns)

    fig2 = go.Figure()
    fig2.add_trace(go.Scatter(
        x=df_top20_genus.index.astype(str),
        y=df_top20_genus[selected_genus],
        mode='markers+lines',
        marker=dict(size=10),
        name=selected_genus
    ))

    fig2.update_layout(
        title=f'Abundancia relativa de <i>{selected_genus}</i> por muestra',
        xaxis_title='Muestra',
        yaxis_title='Abundancia relativa (%)',
        xaxis_tickangle=-45,
        height=500
    )

    st.plotly_chart(fig2, use_container_width=True)
