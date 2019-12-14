import h5py
import numpy as np

datavalues = np.random.uniform(size=(1000, 9))
datavalues[:, 8] = np.linspace(0, 1000, 1000)
hf = h5py.File('particle.h5', 'w')
hf.create_dataset('particles', data=datavalues)
hf.close()

