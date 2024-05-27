from django.shortcuts import render, get_object_or_404
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
            return redirect('receipes')

    search_query = request.GET.get('search', '')
    if search_query:
        queryset = Receipe.objects.filter(receipe_name__icontains=search_query)
    else:
        queryset = Receipe.objects.all()

    context = {'receipes': queryset, 'search_query': search_query}
    return render(request, 'recipes.html', context)

def delete_receipe(request, id):
    queryset = get_object_or_404(Receipe, id=id)
    queryset.delete()
    return render(request, 'recipes.html', {'success': True})

def update_receipe(request, id):
    queryset = get_object_or_404(Receipe, id=id)

    if request.method == 'POST':
        data = request.POST
        receipe_image = request.FILES.get('receipe_image')
        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')

        queryset.receipe_name = receipe_name
        queryset.receipe_description = receipe_description

        if receipe_image:
            queryset.receipe_image = receipe_image

        queryset.save()
        return render(request, 'recipes.html', {'success': True, 'receipe': queryset})

    context = {'receipe': queryset}
    return render(request, 'updatereceipes.html', context)
