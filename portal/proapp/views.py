from django.shortcuts import render


def profunction(request):
    return render(request, 'pro.html')








# def drama(ref):
#     n1="Lovely Runner is a sci-fi drama"
#     n2="Queen of tears is a melo-love drama"
#     n3="Doom at your service is a superfictional drama"
#     return render(ref,'pro.html',{'n1':n1 , 'n2':n2,'n3':n3})
# Create your views here.
