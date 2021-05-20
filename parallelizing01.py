### https://github.com/CoreyMSchafer/code_snippets/blob/master/Python/MultiProcessing/multiprocessing-demo.py
import concurrent.futures
import multiprocessing
import time
"""
CPU bound vs IO bound
Network operations are IO bound frequently

"""
start = time.perf_counter()
def do_something():
    print('Sleeping 1 second(s)...')
    time.sleep(1)
    print('Done Sleeping...1')


# do_something(1)
# do_something(1)
p1 = multiprocessing.Process(target=do_something())
p2 = multiprocessing.Process(target=do_something())
p1.start()
p2.start()
p1.join()
p2.join()

finish = time.perf_counter()
print(f'Finished in {round(finish-start, 2)} second(s)')
