from PIL import Image, ImageDraw


def add_fraction_lines(image_path, output_path):
    img = Image.open(image_path)
    draw = ImageDraw.Draw(img)

    width, height = img.size

    fractions = {
        1 / 8: {"color": "blue", "size": 1},
        1 / 4: {"color": "green", "size": 2},
        1 / 2: {"color": "red", "size": 4},
    }

    for frac, settings in fractions.items():

        denominator = frac.as_integer_ratio()[1]

        for i in range(1, denominator):
            x = (width / denominator) * i
            y = (height / denominator) * i

            coordinates_x = x, 0, x, height
            coordinates_y = 0, y, width, y

            draw.line(coordinates_x, fill=settings["color"], width=settings["size"])
            draw.line(coordinates_y, fill=settings["color"], width=settings["size"])


    img.save(output_path)

in_path = input("Enter the image name. MAKE SURE THE IMAGE IS IN THE SAME FOLDER AS THE SCRIPT: ")
out_path = input("Enter the name of the output image file: ")
add_fraction_lines(in_path, out_path)
