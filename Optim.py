import torch.optim as optim
import torch.nn as nn


def optim_func(net):
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.SGD(net.parameters(), lr=0.001, momentum=0.9)
    return criterion, optimizer

if __name__ == '__main__':
    optim_func(None)
    #Error should be "AttributeError: 'NoneType' object has no attribute 'parameters'"