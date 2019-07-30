from pathlib import Path
import os
import shutil
import time
import random
from shutil import copyfile

for filename in Path('/home/tom/Devel/recall/data/shop_dataset/working/pants').glob('**/*feedback*.jpg'):


    new_file=os.path.join('/home/tom/Downloads/object_detection_demo-master/data/images/new', str(random.randint(0, 999999999999999999)) + ".jpg")
    copyfile(filename, new_file)
