#try: Used to keep the logic in which we, may get some error.
#except: will be executed when exception occurres in try block logic
#else: will be executed when try block logic executed without any error.
#finally: will alwalys executed irrespective of exception occurred or not

def disp(a,b):
    try:
        print('Task Started')
        print(a/b) #ZeroDivisorError
    except:
        print('Some error Handled')
    else:
        print('Task executed without any exception')
    finally:
        print('Task Ended')

disp(10,0)
disp(10,200)
disp(20,2)