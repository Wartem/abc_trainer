import pygame
from io import BytesIO

from PIL import Image, ImageDraw, ImageFont
from PySide6 import QtGui

from color_constants import ColorConst

from settings import Settings

class Gen():
    
    def __init__(self) -> None:
        pass


    def create_exit_button(self, file_name, size=100, margin=20, offset=10):
        # Create a new image with a white background
        img = Image.new("RGB", (size, size), "white")
        # Calculate the size of the triangle
        triangle_size = size - margin
        # Calculate the coordinates of the top vertex of the triangle
        top_vertex = ((size / 2), ((size - triangle_size) / 2))
        # Calculate the coordinates of the bottom-left vertex of the triangle
        bottom_left = ((size / 2) - (triangle_size / 2), ((size + triangle_size) / 2) - offset)
        # Calculate the coordinates of the bottom-right vertex of the triangle
        bottom_right = ((size / 2) + (triangle_size / 2), ((size + triangle_size) / 2) - offset)
        # Create a drawing context
        draw = ImageDraw.Draw(img)
        # Draw the triangle
        draw.polygon([top_vertex, bottom_left, bottom_right], fill="black")
        
        img = img.rotate(90, expand=True)
        
        # Save the image
        img.save(file_name)
        
        
    """     def create_exit_button(file_name, size=100, margin=20, offset=10, corner_radius=10):
        # Create a new image with a transparent background
        img = Image.new("RGBA", (size, size), (255, 255, 255, 0))
        # Calculate the size of the triangle
        triangle_size = size - margin
        # Calculate the coordinates of the top vertex of the triangle
        top_vertex = ((size / 2), ((size - triangle_size) / 2))
        # Calculate the coordinates of the bottom-left vertex of the triangle
        bottom_left = ((size / 2) - (triangle_size / 2), ((size + triangle_size) / 2) - offset)
        # Calculate the coordinates of the bottom-right vertex of the triangle
        bottom_right = ((size / 2) + (triangle_size / 2), ((size + triangle_size) / 2) - offset)
        # Create a drawing context
        draw = ImageDraw.Draw(img)
        # Draw the triangle
        draw.polygon([top_vertex, bottom_left, bottom_right], fill="black")
        
        img = img.rotate(90, expand=True)

        # Create a rounded rectangle mask with the same size as the image
        mask = Image.new("L", (size, size), 0)
        mask_draw = ImageDraw.Draw(mask)
        mask_draw.rounded_rectangle([0, 0, size, size], corner_radius, fill=255)
        mask = mask.convert("RGBA")  # Convert the mask to "RGBA" mode

        # Composite the image and mask
        base_img = Image.new("RGBA", img.size, (255, 255, 255, 0))
        base_img.alpha_composite(img)
        base_img.alpha_composite(mask)

        # Save the image
        base_img.save(file_name) """

    
    def text_image(self, font_path: str, text: str = "", width=500, height=500, background_color=(255, 255, 255), text_color=(0, 0, 0), file_name='text_img.png'):
        image = Image.new("RGB", (width, height), color=background_color)
        draw = ImageDraw.Draw(image)
        
        font_size_increment = 1
        font_size = 10
        buffer = 50
        #file_name = 'text_img.png'

        # Calculate the size of the text with a given font size
        font = ImageFont.truetype(font_path, font_size)

        # Increase font size until the text fits within the image
        try:
            while font.getsize(text)[0] < width - buffer and font.getsize(text)[1] < height - buffer:
                font_size += font_size_increment
                font = ImageFont.truetype(font_path, font_size)
        except AttributeError:
            font = ImageFont.truetype(font_path, 40)

        
        text_width, text_height = draw.textsize(text, font=font)
        
        # Calculate the position of the text to center it in the image
        text_x_pos = (width - text_width) / 2
        text_y_pos = (height - text_height) / 2
        
        # Draw the text
        draw.text((text_x_pos, text_y_pos), text, fill=text_color, font=font)
        
        print(file_name)

        # Save the image to file
        image.save(file_name)

        # Load the image into a QPixmap
        pixmap = QtGui.QPixmap(file_name)

        return pixmap


""" 
To use an image in memory as the icon for a button in PyQt5, you can 
create a QPixmap from the image data in a BytesIO object, and then create 
a QIcon from the QPixmap. Here's an example:

# Create the BytesIO object with your image data
image_data = ... # replace this with your image data
image = io.BytesIO(image_data)

# Load the image into a QPixmap
pixmap = QtGui.QPixmap()
pixmap.loadFromData(image.getvalue())

# Create the QIcon from the QPixmap
icon = QtGui.QIcon(pixmap)

# Use the QIcon as the icon for your button
button = QtGui.QPushButton()
button.setIcon(icon)

Note that you'll need to replace ... with your actual image data. 
You can obtain the image data from a file, for example, using 
the open function and reading the contents of the file into a bytes object.
"""