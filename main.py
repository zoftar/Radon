import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from scipy import misc
import imageio as imageio


def main():
    theta = 90  # kąt
    n = 10  # liczba detektorów
    l = 10  # rozpiętość układu emiter - detektor

    # image = Image.open("square.bmp") #potrzebujemy czegoś, co czyta bmp... poprawnie ;_;
    image = imageio.imread(os.path.join('square.bmp'))

    # Plot the original and the radon transformed image
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 4.5))
    ax1.set_title("Original")
    ax1.imshow(image, cmap=plt.cm.Greys_r)
    fig.tight_layout()
    plt.show()


if __name__ == '__main__':
    main()
