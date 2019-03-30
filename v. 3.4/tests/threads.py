from threading import Thread

def prescript(var):
    print(var)

thread1 = Thread(target=prescript, args='x')
thread2 = Thread(target=prescript, args='y')

thread1.start()
thread2.start()
thread1.join()
thread2.join()
