import h5py
import numpy as np

def read_hdf5_to_array(file_name, dataset_name='data'):
	with h5py.File(file_name, 'r') as f:
		data = f[dataset_name][:]
	return np.array(data)
