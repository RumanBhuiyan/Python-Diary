import asyncio
import time

async def PrintSomething():
    print("Hello ")
    # asynchronous way of sleeping, await functionName/operation will do
    await asyncio.sleep(2)
    print("World")

asyncio.run(PrintSomething())
# synchronous way of sleeping
time.sleep(2)
print("How are you ?")
