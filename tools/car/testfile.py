import numpy as np
import matplotlib
import matplotlib.pyplot as plt

plt.axis([0, 10, 0, 1])
print('________________')
print('--->',matplotlib.get_backend())
print('________________')
def test():
    for i in range(25):
        y = np.random.random()
        plt.scatter(i, y)
        plt.pause(.15)
        print('GLEECE')
    plt.show()

test()


