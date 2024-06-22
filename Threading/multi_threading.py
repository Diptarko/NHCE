'''Threading:

Concept: Threading involves running multiple threads (smaller units of a process
) within the same process. Threads share the same memory space.
Use Case: Useful for I/O-bound tasks (like web scraping, network operations)
where the program spends a lot of time waiting for external resources.
Drawback: In Python, due to the Global Interpreter Lock (GIL), true parallel
execution of threads is limited. Only one thread executes Python bytecode at a
time.
'''

import threading

def cuber(n):
    print(f'Cube {n**3}\n')
    print(f'Thread name is {threading.current_thread().name}')

def squarer(n):
    print(f'\nSquare {n**2}')
    print(f'Thread name is {threading.current_thread().name}')

if __name__=='__main__':
    #Create threads
    t1 = threading.Thread(target= cuber, args=(5,))
    t2 = threading.Thread(target = squarer, args=(5,))
    #Start the threads
    t1.start()
    t2.start()
    print(f'Main thread is {threading.main_thread()}')
    #wait untill the first thread is over
    t1.join()
    #wait until second thread is over
    #both threads done
    print('Done')
