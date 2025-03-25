"""
Using the Python `queue` module and `threading.Event` to
improve our producer consumer queue.

Remember, debugging multithreaded code is very error-prone.
The presenter encountered an error that I avoided, but the
error presenting as a deadlock was unexpected (except that,
I believe, a thread was encountering an exception and
"eating it" resulting in an overall error with no message
indicating the problem).
"""
import concurrent.futures
import queue
import random
import threading
import time


FINISH = 'THE END'


class Pipeline(queue.Queue):
    def __init__(self):
        # `queue.Queue` handles locking "automagically"
        super().__init__(maxsize=10)

    def get_message(self):
        message = self.get()
        print(f'Consuming message: {message}')
        consumer_pipeline.append(message)
        return message

    def set_message(self, message):
        print(f'Producing message: {message}')
        producer_pipeline.append(message)
        self.put(message)


def producer(pipeline, is_finished):
    while not is_finished.is_set():
        message = random.randint(1, 100)
        pipeline.set_message(message)


def consumer(pipeline, is_finished):
    while not pipeline.empty() or not is_finished.is_set():
        print(f'Queue size is {pipeline.qsize()}')
        message = pipeline.get_message()
        time.sleep(random.random())


producer_pipeline = []
consumer_pipeline = []


if __name__ == '__main__':
    pipeline = Pipeline()
    # Use a `threading.Event()` to remove sentinel, `FINISH`
    is_finished = threading.Event()
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(producer, pipeline, is_finished)
        executor.submit(consumer, pipeline, is_finished)
        # Sleeping allows produce and consumer to start
        time.sleep(0.5)
        is_finished.set()
    print(f'Producer: {producer_pipeline}')
    print(f'Consumer: {consumer_pipeline}')
