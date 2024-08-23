from django.shortcuts import render,redirect
from image.models import Upload

def Home(request):
    images= Upload.objects.all()
    data={"data":images}
    return render(request,"index.html",data)


def Submit(request):
    a=request.FILES.get('image')
    Upload(image=a).save()
    
    return redirect('/')