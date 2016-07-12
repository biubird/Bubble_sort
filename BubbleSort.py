import random
import datetime
import time

startTime = time.time()

randomList = random.sample(xrange(10000), 100)

randomList.sort()
elapsedTime = time.time() - startTime
print randomList
print elapsedTime
