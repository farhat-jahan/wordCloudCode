from django.http.request import HttpRequest
from django.http.response import HttpResponse

from os import path
from django.shortcuts import render
print"///////////path/////////////////", path
import numpy
from PIL import Image
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt


def index_page(request):
   # dir_path=path.dirname(__file__)
   # print "dir_path===",dir_path
    t = '//home/farhat/GMP/wordCloudCode/cloud/web/templates/constitution.txt'
    print "t is=============",t
    #template = 'service-desk/feedback_details.html'
    #template = 'constitution.txt'
   # print "template===", template
   # text=open(path.join(dir_path, 'constitution.txt')).read()
    text=open(t ).read()
    
   # print "text got==============", text
    
   # constitution=numpy.array(Image.open(path.join(dir_path, "constitution.png")))
    constitution=numpy.array(Image.open("/home/farhat/GMP/wordCloudCode/cloud/web/static/img//constitution.png"))
    stopwords=set(STOPWORDS)
    wc=WordCloud(background_color="white", max_words=2000, mask=constitution,
                   stopwords=stopwords.add("said"))
    wc.generate(text)
    
    plt.imshow(wc)
    #plt.figure()
    plt.axis("off")
    #plt.imshow(constitution, cmap=plt.cm.gray)
    plt.show()

    
    return HttpResponse(request, plt.show() )
    