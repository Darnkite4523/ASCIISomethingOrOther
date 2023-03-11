def summonsatan(img, chars):
    # Convert each pixel to an ASCII character
    ascii_art = ""
    for y in range(img.size[1]):
        for x in range(img.size[0]):
            pixel = img.getpixel((x, y))
            brightness = (sum(pixel) / len(pixel)) / 255 # average of RGB (and maybe A) values
            char_index = int((len(chars) - 1) * brightness)
            try: 
                ascii_art += chars[char_index]
            except:
                print(char_index)
                print(brightness)
                raise Exception("your shits fucked")
        ascii_art += "\n"
    return ascii_art