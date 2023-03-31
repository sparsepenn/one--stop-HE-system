from PIL import Image

def extract_subimage(image_path, x, y, width, height):
    """
    Extracts a sub-image from a larger image and saves it to disk.

    Args:
        image_path (str): The path to the original image.
        x (int): The x-coordinate of the top-left corner of the sub-image.
        y (int): The y-coordinate of the top-left corner of the sub-image.
        width (int): The width of the sub-image.
        height (int): The height of the sub-image.

    Returns:
        None. Saves the extracted sub-image to disk.

    """

    # Open the original image
    img = Image.open(image_path)

    # Define the box for the sub-image
    box = (x, y, x + width, y + height)

    # Check if the box is outside the image boundaries and adjust it if necessary
    img_width, img_height = img.size
    if box[0] < 0:
        box = (0, box[1], box[2] - box[0], box[3])
    if box[1] < 0:
        box = (box[0], 0, box[2], box[3] - box[1])
    if box[2] > img_width:
        box = (box[0], box[1], img_width, box[3])
    if box[3] > img_height:
        box = (box[0], box[1], box[2], img_height)

    # Crop the sub-image from the original image
    sub_image = img.crop(box)

    # Save the sub-image to disk
    sub_image.save("sub_image.tif")
