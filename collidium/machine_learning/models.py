from torch import nn

class ShallowNet(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(ShallowNet, self).__init__()
        self.net_sequence = nn.Sequential(
            nn.Linear(input_size, hidden_size),
            nn.ReLU(),
            nn.Linear(hidden_size, output_size)
        )

    def forward(self, x):
        return self.net_sequence(x)
