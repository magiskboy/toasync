from unittest import TestCase
import asyncio
from typing import Coroutine
from time import sleep, time
from toasync import async_


@async_
def func(i):
    sleep(i)


class time_couter:
    def __enter__(self):
        self.start_time = time()

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.duration = time() - self.start_time


class TestToAsync(TestCase):
    def setUp(self):
        self.counter = time_couter()

    def test_async_function(self):
        coroutines = [
            func()(1),
            func()(1),
            func()(1),
        ]
        for c in coroutines:
            self.assertIsInstance(c, Coroutine)

        coroutine = asyncio.gather(*coroutines)
        loop = asyncio.get_event_loop()

        with self.counter:
            loop.run_until_complete(coroutine)
        self.assertLess(self.counter.duration - 1, 0.1)

    def test_sync_function(self):
        with self.counter:
            func().delay(1)
            func().delay(1)
            func().delay(1)
        self.assertGreater(self.counter.duration, 3)
