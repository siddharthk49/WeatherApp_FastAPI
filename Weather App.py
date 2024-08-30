from fastapi import FastAPI
import requests

app = FastAPI()
api_key = ""


@app.get("/")
async def root():
    return {"message": "Welcome to the Weather API!"}


@app.get("/weather/{city}")
async def get_weather(city: str):
    api_key = "YOUR_OPENWEATHERMAP_API_KEY"
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

    try:
        response = requests.get(base_url)
        response.raise_for_status()  # Raise an exception for bad status codes
        weather_data = response.json()
        return {
            "city": city,
            "temperature": weather_data["main"]["temp"],
            "description": weather_data["weather"][0]["description"]
        }
    except requests.RequestException as e:
        return {"error": str(e)}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
