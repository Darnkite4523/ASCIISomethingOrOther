from PIL import Image
from os import listdir
from libs.asciiart import summonsatan

for file in listdir("memesource"):
    # Open the image file and resize it
    img = Image.open(f"memesource/{file}")
    img = img.resize((160, 90))

    # Define the ASCII characters to use based on brightness
    chars = " .,':;!?/-_|~+-=><[](){}@#$%&*^`\""
    ascii_art = summonsatan(img, chars)
    with open(f"memeout/{file}.txt", "w") as fileout:
        fileout.write(ascii_art)
