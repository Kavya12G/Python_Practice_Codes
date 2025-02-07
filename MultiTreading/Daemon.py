import threading
import time

def background_task():
    print(threading.current_thread())
    while True:
        print("Background task running...")
        time.sleep(2000)

thread =  threading.Thread(target = background_task, name = 'daemon')
thread.daemon = True
thread.start()

time.sleep(1)
print("Main program ends.")