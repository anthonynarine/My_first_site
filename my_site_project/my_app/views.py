from django.shortcuts import render

# Create your views here.
def exampl_view(request):
    return render(request,"my_app/example.html" ) #my_app/example.html will be referring to 
                                                  #my_app/templates/my_app/example.html  