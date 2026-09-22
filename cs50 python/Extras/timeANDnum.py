if False:
    import time
    seconds_since_epoch = time.time()
    # In Python’s time module, the epoch is the starting point from which the module measures time. 
    # Defined as January 1, 1970, 00:00:00 UTC.
    start = time.time()

    a = [i for i in range(100000000)]
    b = [i for i in range(100000000, 200000000)]
    c = []

    for i in range(len(a)):
        c.append(a[i]+b[i])

    print(seconds_since_epoch)
    # print result @7/22/26 == 1784670302.5966673
    print(time.time() - start)
    # print result @7/22/26 == 28.8366596698761

# let's try out numpy
import time
import numpy as np

start = time.time()

a = np.arange(100000000)
b = np.arange(100000000, 200000000)
c = a + b

print(time.time() - start)
# print result @7/22/26 == 28.8366596698761