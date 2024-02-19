import sys
from PIL import Image
from PIL import ImageOps
formatos = ['jpg','png','jpeg']


if len(sys.argv) > 3 :
    sys.exit("to many arguments")
elif len(sys.argv) < 3:
    sys.exit("to few arguments")
else :
    inp = sys.argv[1].lower().split(".")
    out = sys.argv[2].lower().split(".")

if inp[-1] not in formatos:
    sys.exit("formato incorrecto entrada")
elif out[-1] not in formatos:
    sys.exit("formato incorrecto salida")
elif out[-1] != inp[-1]:
    sys.exit("formato incorrecto salida final")
else :
    try:
        """
        with Image.open("shirt.png") as im1:
            print(im1.size)
            """
        size_shirt = (600 , 600)
        with Image.open(sys.argv[1]) as im:
            newim = ImageOps.fit(im, size = size_shirt, bleed=0.0, centering=(0.5, 0.5))
            with Image.open("shirt.png") as im1:
                newim.paste(im1,im1)
                #newim = newim.paste(newim,im1)
                newim.save(sys.argv[2])

    except FileNotFoundError:
        sys.exit("File does not exist")