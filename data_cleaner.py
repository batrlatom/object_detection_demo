"""
cleans files without bbox info

"""

import os
import pathlib
import glob


from pathlib import Path


p_jpgs = Path('/home/tom/Downloads/object_detection_demo-master/data/images/test/').glob('**/*.jpg')
p_xmls = Path('/home/tom/Downloads/object_detection_demo-master/data/images/test/').glob('**/*.xml')

jpgs = {os.path.splitext(x)[0] for x in p_jpgs if x.is_file()}
xmls = {os.path.splitext(x)[0] for x in p_xmls if x.is_file()}

difference_one = (xmls.difference(jpgs))
difference_two = (jpgs.difference(xmls))


print("*******************")
print(difference_one)
print("*******************")
print(difference_two)
print("*******************")


# remove all files which are not in pairs
for i, path in enumerate(difference_one):

    print(Path(path).with_suffix('.xml'))
    Path(path).with_suffix('.xml').unlink()


for i, path in enumerate(difference_two):
    #path.with_suffix('.jpg').unlink()
    print(Path(path).with_suffix('.jpg'))
    Path(path).with_suffix('.jpg').unlink()
