from django.shortcuts import render

# Create your views here.
 

def HomeRender(request):
    context = {} # data need to sent along responce. 
    if request.method == "POST":
        pass
    else:
        return render(request, 'blog/blog.home.html', context) # render Homage page. 