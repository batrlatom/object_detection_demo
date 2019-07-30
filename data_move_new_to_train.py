"""
cleans files without bbox info

"""

import os
import pathlib
import glob
import time
import random
from pathlib import Path


p_jpgs = Path('/home/tom/Downloads/object_detection_demo-master/data/images/new/').glob('**/*.jpg')
p_xmls = Path('/home/tom/Downloads/object_detection_demo-master/data/images/new/').glob('**/*.xml')

jpgs = {os.path.splitext(x) for x in p_jpgs if x.is_file()}
xmls = {os.path.splitext(x) for x in p_xmls if x.is_file()}


# change name of all file pairs
for i, path in enumerate(jpgs):
    print(path)
    head, tail = os.path.split(path[0])
    new_filename_head = Path(os.path.join(head,str(random.randint(0, int(time.time())))))
    print(new_filename_head)
    os.rename(Path(path[0]).with_suffix('.jpg'), new_filename_head.with_suffix('.jpg'))
    os.rename(Path(path[0]).with_suffix('.xml'), new_filename_head.with_suffix('.xml'))
