from django.http.request import HttpRequest
from django.http.response import HttpResponse

from os import path
from django.shortcuts import render
import numpy
from PIL import Image
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from .forms import UploadFileForm

# Imaginary function to handle an uploaded file.
#from somewhere import handle_uploaded_file

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        print form
        if form.is_valid():
            file_name  = request.FILES["file"]
            uploaded_image  = request.FILES["image"]
            cloud_popup(file_name, uploaded_image)
            return HttpResponseRedirect("/success")
    else:
        form = UploadFileForm()
    return render_to_response('inputform.html', {'form': form})

def success(request):
    return HttpResponse ("Waoooo here is the word cloud---> Thank you")

def cloud_popup(file_name, uploaded_image):
    text = file_name.read()
    #<PIL.JpegImagePlugin.JpegImageFile image mode=RGB size=640x360 at 0x7F28EF7FE878>
    display_image=numpy.array(Image.open(uploaded_image))
#     print "=="
#     #print display_image
#     print "//////"
    stopwords=set(STOPWORDS)
    wc=WordCloud(background_color="white", max_words=2000, mask=display_image,
                   stopwords=stopwords.add("said"))
    wc.generate(text)
    plt.imshow(wc)
    plt.axis("off")
    plt.show()
