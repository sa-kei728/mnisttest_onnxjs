#!/usr/bin/python

import urllib.request
import gzip
import numpy as np
from PIL import Image, ImageOps

url_base = 'http://yann.lecun.com/exdb/mnist/'
key_file = {
    'test_img':'t10k-images-idx3-ubyte.gz',
}

dataset_dir = "./mnistdata"
for v in key_file.values():
    file_path = dataset_dir + '/' + v
    urllib.request.urlretrieve(url_base + v, file_path)

file_path = dataset_dir + key_file['test_img']
with gzip.open(file_path, 'rb') as f:
    data = np.frombuffer(f.read(), np.uint8, offset=16)

