#try: Used to keep the logic in which we ,ay get some error.
#except: will be executed ehen exception occurres in try block logic
#else: will be executed when try block logiv executed without any error.
#finally: will alwalys executed irrespective of exception occurred or not

def disp(a,b):
    try:
        print('Task Started')
        print(a/b) #ZeroDivisorError
    except:
        print('Some erro Handled')
    else:
        print('Task executed without any exception')
    finally:
        print('Task Ended')

disp(10,0)
disp(10,200)
disp(20,2)