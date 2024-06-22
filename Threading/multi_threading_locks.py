'''
https://www.turing.com/kb/python-multiprocessing-vs-multithreading
Theory
When using threads, we  often need to ensure that only one thread accesses a
particular section of code or a shared resource at a time to avoid
conflicts and ensure data integrity. This is where locks (or mutexes) come
into play.

Locks:
Concept: A lock is a synchronization primitive that prevents multiple threads
from accessing shared resources simultaneously.
Use Case: Useful when you have critical sections of code that modify shared
resources and need to prevent race conditions.
Behavior: When a thread acquires a lock, other threads attempting to acquire
the same lock will block until the lock is released.

'''


import threading
import time

# Shared resource
shared_counter = 0

# Create a lock
lock = threading.Lock()

def increment_counter():
    global shared_counter
    for _ in range(100000):
        # Acquire the lock before accessing the shared resource
        lock.acquire()
        shared_counter += 1
        # Release the lock after accessing the shared resource
        lock.release()

def decrement_counter():
    global shared_counter
    for _ in range(100000):
        # Acquire the lock before accessing the shared resource
        lock.acquire()
        shared_counter -= 1
        # Release the lock after accessing the shared resource
        lock.release()

# Create threads
thread1 = threading.Thread(target=increment_counter)
thread2 = threading.Thread(target=decrement_counter)

# Start threads
thread1.start()
thread2.start()

# Wait for both threads to complete
thread1.join()
thread2.join()

print(f"Final value of shared_counter: {shared_counter}")
