import numpy as np
import matplotlib.pyplot as plt


filenames = ['avgRoundFive.txt', 'rmsRoundFive.txt']

def SampleAnalysis(filename):
	Sample = np.loadtxt(filename, delimiter = ',')
	SampleLeftChannel = Sample[:,0]
	SampleRightChannel = Sample[:, 1]
	SampleLatMix = Sample[:, 2]
	SampleVertMix = Sample[:, 3]
	maxval = np.max(Sample)		
	numsamps, nummixes = np.shape(Sample)
	'''
	plt.subplot(4, 3, i+1)
	plt.plot(SampleLeftChannel, color = 'r')
	plt.plot(SampleVertMix, color = 'g')
	plt.plot(SampleLatMix, color = 'b')		
	plt.plot(SampleRightChannel, color = 'c')
	plt.title(filename[:-4] + " Values	")
	'''
	return Sample, SampleLeftChannel, SampleRightChannel, SampleLatMix, SampleVertMix

Sample, SampleLeftChannel, SampleRightChannel, SampleLatMix, SampleVertMix = SampleAnalysis(filenames[0])

plt.figure()
'''
ax1 = plt.subplot(411)
ax1.plot(SampleVertMix)

ax2 = plt.subplot(412)

'''
SampleLatMix = SampleLatMix.reshape(10,3)
print(SampleLatMix)
domain =np.arange(0, 10, 1)



SampleLatMix[:,0] = SampleLatMix[:,1] + SampleLatMix[:,2] + SampleLatMix[:,0]
plt.scatter(domain, SampleLatMix[:,0])
'''
plt.scatter(domain, SampleLatMix[:,0], color = 'r')
plt.scatter(domain, SampleLatMix[:,1], color = 'b')
plt.scatter(domain, SampleLatMix[:,2], color = 'g')
ax3 = plt.subplot(413)

ax3.plot(SampleLeftChannel, color = 'b')
ax4 = plt.subplot(414)
ax4.plot(SampleRightChannel, color = 'r')
'''
plt.show()


