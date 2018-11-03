## Import necessary modules (Python 3)
import time, urllib.request, threading, _thread
#Take input for semaphore value, n
n = int(input("Enter number of simulaneous queries: "))
sa = threading.Semaphore(n)
#Take input of urls
x = input("Enter urls, separated by spaces: ")
#Turn string input into list of strings
urls = [url for url in x.split()]
#Create a Lock, mutex
mut = threading.Lock()

def getUrlInfo(x):
    ##set initial time
    newTime = time.time()
    ##open url
    resp = urllib.request.urlopen(x)
    ##limit the ammount of threads that can enter this part of code to n using semaphore
    sa.acquire()
    ##limit the number of threads that can print at a time to 1 using lock
    mut.acquire()
    print(resp.getcode())
    ##time.time() - initial time to get time taken
    print('It took ',time.time()-newTime,' seconds to get a reply from',x)
    mut.release()
    sa.release()
##Use for loop to create a new thread for each url
for y in urls:
    _thread.start_new_thread(getUrlInfo, (y,))
