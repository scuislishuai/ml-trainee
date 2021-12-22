# -*- coding:utf-8 -*-


# Imports
import torch.nn as nn  # All neural network modules, nn.Linear, nn.Conv2d, BatchNorm, Loss functions
import torch.nn.functional as F  # All functions that don't have any parameters


class CNN(nn.Module):
    def __init__(self, in_channels, num_classes):
        super(CNN, self).__init__()
        self.conv1 = nn.Conv2d(
            in_channels=in_channels,
            out_channels=6,
            kernel_size=(3, 3),
            padding=(1, 1),
            stride=(1, 1)
        )
        self.pool = nn.MaxPool2d(kernel_size=(2, 2), stride=(2, 2))
        self.conv2 = nn.Conv2d(
            in_channels=in_channels,
            out_channels=16,
            kernel_size=(3, 3),
            padding=(1, 1),
            stride=(1, 1)
        )
        self.fc1 = nn.Linear(in_features=16 * 7 * 7, out_features=num_classes)
        self.initialize_weights()

    def forward(self, x):
        x = F.relu(self.fc1(x))
        x = self.pool(x)
        x = F.relu(self.fc2(x))
        x = self.pool(x)
        x = x.reshape(x.shape[0], -1)
        x = self.fc1(x)
        return x

    def initialize_weights(self):
        for m in self.modules():
            if isinstance(m, nn.Conv2d):
                nn.init.kaiming_normal_(tensor=m.weight)

                if m.bias is not None:
                    nn.init.constant_(tensor=m.bias, val=0)
            elif isinstance(m, nn.BatchNorm2d):
                nn.init.constant_(tensor=m.weights, val=1)
                nn.init.constant_(tensor=m.bias, val=0)
            elif isinstance(m, nn.Linear):
                nn.init.kaiming_normal_(tensor=m.weight)
                nn.init.constant_(tensor=m.bias, val=0)


if __name__ == "__main__":
    model = CNN(in_channels=3, num_classes=10)
    for param in model.parameters():
        print(param)