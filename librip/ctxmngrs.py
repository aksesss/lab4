import contextlib
import time


@contextlib.contextmanager
def timer():
    t1 = time.time()
    yield
    t2 = time.time()
    print(t2-t1)
