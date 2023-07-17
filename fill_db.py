import asyncio
import json

import aiohttp

URL = "http://127.0.0.1/create_rate"  # docker
HEADERS = {'content-type': 'application/json'}
payload = []


def prepare_payload():
    """Подготовка payload для отправки в теле запроса"""
    with open("data_rates.json", "r") as f:
        data = json.loads(f.read())
        for date, values in data.items():
            for value in values:
                payload.append(
                    {
                        "cargo_type": value["cargo_type"],
                        "rate": value["rate"],
                        "date": date,
                    },
                )


async def task(rate_obj):
    """Функция создания задачи"""
    async with aiohttp.ClientSession() as session:
        await session.post(
            url=URL,
            data=json.dumps(rate_obj),
            headers=HEADERS,
        )


async def async_execute():
    """Асинхронный генератор задач"""
    tasks = [asyncio.ensure_future(task(rate_obj)) for rate_obj in payload]
    await asyncio.wait(tasks)
    print("Данные загружены в БД")


if __name__ == "__main__":
    prepare_payload()
    asyncio.run(async_execute())
