import asyncio
import httpx
import time
import sys
import time

def type_writer(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.01)


async def stream_with_ttft():
    url = "https://httpbin.org/stream/20"

    start = time.time()
    first_token_time = None

    async with httpx.AsyncClient(timeout=None) as client:
        async with client.stream("GET", url) as response:
            async for chunk in response.aiter_text():

                if first_token_time is None:
                    first_token_time = time.time()
                    print(f"\nTTFT: {first_token_time - start:.3f}s\n")

                type_writer(chunk)

# asyncio.run(stream_with_ttft())

# buffer 
buffer = ""

async for chunk in response.aiter_text():
    buffer += chunk

    while "\n" in buffer:
        line, buffer = buffer.split("\n", 1)
        print("Processed:", line)