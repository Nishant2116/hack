from django.shortcuts import render,HttpResponse

# Create your views here.

def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
    #return HttpResponse('This is about page...')
def contact(request):
    return render(request,'contact.html')
    #return HttpResponse('This is contact page..')
def services(request):
    return render(request,'services.html')
    #return HttpResponse('This is Services page...')
def carousel(request):
    return render(request, 'carousel.html')
def dataset(request):
    return render(request,'dataset.html')


