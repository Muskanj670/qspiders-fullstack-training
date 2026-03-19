from django.http import HttpResponse
# Create your views here.
def home(request):
    return HttpResponse('Hello World')
def fun(request):
    return HttpResponse('Python is Fun')
def html(request):
    return HttpResponse("<center><H1> Muskan Jain </h1>"
                                "<H3>You can do it! </h3>" \
                        "<P>Lorem ipsum, dolor sit amet consectetur adipisicing elit. Ad id ipsam debitis quidem doloribus error assumenda ducimus, minus aliquam hic voluptatem <br> laboriosam exercitationem aliquid doloremque quo modi placeat nisi. Nam.</P></center>")

def htmlFile(request):
    a = open(r'firstProject\firstProject\index.html','r')
    data = a.read()
    print(data)
    a.close()
    return HttpResponse(data)