import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from scipy import misc


def main():
    theta = 90  # kąt
    n = 10  # liczba detektorów
    l = 10  # rozpiętość układu emiter - detektor

    # image = Image.open("square.bmp") #potrzebujemy czegoś, co czyta bmp... poprawnie ;_;
    image = Image.open("square.png")

    # Plot the original and the radon transformed image
    plt.subplot(1, 2, 1), plt.imshow(image, cmap='gray')
    plt.xticks([]), plt.yticks([])
    plt.show()


if __name__ == '__main__':
    main()
