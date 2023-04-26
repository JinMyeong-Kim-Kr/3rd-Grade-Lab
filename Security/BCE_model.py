import torch
import torch.nn as nn
import numpy as np

from tqdm.notebook import tqdm
from torch.optim import Adam
from torch.utils.data import DataLoader, Dataset


device = 'cuda' if torch.cuda.is_available() else 'cpu'

class FlowDataset(Dataset):
    def __init__(self, data, label):
        self.data = data
        self.label = label
    
    def __len__(self):
        return len(self.label)
    
    def __getitem__(self, idx):
        return self.data[idx], self.label[idx]
    
class BinaryClassifier(nn.Module):
    def __init__(self, num_feature):
        super(BinaryClassifier, self).__init__()
        self.layer = nn.Sequential(
            nn.Linear(num_feature, 128),
            nn.ReLU(),
            nn.Linear(128, 128),
            nn.ReLU(),
            nn.Linear(128, 64),
            nn.ReLU(),
            nn.Linear(64, 32),
            nn.ReLU(),
            nn.Linear(32, 16),
            nn.ReLU(),
            nn.Linear(16, 8),
            nn.ReLU(),
            nn.Linear(8, 4),
            nn.ReLU(),
            nn.Linear(4, 1),
            nn.Sigmoid()
        )
    def forward(self, x):
        output = self.layer(x)
        return output

def train(train_X, train_y):
    torch.manual_seed(42)
    torch.cuda.manual_seed(42)
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = False
    np.random.seed(42)

    model = BinaryClassifier(len(train_X[0]))
    criterion = nn.BCELoss()
    optimizer = Adam(model.parameters(), lr = 1e-4)
    epoch = 32

    train_dataset = FlowDataset(train_X, train_y)
    train_dataloader = DataLoader(train_dataset, batch_size=512, shuffle=True)

    model.to(device)
    with tqdm(range(epoch)) as pbar:
        for _ in pbar:
            epoch_loss = 0
            data_count = 0
            for data, label in train_dataloader:
                data = data.to(device)
                label = label.to(device)
                output = model(data)
                loss = criterion(output.squeeze(1), label)
                optimizer.zero_grad()
                loss.backward()
                optimizer.step()
                epoch_loss += loss.item()
                data_count += len(data)
                pbar.set_postfix(epoch=epoch, loss=f"{epoch_loss / data_count}")
    return model

def test(test_X, test_y, model):
    test_dataset = FlowDataset(test_X, test_y)
    test_dataloader = DataLoader(test_dataset, batch_size= 512, shuffle=False)
    model.to(device)
    pred = []
    with torch.no_grad():
        for data, label in (test_dataloader):
            data = data.to(device)
            label = label.to(device)
            output = model(data)
            output = output.cpu().squeeze().tolist()
            pred.extend(output)
    return pred