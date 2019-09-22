
import timeit
import random
import matplotlib.pyplot as plt

# Devise an experiment to verify that get item and update item are for dictionaries.
# a graph displaying the timings of those operators
storeIndex = []
storeTime = []
for i in range(10000,1000001,20000):
    t = timeit.Timer("random.randrange(%d) in x"%i,
                     "from __main__ import random,x")
    randomNum = random.randrange(1,101)
    x = {j:randomNum for j in range(i)}
    x.get(range(i))
    get_time = t.timeit(number=100) # runs it 100 times and gets the average
    x.update(y = 3, z =4)
    update_time = t.timeit(number=100)
    storeIndex.append(i)
    average = (get_time + update_time)/2
    storeTime.append(average)
    print("%d,%10.3f,%10.3f" % (i, get_time, update_time))

# indentation for a scatter plot graph
plt.scatter(storeIndex, storeTime, marker='*', c='c', s=4)
plt.xlabel('Size')
plt.ylabel('Time')
plt.ylim(0.000)
plt.title('An Experiment to Verify that Get item and Update item (in dictionaries) are O(1)')
plt.show()


