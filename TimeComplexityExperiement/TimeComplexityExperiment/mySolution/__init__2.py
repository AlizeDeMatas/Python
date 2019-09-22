
import timeit
import matplotlib.pyplot as plt
import random

# Devise an experiment that compares the
# performance of the del operator on lists and dictionaries.
lstDel = []
dictDel = []
for i in range(10000,1000001,20000):
    t = timeit.Timer("random.randrange(%d) in x"%i,
                     "from __main__ import random,x")
    x = list(range(i))
    del x[8]
    lstDel_time = t.timeit(number=100)
    lstDel.append(lstDel_time)
    x = {j:None for j in range(i)}
    del x[8]
    dictDel_time = t.timeit(number=100)
    dictDel.append(dictDel_time)
    print("%d,%10.3f,%10.3f" % (i, lstDel_time, dictDel_time))


plt.plot(lstDel, 'c', marker='*', label = "List Del Operator")
plt.plot(dictDel, 'm', marker='*', label = "Dictionary Del Operator")
plt.legend()
plt.xlabel('Size')
plt.ylabel('Time')
plt.title('An Experiment to Compare the Del operator in Lists to the Del Operator in Dictionaries')
plt.show()
