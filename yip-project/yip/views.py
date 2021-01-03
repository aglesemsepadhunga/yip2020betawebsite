from django.shortcuts import render

def home(request):
    return render(request,'yip/homepage.html')
def about(request):
    return render(request,'yip/about.html')
def contacts(request):
    return render(request,'yip/contacts.html')
def gallery(request):
    return render(request,'yip/gallery.html')
def media(request):
    return render(request,'yip/media.html')
def msg_from_org(request):
    return render(request,'yip/msg_from_org.html')
def prev_yip(request):
    return render(request,'yip/prev_yip.html')
def testimonials(request):
    return render(request,'yip/testimonials.html')
def themes(request):
    return render(request,'yip/themes.html')
def why_yip(request):
    return render(request,'yip/why_yip.html')
def winners(request):
    return render(request,'yip/winners.html')
def login(request):
    return render(request,'yip/login.html')
def signup(request):
    return render(request,'yip/signup.html')