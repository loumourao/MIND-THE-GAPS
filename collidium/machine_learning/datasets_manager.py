import torch
import pandas as pd

from torch.utils.data import Dataset

class ProximityQueriesDataset(Dataset):
    def __init__(self, annotations_file):
        self.df = pd.read_csv(annotations_file)

    def __len__(self):
        return len(self.df)

    def __getitem__(self, idx):
        X = torch.tensor(self.df.iloc[idx, :-1].tolist(), 
                         dtype=torch.float32)
        y = torch.tensor([self.df.iloc[idx, -1]],
                         dtype=torch.float32)
        return X, y
