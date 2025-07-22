# Proyecto_7
# Visualización interactiva de la composición bacteriana

Esta aplicación web permite explorar de forma interactiva la composición relativa de géneros bacterianos presentes en diferentes tipos de muestras (como heces, agua y organismos acuáticos). Fue desarrollada como parte del análisis exploratorio de datos (EDA) en un estudio de microbiota.

Este proyecto fue realizado en el contexto de una investigación doctoral en Ciencias Biológicas y de la Salud, desarrollada por **José Mijail Campos Compeán**.

## Contacto

📫 Puedes encontrarme en [LinkedIn](https://www.linkedin.com/in/jos%C3%A9-mijail-campos-compean-30ba98121/) para más información o colaboración en proyectos relacionados.


## Funcionalidad principal

La app proporciona dos tipos de visualización, accesibles mediante casillas de verificación:

- **Gráfico de barras 100% apiladas**: muestra la abundancia relativa de los 20 géneros más abundantes en cada muestra, con un diseño intuitivo que facilita la comparación visual entre condiciones.
- **Gráfico de dispersión por género**: permite seleccionar un género bacteriano y observar su distribución relativa a lo largo de las diferentes muestras.

Ambas gráficas son interactivas, están construidas con Plotly y son desplegadas usando Streamlit.

## Cómo usarla

1. Ejecuta `streamlit run app.py`.
2. Marca una o ambas casillas para generar las visualizaciones.
3. Interactúa con las gráficas para explorar las abundancias relativas.

---

Esta aplicación es útil para investigadores en microbiología, bioinformática o áreas afines que busquen visualizar rápidamente los resultados de un análisis de comunidades microbianas a nivel de género.
