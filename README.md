# WeatherApi

API REST para obtener datos meteorológicos en tiempo real por ciudad, utilizando la API de [Open Meteo](https://open-meteo.com/). También permite generar reportes en formatos Excel, CSV y PDF.

## Tecnologías Usadas

- **[FastAPI](https://fastapi.tiangolo.com/)**: Framework para construir APIs rápidas y modernas con Python.
- **[Uvicorn](https://www.uvicorn.org/)**: Servidor ASGI para ejecutar la aplicación FastAPI.
- **[Open-Meteo API](https://open-meteo.com/)**: API gratuita sin autenticación para obtener datos meteorológicos por coordenadas.
- **[Geopy](https://geopy.readthedocs.io/)**: Librería para geocodificación (conversión de nombres de ciudad a coordenadas geográficas).
- **[Pandas](https://pandas.pydata.org/)**: Herramienta poderosa para análisis, transformación y exportación de datos.
- **[XlsxWriter](https://xlsxwriter.readthedocs.io/)**: Librería para crear archivos Excel (.xlsx) con múltiples opciones de formato.
- **[Jinja2](https://jinja.palletsprojects.com/)**: Motor de plantillas para generar HTML dinámico usado en la generación de PDFs.
- **[xhtml2pdf](https://xhtml2pdf.readthedocs.io/)**: Herramienta que convierte HTML y CSS básicos a archivos PDF.
- **[python-dotenv](https://pypi.org/project/python-dotenv/)**: Carga variables de entorno desde archivos `.env` para mantener claves y configuraciones fuera del código fuente.

---

## Estructura de Carpetas

```
weather_api/
├── main.py                # Archivo principal de la aplicación FastAPI
├── .gitignore             # Lista de archivos y carpetas que Git debe ignorar
├── requirements.txt       # Lista de dependencias
├── .env.example           # Variables de entorno de ejemplo
├── utils/
│ ├── api_client.py        # Cliente HTTP para geocodificación y Open Meteo
│ └── report_generator.py  # Generación de archivos Excel, CSV y PDF
├── views/
│ └── pdf_template.html    # Plantilla HTML usada para generar el PDF
└── README.md              # Documentación del proyecto
```

## Configuración del Proyecto

### Variables de Entorno

El proyecto no necesita archivo `.env` para esta primera versión.

### Cómo Ejecutar el Proyecto

#### 1. **Ejecutar Localmente**

1. **Crear un entorno virtual**:

   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```

2. **Instalar dependencias**:

   ```bash
   pip install -r requirements.txt
   ```

3. **Ejecutar la aplicación**:

   ```bash
   python main.py
   ```

4. **Abrir la documentación interactiva**:
   - Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
   - Redoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## End points disponibles

| Método | Endpoint                | Descripción                                 |
| ------ | ----------------------- | ------------------------------------------- |
| GET    | `/weather/{city}`       | Datos meteorológicos actuales de una ciudad |
| GET    | `/weather/{city}/excel` | Reporte en formato Excel (.xlsx)            |
| GET    | `/weather/{city}/csv`   | Reporte en formato CSV                      |
| GET    | `/weather/{city}/pdf`   | Reporte en formato PDF                      |
