import threading
import time
def sample1():
    for ele in range(1,5):
        print(ele)
        time.sleep(2)
def sample2():
    for ele in range(10,15):
        print(ele)
t1= threading.Thread(target = sample1)
t2= threading.Thread(target = sample2)
print(t1)
print(t2)
t1.start()
t2.start()

output: <Thread(Thread-1 (sample1), initial)>
        <Thread(Thread-2 (sample2), initial)>
        1
        10
        11
        12
        13
        14
        2
        3
        4
