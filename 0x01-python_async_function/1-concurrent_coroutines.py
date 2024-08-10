#!/usr/bin/env python3
import asyncio
from previous_file import wait_n  # Replace 'previous_file' with the actual filename

async def main():
    delays = await wait_n(5, 10)
    print(delays)

if __name__ == "__main__":
    asyncio.run(main())

