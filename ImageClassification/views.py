from turtle import up
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from .models import Info

from django.conf import settings 

from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.models import load_model

labels = ['Airplane', 'Automobile', 'Bird', 'Cat', 'Deer', 'Dog', 'Frog', 'Horse', 'Ship', 'Truck']

def load_image(filename):
	image = load_img(filename, target_size=(32, 32))
	image = img_to_array(image)
	image = image.reshape(1, 32, 32, 3)
	image = image.astype('float32')/255.0
	return image

def predict(image_path):
	image = load_image(image_path)
	model = load_model('ImageClassification/models/current.h5')
	result = model.predict_classes(image)
	return labels[result[0]]	

def index(request):
	if request.method == 'POST' and request.FILES['upload']:
		upload = request.FILES['upload']
		fss = FileSystemStorage()
		file = fss.save(upload.name, upload)
		file_url = fss.url(file)
		full_path = settings.MEDIA_ROOT.replace('\\', '/') + "/" + file
		result = predict(full_path)
		Info.save(Info.objects.create(imageLink=full_path, result=result))
	
		return render(request, 'ImageClassification/index.html', {'file_url': file_url, 'result': result})
	return render(request, 'ImageClassification/index.html')

