# exfiltrator
remove exif data from pictures in a folder

## Installation

	pip install Pillow
	mkdir stripped removeexif

## run

* put img files in _removeexif_ folder

	exfiltrator git:(master) ✗ ls removeexif 
	example.jpg  example.jpg 

* run python file

	exfiltrator git:(master) python exifdel.py
	[*] File Saved: Exif_Stripped_example.jpg
	[*] File Saved: Exif_Stripped_example.jpg


* use your new exfiltrated image file

	exfiltrator git:(master) ✗ ls stripped 
	074d9b7d1bb043b98430a096f35d08ea.jpg  efc0905786814091a50f6d83aebdd38e.jpg
