# Image Classification Django + Keras + CIFAR-10 dataset + Saving in Database 
This project was created as the Final Project for the Advanced Programming 2 course. 
It is a website with a single page, where you can upload image, then functionality of CNN based image classifier will run, and output result.
Check example:) 

### Installation
Copy from source
```bash
git clone https://github.com/Assylken/ImageClassification.git

```

### Usage

```
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.models import load_model
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.conf import settings 
from tensorflow.keras.datasets import cifar10
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.models import load_model
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Conv2D, MaxPooling2D, Flatten
from tensorflow.keras.optimizers import SGD
```

### Examples
Home Page: <br />
<img src="/images/image_screen.png" width="600" height="300"/> <br />
