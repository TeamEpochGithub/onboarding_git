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

    ########################################################################
    # See `here <https://pytorch.org/docs/stable/notes/serialization.html>`_
    # for more details on saving PyTorch models.
    #
    # 5. Test the network on the test data
    # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    #
    # We have trained the network for 2 passes over the training dataset.
    # But we need to check if the network has learnt anything at all.
    #
    # We will check this by predicting the class label that the neural network
    # outputs, and checking it against the ground-truth. If the prediction is
    # correct, we add the sample to the list of correct predictions.

    ########################################################################
    # Next, let's load back in our saved model (note: saving and re-loading the model
    # wasn't necessary here, we only did it to illustrate how to do so):

    net = Net()
    net.load_state_dict(torch.load(PATH))

    ########################################################################
    # Okay, now let us see what the neural network thinks these examples above are:
    dataiter = iter(testloader)
    images, labels = next(dataiter)

    outputs = net(images)

    ########################################################################
    # The outputs are energies for the 10 classes.
    # The higher the energy for a class, the more the network
    # thinks that the image is of the particular class.
    # So, let's get the index of the highest energy:
    _, predicted = torch.max(outputs, 1)

    print('Predicted: ', ' '.join(f'{classes[predicted[j]]:5s}'
                                  for j in range(4)))

    ########################################################################
    # The results seem pretty good.
    #
    # Let us look at how the network performs on the whole dataset.

    correct = 0
    total = 0
    # since we're not training, we don't need to calculate the gradients for our outputs
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

    ########################################################################
    # That looks way better than chance, which is 10% accuracy (randomly picking
    # a class out of 10 classes).
    # Seems like the network learnt something.
    #
    # Hmmm, what are the classes that performed well, and the classes that did
    # not perform well:

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
