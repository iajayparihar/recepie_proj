from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse
# Create your views here.

def index(request):
    # Fetch all recipes
    queryset = Recepie.objects.all()

    if request.GET.get('search'):
        # Filter recipes by name if search query is provided
        queryset = queryset.filter(name__icontains=request.GET.get('search'))

    context = {'recepies': queryset}

    if request.method == "POST":
        data = request.POST

        # Get data from the form
        name = data.get('name')
        description = data.get('description')
        image = request.FILES.get('image')

        if name is not None and name.strip():  # Check if the name is not None and not empty or whitespace
            # Save data to the database
            Recepie.objects.create(
                name=name,
                description=description,
                image=image
            )

    return render(request, 'html/chat.html', context)

def update(request, id ):  # sourcery skip: extract-method
    row = Recepie.objects.get(id = id )
    context = { "recepie" : row }
    
    if request.method == 'POST':
        data = request.POST
        # geting the data
        name = data.get('name')
        description = data.get('description')
        image = request.FILES.get('image')

        row.name = name 
        row.description = description

        if image :
            row.image = image
            
        row.save()
        
        return redirect('/')
    return render(request,'html/update.html',context)


def delete(request,id):
    a = Recepie.objects.get( id = id )
    a.delete()
    return redirect('/')


