'''
README: this script should do analysis on the files generated by azcalculations.py
'''

import numpy as np 
from matplotlib import pyplot as  plt 

def SampleAnalysis(filename):
	Sample = np.loadtxt('filename.txt', delimiter = ',')
	SampleLeftChannel = Sample[:,0]
	SampleRightChannel = Sample[:, 1]
	SampleLatMix = Sample[:, 2]
	SampleVertMix = Sample[:, 3]
	maxval = np.max(Sample)
	plt.plot(SampleLeftChannel, color = 'r')
	plt.plot(SampleVertMix, color = 'g')
	plt.plot(SampleLatMix, color = 'b')
	plt.plot(SampleRightChannel, color = 'c')
	plt.xlabel("Recording Number")
	plt.text(0, maxval*.8, "Red is left channel, Cyan is right")
	plt.text(0, maxval * .2, "Green is vert mix, blue is lateral")
	plt.show()