"""
Implements a protected pipeline between a producer and a consumer.

This implementation has a problem. It correctly produces 10 messages,
but it consumes **fewer than 10 messages** before terminating. We'll fix
this problem in the next video.
"""
import concurrent.futures
import random
import time


FINISH = 'THE END'


class Pipeline:
    def __init__(self, capacity):
        self.capacity = capacity
        self.message = None

    def get_message(self):
        print(f'Consuming message of {self.message=}')
        message = self.message
        consumer_pipeline.append(message)
        return message

    def set_message(self, message):
        print(f'Producing message of {self.message=}')
        producer_pipeline.append(message)
        self.message = message


def producer(pipeline):
    for _ in range(pipeline.capacity):
        message = random.randint(1, 100)
        pipeline.set_message(message)
    pipeline.set_message(FINISH)


def consumer(pipeline):
    message = None
    while message is not FINISH:
       message = pipeline.get_message()
       if message is not FINISH:
           time.sleep(random.random())


producer_pipeline = []
consumer_pipeline = []


if __name__ == '__main__':
    pipeline = Pipeline(10)
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(producer, pipeline)
        executor.submit(consumer, pipeline)
    print(f'Producer: {producer_pipeline}')
    print(f'Consumer: {consumer_pipeline}')
