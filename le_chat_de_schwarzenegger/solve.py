import os

from PIL.Image import open as load_pic, new as new_pic


def main(path, iterations, keep_all=False, name="arnold_cat-{name}-{index}.png"):
    """
    Params
        path:str
            path to photograph
        iterations:int
            number of iterations to compute
        name:str
            formattable string to use as template for file names
    """
    title = os.path.splitext(os.path.split(path)[1])[0]
    counter = 0
    while counter < iterations:
        with load_pic(path) as image:
            dim = width, height = image.size
            with new_pic(image.mode, dim) as canvas:
                for x in range(width):
                    for y in range(height):
                        nx = (2 * x + y) % width
                        ny = (x + y) % height

                        canvas.putpixel((nx, height-ny-1), image.getpixel((x, height-y-1)))

        if counter > 0 and not keep_all:
            os.remove(path)
        counter += 1
        print(counter, end="\r")
        path = name.format(name=title, index=counter)
        canvas.save(path)

    return canvas


if __name__ == "__main__":
    result = main("end.bmp", 38)
    result.show()
