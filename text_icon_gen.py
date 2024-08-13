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
        

    
    def text_image(self, font_path: str, text: str = "", width=500, height=500, background_color=(255, 255, 255), text_color=(0, 0, 0), file_name='text_img.png'):
        image = Image.new("RGB", (width, height), color=background_color)
        draw = ImageDraw.Draw(image)
        
        font_size_increment = 1
        font_size = 10
        buffer = 50

        # Calculate the size of the text with a given font size
        font = ImageFont.truetype(font_path, font_size)

        # Increase font size until the text fits within the image
        while True:
            bbox = font.getbbox(text)
            if bbox[2] - bbox[0] >= width - buffer or bbox[3] - bbox[1] >= height - buffer:
                font_size -= font_size_increment  # Go back one step
                font = ImageFont.truetype(font_path, font_size)
                break
            font_size += font_size_increment
            font = ImageFont.truetype(font_path, font_size)

        # Get the final text dimensions
        bbox = font.getbbox(text)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
        
        # Calculate the position of the text to center it in the image
        text_x_pos = (width - text_width) / 2
        text_y_pos = (height - text_height) / 2
        
        # Draw the text
        draw.text((text_x_pos, text_y_pos), text, fill=text_color, font=font)
        
        # Save the image to file
        image.save(file_name)

        # Load the image into a QPixmap
        pixmap = QtGui.QPixmap(file_name)

        return pixmap