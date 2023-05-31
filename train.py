import torch

def train_model(trainloader, criterion, optimizer, net):
    for epoch in range(2):  # loop over the dataset multiple times

        running_loss = 0.0
        for i, data in enumerate(trainloader, 0):
            # get the inputs; data is a list of [inputs, labels]
            inputs, labels = data

            # zero the parameter gradients
            optimizer.zero_grad()

            # forward + backward + optimize
            outputs = net(inputs)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()

            # print statistics
            running_loss += loss.item()
            if i % 2000 == 1999:    # print every 2000 mini-batches
                print(f'[{epoch + 1}, {i + 1:5d}] loss: {running_loss / 2000:.3f}')
                running_loss = 0.0

    print('Finished Training')

    ########################################################################
    # Let's quickly save our trained model:

    PATH = './cifar_net.pth'
    torch.save(net.state_dict(), PATH)

    return PATH

if __name__ == '__main__':
    train_model(None, None, None, None)
    #Error should be "TypeError: 'NoneType' object is not iterable"