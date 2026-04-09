import asyncio
import httpx
import json
import time
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from keys import OPENROUTER_API_KEY 
API_KEY = OPENROUTER_API_KEY
MODEL = "nvidia/nemotron-3-super-120b-a12b:free"
 
 
 # ---------------------------
# Typing Animation
# ---------------------------
def type_writer(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.005)


# ---------------------------
# Streaming LLM Response
# ---------------------------
async def stream_llm(messages):
    url = "https://openrouter.ai/api/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": MODEL,
        "messages": messages,
        "stream": True
    }

    start_time = time.time()
    first_token_time = None
    full_response = ""

    async with httpx.AsyncClient(timeout=None) as client:
        async with client.stream("POST", url, headers=headers, json=data) as response:

            buffer = ""

            async for chunk in response.aiter_text():
                print(f"Chunk: {chunk}")
                buffer += chunk

                # Process line-by-line (SSE format)
                while "\n" in buffer:
                    line, buffer = buffer.split("\n", 1)

                    if not line.startswith("data: "):
                        continue

                    data_line = line[6:].strip()

                    if data_line == "[DONE]":
                        print()
                        total_time = time.time() - start_time
                        print(f"\n⏱ Total Time: {total_time:.2f}s")
                        return full_response

                    try:
                        parsed = json.loads(data_line)
                        delta = parsed["choices"][0]["delta"]

                        content = delta.get("content", "")
                        if content:

                            # TTFT
                            if first_token_time is None:
                                first_token_time = time.time()
                                print(f"\n⚡ TTFT: {first_token_time - start_time:.2f}s\n")

                            type_writer(content)
                            full_response += content

                    except Exception as e:
                        print(f"Error parsing chunk: {chunk}")
                        print(f"Error: {e}")
                        continue


                        

def terminal_loading_animation():
    loading = ["◐", "◓", "◑", "◒"]
    index = 0
    while index < len(loading):
        sys.stdout.write(loading[index])
        sys.stdout.flush()
        time.sleep(0.1)
        sys.stdout.write("\b")
        index += 1
        if index == len(loading):
            index = 0

# ---------------------------
# Chat Loop with Memory
# ---------------------------
async def chat():
    print("🔥 Streaming Chat CLI (type 'exit' to quit)\n")

    messages = []

    while True:
        user_input = input("\n🧑 You: ")

        if user_input.lower() == "exit":
            break

        messages.append({"role": "user", "content": user_input})

        print("\n🤖 Bot: ", end="", flush=True)
        terminal_loading_animation()

        response = await stream_llm(messages)

        messages.append({"role": "assistant", "content": response})


# ---------------------------
# Run App
# ---------------------------
if __name__ == "__main__":
    asyncio.run(chat())