"""
Implements a protected pipeline between a producer and a consumer.

This implementation has a problem. It correctly produces 10 messages,
but it consumes **fewer than 10 messages** before terminating. We'll fix
this problem in the next video.
"""
import concurrent.futures
import random
import threading
import time


FINISH = 'THE END'


class Pipeline:
    def __init__(self, capacity):
        self.capacity = capacity
        self.message = None
        self.producer_lock = threading.Lock()
        # This implementation has a problem. The consumer can
        # **immediately** acquire its lock even if the producer
        # has produced **no data**. The result: deadlock.
        self.consumer_lock = threading.Lock()

    def get_message(self):
        print(f'Consuming message of {self.message=}')
        self.consumer_lock.acquire()
        message = self.message
        # Since I've consumed a message, allow the producer
        # to add another message
        self.producer_lock.release()
        producer_pipeline.append(message)
        return message

    def set_message(self, message):
        print(f'Producing message of {self.message=}')
        producer_pipeline.append(message)
        self.producer_lock.acquire()
        self.message = message
        # Since I've produced a message, allow the consumer
        # to get another message
        self.consumer_lock.release()


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
