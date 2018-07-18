import os
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np


files = os.listdir('./')
fig   = plt.figure()


for file in files:
	if file.find('png') != -1:
		im   = Image.open(file)
		file = str(file[:file.find('.')])+'.jpg'
		print(file)
		im = im.convert("RGBA")

		im.save(file)

		#plt.imshow(im)
		#plt.pause(0.05)
		#plt.show()




'''
plt.axis([0, 10, 0, 1])

for i in range(10):
    y = np.random.random()
    plt.scatter(i, y)
    plt.pause(0.05)

plt.show()
'''

'''
img = None
for f in files:
	if f.find('png') != -1:
		im=plt.imread(f)
		if img is None:
		    img = plt.imshow(im)
		else:
		    img.set_data(im)
		plt.pause(.1)
		plt.draw()
'''
