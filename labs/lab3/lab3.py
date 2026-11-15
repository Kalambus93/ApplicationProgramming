import cv2
import matplotlib.pyplot as plt

import work_image as wi
import clprocessing as clp


def main() -> None:

    args = clp.processing_command()

    orig_im = args[0]
    result_im = args[1]

    current_image = wi.download_image(orig_im)
    wi.show_image(current_image)

    print(f"Размер изображения: {current_image.size}")

    current_image = wi.grayscale_image(current_image)
    wi.show_image(current_image)

    current_image = wi.gradient_image(current_image)
    wi.show_image(current_image)

    current_image = wi.circle_image(current_image)
    wi.show_image(current_image)

    cv2.imwrite(result_im, current_image)


if __name__ == "__main__":
    main()
