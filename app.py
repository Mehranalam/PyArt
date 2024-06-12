from PIL import Image
import numpy as np

ASCII_CHARS = "@%#*+=-:. "

def resize_image(image, new_width=100):
    width, height = image.size
    aspect_ratio = height / width
    new_height = int(new_width * aspect_ratio)
    resized_image = image.resize((new_width, new_height))
    return resized_image

def grayscale_image(image):
    return image.convert("L")

def pixel_to_ascii(image):
    pixels = np.array(image)
    ascii_str = ""
    for pixel_row in pixels:
        for pixel in pixel_row:
            ascii_str += ASCII_CHARS[pixel // 32]
        ascii_str += "\n"
    return ascii_str

def image_to_ascii(image_path, output_file="ascii_art.txt", new_width=100):
    try:
        image = Image.open(image_path)
    except Exception as e:
        print(f"Unable to open image file {image_path}.")
        print(e)
        return

    image = resize_image(image, new_width)
    image = grayscale_image(image)

    ascii_str = pixel_to_ascii(image)

    with open(output_file, "w") as f:
        f.write(ascii_str)
    
    print(f"ASCII art written to {output_file}")

image_path = "input/n.jpg"
image_to_ascii(image_path)

def print_output_in():
    f = open('ascii_art.txt', 'r')
    file_contents = f.read()

    print(file_contents)
    f.close()