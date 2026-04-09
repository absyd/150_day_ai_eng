

import asyncio
import httpx

async def chat():
    url = "https://httpbin.org/stream/10"

    user_input = input("You: ")

    print("Bot: ", end="", flush=True)

    async with httpx.AsyncClient(timeout=None) as client:
        async with client.stream("GET", url) as response:
            async for chunk in response.aiter_text():
                print(chunk, end="", flush=True)

asyncio.run(chat())