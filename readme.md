
REGISTERING an APP with Django PROJECT

1. go to project setting.py 
2. go to INSTALLED_APPS
3. Add app to list
4. "my_app.apps.MyAppConfig" (don't forget a comma!) SAVE
5. Make sure under templates "APP_DIRS" = True
    ~This lets the project know it can start looking this app
    directory to begin connecting to templates and veiws... 

Passing Information From Python views to template HTML. 

Passing a variable into and html template using render(context)
1. create variable
    my_var = {"first_name": "Old", "last_name": "Copper"}

2. pass variable in using context 
    return render(request, "my_app/variables.html", context=my_var)

3. link to html file. 
    <h2>{{firs_name}}</h2>
    2x curley braces and refrence a key
     <h2>Her first name is {{first_name}} her last name is {{last_name}}</h2>

USING AN INDEX IN FROM A PYTHON LIST IN HTML
    Python ->  some_list = [1,2,3]
        acces -> somet_list[0] = 1
    
    HTML ->  <h2>{{some_list.0}}</h2> = 1 #note . notation


COMMENTING OUT THINGS IN Django.
     <h2>{#This is a Django style comment#}</h2> 
     ~this will not show up in the browser. 


Django Filters

 are built in modifiers taht all to quickly apply a change to a 
 variable on the template rather than on the python script. 

    {{first_name |upper}} #the vertical bar | declares you will be 
    usint a filter


Django Tags - For loops







