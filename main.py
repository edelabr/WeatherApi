from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from utils.api_client import get_weather_data, get_coordinates
from utils.report_generator import generate_excel, generate_csv, generate_pdf
import os

app = FastAPI(title="Weather API", description="Consulta meteorológica y generación de reportes", version="1.0")

@app.get("/")
def root():
    return {"message": "Welcome to WeatherApi"}

@app.get("/weather/{city}")
def get_weather(city: str):
    coords = get_coordinates(city)
    if not coords:
        raise HTTPException(status_code=404, detail="Ciudad no encontrada")

    data = get_weather_data(coords['lat'], coords['lon'])
    if not data:
        raise HTTPException(status_code=500, detail="Error al obtener datos meteorológicos")

    return {
        "city": city,
        "latitude": coords['lat'],
        "longitude": coords['lon'],
        "forecast": data
    }

@app.get("/weather/{city}/excel")
def get_excel(city: str):
    coords = get_coordinates(city)
    if not coords:
        raise HTTPException(status_code=404, detail="Ciudad no encontrada")

    data = get_weather_data(coords['lat'], coords['lon'])
    if not data:
        raise HTTPException(status_code=500, detail="Error al obtener datos meteorológicos")
    
    filepath = generate_excel(city, data)

    return FileResponse(filepath, media_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet', filename=os.path.basename(filepath))

@app.get("/weather/{city}/csv")
def get_csv(city: str):
    coords = get_coordinates(city)
    if not coords:
        raise HTTPException(status_code=404, detail="Ciudad no encontrada")

    data = get_weather_data(coords['lat'], coords['lon'])
    if not data:
        raise HTTPException(status_code=500, detail="Error al obtener datos meteorológicos")
    
    filepath = generate_csv(city, data)
    return FileResponse(filepath, media_type='text/csv', filename=os.path.basename(filepath))

@app.get("/weather/{city}/pdf")
def get_pdf(city: str):
    coords = get_coordinates(city)
    if not coords:
        raise HTTPException(status_code=404, detail="Ciudad no encontrada")

    data = get_weather_data(coords['lat'], coords['lon'])
    if not data:
        raise HTTPException(status_code=500, detail="Error al obtener datos meteorológicos")
    
    filepath = generate_pdf(city, data)
    return FileResponse(filepath, media_type='application/pdf', filename=os.path.basename(filepath))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
