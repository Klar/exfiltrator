import os, sys
#pip install Pillow
from PIL import Image as Image
import uuid


file_path = "removeexif"

for imagename in os.listdir(file_path):

    image = Image.open(file_path + "/" + imagename)
    data = list(image.getdata())
    image_without_exif = Image.new(image.mode, image.size)
    image_without_exif.putdata(data)

    image_without_exif.save("stripped" + "/" + uuid.uuid4().hex + ".jpg")
    # os.remove(file_path + "/" + imagename)

    print("[*] File Saved: Exif_Stripped_%s" % (imagename))

sys.exit(0)