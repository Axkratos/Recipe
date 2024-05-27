from django.shortcuts import render
from .models import Receipe

def receipes(request):
    if request.method == "POST":
        data = request.POST
        receipe_image = request.FILES.get('receipe_image')
        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')

        if receipe_name and receipe_description and receipe_image:
            Receipe.objects.create(
                receipe_image=receipe_image,
                receipe_name=receipe_name,
                receipe_description=receipe_description
            )
            return render(request, 'recipes.html', {'success': True})

    return render(request, 'recipes.html')
