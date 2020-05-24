#!/usr/bin/env python3

import os
import glob
from PIL import Image

size = 600, 400

for file in glob.glob("/home/student-04-8509cc2bbce2/supplier-data/images/*.tiff"):
  print(os.path.basename(file))
  newFilename = os.path.basename(file).replace("tiff","jpeg")
  print(newFilename)
  im = Image.open(file).convert('RGB')
  im.resize((size)).save("/home/student-04-8509cc2bbce2/supplier-data/images/" + newFilename, "jpeg")
