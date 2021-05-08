from django.shortcuts import render,redirect
from django.http import HttpResponse
import os
from recipe.models import Recipe
from recipe.form import RecipeForm

# Create your views here.
def index(request):
    gallery=Recipe.objects.all() 

    return render(request,'index.html',{'recipe_gallery':gallery})

def upload(request):
    obj=RecipeForm()

    if request.method=='POST':
        # once the form is sumbitted,fetch form params using request
        obj=RecipeForm(request.POST,request.FILES)
        #to validate form fields
        if obj.is_valid():
            # save the accepted /form data
            obj.save()
            return redirect('index')

        else:
            return HttpResponse("something wrong,reload <a href='{{url:'index'}}'>reload</a>")
    
    else:
        return render(request,'upload.html',{'upload_form':obj})

def update(request,recipe_id):
    #id()-built-in function
    # convert it to string
    recipe_id=int(recipe_id)

    try:
        #id is autogeneration field
        # using id to fetch particular book details to update 
        recipe_select=Recipe.objects.get(id=recipe_id)

    except Recipe.DoesNotExist:
        return redirect('index')

    else:
        # to displaying form with filled data
        recipe_form=RecipeForm(request.POST or None,instance=recipe_select)

        if recipe_form.is_valid():
            old_image = ""
            if recipe_select.picture:
                old_image = recipe_select.picture.path
                #data/fields are updated 
                form = RecipeForm(request.POST,request.FILES,instance = recipe_select)
                if form.is_valid():
                    if os.path.exists(old_image):
                        os.remove(old_image)
                        #updated fields will be saved
                        form.save()
            return redirect('index')
    return render(request,'upload.html',{'upload_form':recipe_form})  


def delete(request,recipe_id):
    recipe_id=int(recipe_id)
    
    try:
        recipe_select=Recipe.objects.get(id=recipe_id)

    except Recipe.DoesNotExist:
        return redirect('index')

    recipe_select.delete()
    return redirect('index')
