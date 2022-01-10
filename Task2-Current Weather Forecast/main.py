'''
To show current weather forecast for a city using python_weather module
'''
import python_weather
import asyncio

async def fetch_weather(city):
    '''
    To fetch weather forecast for a city
    '''
    client = python_weather.Client(format=python_weather.METRIC)
    city_forecast = await client.find(city)
    await client.close()
    return city_forecast.current

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    city = input("Enter city name: ")
    future = asyncio.ensure_future(fetch_weather(city))
    loop.run_until_complete(future)
    print(f'City : {city}\nDate: {future.result().date}\nTemperature: {future.result().temperature}°C\nSky: {future.result().sky_text}\nHumidity: {future.result().humidity}%\nWind: {future.result().wind_speed}km/h')