import aiohttp

async def get_weather(city: str, api_key: str):
    url = f"https://devapi.qweather.com/v7/weather/now?location={city}&key={api_key}"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.json()
            return {
                "temp": data["now"]["temp"],
                "weather": data["now"]["text"],
                "wind": data["now"]["windScale"]
            }