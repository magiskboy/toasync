# -*- coding:utf-8 -*-
import asyncio
import time


def async_(func):
    class Async:
        def __init__(self, func):
            self.func = func

        def delay(self, *args, **kwargs):
            return self.func(*args, **kwargs)

        async def __call__(self, *args, **kwargs):
            loop = asyncio.get_event_loop()
            f = loop.run_in_executor(None, lambda: self.func(*args, **kwargs))
            return await asyncio.wait_for(f, timeout=None)

    def decorator(*args, **kwargs):
        return Async(func)

    return decorator
