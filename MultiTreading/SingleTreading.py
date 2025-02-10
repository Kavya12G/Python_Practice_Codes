import threading
import time
print(threading.current_thread)
l1 = [1,2,3,4,5]
l2 = ['a','b','c','d','e']

def displayDigits(l1):
     for i in l1:
          print(i)
          time.sleep(1)

def displayLetters(l2):
     for i in l2:
          print(i)
          time.sleep(1)
displayDigits(l1)
displayDigits(l2)