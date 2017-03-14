'''
README: this script should do analysis on the files generated by azcalculations.py
'''
	
import numpy as np 
from matplotlib import pyplot as  plt 

def SampleAnalysis(filename):
	Sample = np.loadtxt(filename, delimiter = ',')
	SampleLeftChannel = Sample[:,0]
	SampleRightChannel = Sample[:, 1]
	SampleLatMix = Sample[:, 2]
	SampleVertMix = Sample[:, 3]
	maxval = np.max(Sample)
	numsamps, nummixes = np.size(Sample)
	plt.plot(SampleLeftChannel, color = 'r')
	plt.plot(SampleVertMix, color = 'g')
	plt.plot(SampleLatMix, color = 'b')
	plt.plot(SampleRightChannel, color = 'c')
	plt.xlabel("Recording Number")
	plt.text(0, maxval*.8, "Red is left channel, Cyan is right")
	print(numsamps)
	plt.text(numsamps - 2, maxval*.8 , "Green is vert mix, blue is lateral")
	plt.show()
	return Sample, SampleLeftChannel, SampleRightChannel, SampleLatMix, SampleVertMix
