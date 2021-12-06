import asyncio
import aiohttp
import aiofiles
from aiostream import stream
from datetime import datetime
import time

BASE_URL = "http://roboforge.ru:8000/"
TEMP_URL = BASE_URL + "temp"
CO2_URL = BASE_URL + "co2"

async def req_json(url):
    async with aiohttp.ClientSession() as session:
        while True:
            async with session.get(url) as response:
                yield await response.json()

async def write_to_file(path):
    zip_stream = stream.combine.zip(req_json(TEMP_URL), req_json(CO2_URL))

    async with zip_stream.stream() as data:
        async with aiofiles.open(path, 'w') as file:
            await file.write("dt, tempreture, CO2\n")

            async for temp_js, co2_js in data:
                dt = datetime.utcnow()
                await file.write(f"{dt}, {temp_js['temperature']}, {co2_js['co2']}\n")
                await file.flush()

async def main():
    await write_to_file("./zmq/test.csv")

if __name__ == "__main__":
    asyncio.run(main())