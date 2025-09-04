import h5py
import numpy as np

class HDF5Dataset:
    def __init__(self, columns):
        self.columns = columns

    def write(self, rows, file_name, dataset_name='data'):
        dtype = [(col, 'f8') if col != 'flag' else (col, 'i4') for col in self.columns]
        arr = np.array([tuple(row) for row in rows], dtype=dtype)
        with h5py.File(file_name, 'w') as f:
            f.create_dataset(dataset_name, data=arr)

    def read(self, file_name, dataset_name='data'):
        with h5py.File(file_name, 'r') as f:
            data = f[dataset_name][:]
        return data
