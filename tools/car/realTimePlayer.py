
import setup_path
import airsim

import time
import os
import numpy as np
import matplotlib.pyplot as plt


# connect to the AirSim simulator
client = airsim.CarClient()
client.confirmConnection()


# get image from Aisim
minutes = 3
endTime = time.time() + minutes*60


# run until time has elapse
raw = client.simGetImages([airsim.ImageRequest("1", airsim.ImageType.Scene, False, False)])
img1d = np.fromstring(raw[0].image_data_uint8, dtype=np.uint8) #get numpy array
print(img1d.shape)
img_rgba = img1d.reshape(raw[0].height, raw[0].width, 4) #reshape array to 4 channel image array H X W X 4


img = plt.imshow(img_rgba)
plt.pause(.01)
plt.draw()

while time.time() < endTime:
	raw = client.simGetImages([airsim.ImageRequest("1", airsim.ImageType.Scene, False, False)])
	img1d = np.fromstring(raw[0].image_data_uint8, dtype=np.uint8) #get numpy array
	print(img1d.shape)
	img_rgba = img1d.reshape(raw[0].height, raw[0].width, 4) #reshape array to 4 channel image array H X W X 4


	img.set_data(img_rgba)
	plt.pause(.01)
	plt.draw()

