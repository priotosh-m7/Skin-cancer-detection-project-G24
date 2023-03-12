import numpy
from django.shortcuts import render
from django.http import HttpResponse
from .forms import UploadImageForm
from .models import UploadImage
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import keras
import random


def index(request):
    model_o = load_model('C:\\SCDProject\\static\\model_melanoma_non_new_cleaned_2512.h5')
    submitted = False
    imagename = ""
    result = []
    p_image = ""
    if request.method == "POST":
        form = UploadImageForm(request.POST,request.FILES)
        
        if form.is_valid():
            user = form.cleaned_data['user']
            #form.cleaned_data['user'] = 
            submitted = True
            
            form.save()
            p_image = UploadImage.objects.get(user=user)
            from keras.utils import load_img
            import tensorflow
            import cv2
            

            img = tensorflow.keras.preprocessing.image.load_img("C:\\SCDProject"+p_image.image.url,target_size = (200,200))
            
            #denoising

            src = cv2.imread("C:\\SCDProject"+p_image.image.url)
            grayScale = cv2.cvtColor(src, cv2.COLOR_RGB2GRAY)
            kernel = cv2.getStructuringElement(1, (17, 17))
            blackhat = cv2.morphologyEx(grayScale, cv2.MORPH_BLACKHAT, kernel)
            ret, thresh2 = cv2.threshold(blackhat, 10, 255, cv2.THRESH_BINARY)
            dst = cv2.inpaint(src, thresh2, 1, cv2.INPAINT_TELEA)
    # cv2.imshow("InPaint", dst)
            cv2.imwrite( "C:\\SCDProject"+p_image.image.url+".jpg", dst, [int(cv2.IMWRITE_JPEG_QUALITY), 90])
            
            cleaned_img = tensorflow.keras.preprocessing.image.load_img("C:\\SCDProject"+p_image.image.url+".jpg",target_size = (200,200))
            
            
            import warnings
            import numpy as np
            warnings.filterwarnings('ignore')
            test_image = tensorflow.keras.preprocessing.image.img_to_array(cleaned_img)
            test_image = test_image/255
            test_image = np.expand_dims(test_image, axis = 0)
            result = model_o.predict(test_image)
            if result[0][0]>0:
                imagename += "Non-Melanoma/ Normally"

            else:
                imagename += "Melanoma / Anomaly Detected"
            

        else:
            form = UploadImageForm
            if 'submitted' in request.GET:
                submitted = True
        
    form = UploadImageForm
    #p_image = UploadImage.objects.get(user=user)
    context = p_image
    
    
    

# load model
    no = int(random.randint(1,999))
    return render(request,'emp_upload.html',{'form':form, 'submitted':submitted , 'context':context ,'result':result , 'no' : no, 'imagename':imagename})


# Create your views here.


def index2(request):
    model_o = load_model('C:\\SCDProject\\static\\multiclass_AB_07-03-2023_96.51.h5')
    submitted = False
    imagename = ""
    result = []
    chartdata = []
    results = []
    p_image = ""
    major = []
    dict = {0: 'acnitic keratosis',
            1: 'basal cell carcinoma',
            2: 'benign keratosis',
            3: 'dermatofibroma',
            4: 'healthy skin',
            5: 'melanocytic nevus',
            6: 'melanoma',

            7: 'squamous cell carcinoma',
            8: 'vascular lesion'}

    if request.method == "POST":
        form = UploadImageForm(request.POST, request.FILES)

        if form.is_valid():
            user = form.cleaned_data['user']
            # form.cleaned_data['user'] =
            submitted = True

            form.save()
            p_image = UploadImage.objects.get(user=user)
            from keras.utils import load_img
            import tensorflow
            import cv2

            img = tensorflow.keras.preprocessing.image.load_img("C:\\SCDProject" + p_image.image.url,
                                                                target_size=(200, 200))

            # denoising

            src = cv2.imread("C:\\SCDProject" + p_image.image.url)
            grayScale = cv2.cvtColor(src, cv2.COLOR_RGB2GRAY)
            kernel = cv2.getStructuringElement(1, (17, 17))
            blackhat = cv2.morphologyEx(grayScale, cv2.MORPH_BLACKHAT, kernel)
            ret, thresh2 = cv2.threshold(blackhat, 10, 255, cv2.THRESH_BINARY)
            dst = cv2.inpaint(src, thresh2, 1, cv2.INPAINT_TELEA)
            # cv2.imshow("InPaint", dst)
            cv2.imwrite("C:\\SCDProject" + p_image.image.url + ".jpg", dst, [int(cv2.IMWRITE_JPEG_QUALITY), 90])

            cleaned_img = tensorflow.keras.preprocessing.image.load_img("C:\\SCDProject" + p_image.image.url + ".jpg",
                                                                        target_size=(200, 200))

            import warnings
            import numpy as np
            warnings.filterwarnings('ignore')
            test_image = tensorflow.keras.preprocessing.image.img_to_array(cleaned_img)
           ## test_image = test_image / 255
            test_image = np.expand_dims(test_image, axis=0)
            result = model_o.predict(test_image)
            result = np.array(result)
            major = dict.get(result.argmax())
            sum = 0
            for i in range(0, 9):
                if result[0][i] >= 0:
                    sum += result[0][i]

            sum = abs(sum)

            for i in range(0, 9):
                if result[0][i] >= 0:
                    perc = ((result[0][i]) / sum) * 100
                    perc = round(perc,4)
                    chartdata.append(perc)
                    imagename = dict[i] + " : "+numpy.format_float_positional(perc)+"%"
                    results.append(imagename)
                else:
                    chartdata.append(0)
                   # print(f"{dict[i]} : {perc}%")





        else:
            form = UploadImageForm
            if 'submitted' in request.GET:
                submitted = True

    form = UploadImageForm
    # p_image = UploadImage.objects.get(user=user)
    context = p_image

    # load model
    no = int(random.randint(1, 999))
    return render(request, 'multi_upload.html',
                  {'form': form, 'submitted': submitted, 'context': context, 'result': result, 'no': no,
                   'imagename': major, 'results':results, 'data' : chartdata, 'dict':dict})

