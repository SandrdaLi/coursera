#!/usr/bin/env python

import subprocess, os
from multiprocessing import Pool

src = "/home/student-04-34697568baad/data/prod"
dest = "/home/student-04-34697568baad/data/prod_backup"

def run(dir):
  subprocess.call(["rsync", "-arq", dir, dest])

if __name__ == "__main__":
  dir_list = []
  for root, dirs, files in os.walk(src, topdown=False):
    if root == src:
      for name in dirs:
        sub_dir = os.path.join(root, name)
        dir_list.append(sub_dir)

  p = Pool(len(dir_list))
  p.map(run, dir_list)
