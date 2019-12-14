import h5py
import numpy as np

data = np.loadtxt('particle.in', skiprows=1)
print(data.shape)
hf = h5py.File('particle.h5', 'w')
hf.create_dataset('particles', data=data)
hf.close()

