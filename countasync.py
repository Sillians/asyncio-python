#!/usr/bin/env python3
# countasync.py

import asyncio

async def count():
    print("One")
    await asyncio.sleep(1)
    print("Two")
    
async def main():
    await asyncio.gather(count(), count(), count())
    
if __name__ == "__main__":
    import time
    s = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")
    






"""
    The order of this output is the heart of async IO. 
    Talking to each of the calls to count() is a single event loop, 
    or coordinator. When each task reaches await asyncio.sleep(1), 
    the function yells up to the event loop and gives 
    control back to it, saying, “I’m going to be sleeping for 1 second. 
    Go ahead and let something else meaningful be done in the meantime.”

"""