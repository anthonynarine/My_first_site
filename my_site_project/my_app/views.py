from django.shortcuts import render

# Create your views here.
def exampl_view(request):
    return render(request,"my_app/example.html" ) 

    #NOTE USE OF render FUNCTION  
    #my_app/example.html will be referring to 
    #my_app/templates/my_app/example.html

def variable_view(request):
    my_var = {"first_name": "Julia", "last_name": "Narine"}
#to pass this variable to be used in variable.html we pass the arg context
#set it equal to the variable name. 
    return render(request, "my_app/variables.html", context=my_var)
