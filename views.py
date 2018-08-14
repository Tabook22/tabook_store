from django.shortcuts import render

# Create your views here.

def slist_view(request):
    return render(request,'tabook_store/slist.html')
