import asyncio
import httpx

async def stream_basic():
    url = "https://httpbin.org/stream/20"

    async with httpx.AsyncClient(timeout=None) as client:
        async with client.stream("GET", url) as response:
            async for chunk in response.aiter_text():
                print(chunk, end="", flush=True)
                print("\n\n")

asyncio.run(stream_basic())