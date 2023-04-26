import torch


class NeuralNetwork(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.main = torch.nn.Sequential(
            torch.nn.Linear(in_features=28 * 28, out_features=512),
            torch.nn.ReLU(),
            torch.nn.Linear(512, 512),
            torch.nn.ReLU(),
            torch.nn.Linear(512, 10),
            torch.nn.Softmax(dim=1)
        )

    def forward(self, x):
        output = self.main(x)
        return output

