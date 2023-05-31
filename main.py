# This is a sample Python script.
import torch
from create_data import make_datasets
from graphing import graph
from CNN import Net
from Optim import optim_func
from train import train_model


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    batch_size, trainloader, testloader, classes = make_datasets()
    graph(trainloader, classes, batch_size)
    net = Net()
    criterion, optimizer = optim_func(net)
    PATH = train_model(trainloader, criterion, optimizer, net)

    net = Net()
    net.load_state_dict(torch.load(PATH))

    dataiter = iter(testloader)
    images, labels = next(dataiter)

    outputs = net(images)

    _, predicted = torch.max(outputs, 1)

    print('Predicted: ', ' '.join(f'{classes[predicted[j]]:5s}'
                                  for j in range(4)))


    correct = 0
    total = 0

    with torch.no_grad():
        for data in testloader:
            images, labels = data
            # calculate outputs by running images through the network
            outputs = net(images)
            # the class with the highest energy is what we choose as prediction
            _, predicted = torch.max(outputs.data, 1)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()

    print(f'Accuracy of the network on the 10000 test images: {100 * correct // total} %')


    # prepare to count predictions for each class
    correct_pred = {classname: 0 for classname in classes}
    total_pred = {classname: 0 for classname in classes}

    # again no gradients needed
    with torch.no_grad():
        for data in testloader:
            images, labels = data
            outputs = net(images)
            _, predictions = torch.max(outputs, 1)
            # collect the correct predictions for each class
            for label, prediction in zip(labels, predictions):
                if label == prediction:
                    correct_pred[classes[label]] += 1
                total_pred[classes[label]] += 1

    # print accuracy for each class
    for classname, correct_count in correct_pred.items():
        accuracy = 100 * float(correct_count) / total_pred[classname]
        print(f'Accuracy for class: {classname:5s} is {accuracy:.1f} %')
