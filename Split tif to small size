from PIL import Image
import cv2

def split_image(image_path, width, height, stride):
    """
    Splits a large image into smaller images of a specified size and stride.

    Args:
        image_path (str): The path to the original image.
        width (int): The width (in pixels) of each small image.
        height (int): The height (in pixels) of each small image.
        stride (int): The distance (in pixels) to slide the window for each small image.

    Returns:
        None. Saves the split images to disk.

    """

    # Open the original image
    img = Image.open(image_path)
    img_width, img_height = img.size

    # Split the image into smaller images
    images = []
    for y in range(0, img_height, stride):
        for x in range(0, img_width, stride):
            # Define the box for the small image
            box = (x, y, x+width, y+height)
            # Check if the box is outside the image boundaries and adjust it if necessary
            if box[2] > img_width:
                box = (img_width-width, y, img_width, y+height)
            if box[3] > img_height:
                box = (x, img_height-height, x+width, img_height)
            # Crop the small image from the original image and add it to the list of images
            images.append(img.crop(box))

    # Save the split images to disk
    for i, image in enumerate(images):
        image.save(f"image_{i}.tif")
