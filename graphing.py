import matplotlib.pyplot as plt
import numpy as np
import torchvision

########################################################################
# Let us show some of the training images, for fun.
# functions to show an image
def graph(trainloader, classes, batch_size):
    def imshow(img):
        img = img / 2 + 0.5  # unnormalize
        npimg = img.numpy()
        plt.imshow(np.transpose(npimg, (1, 2, 0)))
        plt.show()

    # get some random training images
    dataiter = iter(trainloader)
    images, labels = next(dataiter)

    # show images
    imshow(torchvision.utils.make_grid(images))
    # print labels
    print(' '.join(f'{classes[labels[j]]:5s}' for j in range(batch_size)))

if __name__ == '__main__':
    graph(None, None, None)
    #Error should be "TypeError: 'NoneType' object is not iterable"