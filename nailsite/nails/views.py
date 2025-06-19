from django.shortcuts import render
from .forms import NailForm
from nail_creator import generate_nail_image


def index(request):
    images = None
    if request.method == 'POST':
        form = NailForm(request.POST)
        if form.is_valid():
            desc = form.cleaned_data['description']
            feelings = form.cleaned_data['feelings']
            count = form.cleaned_data['count']
            images = generate_nail_image(desc, feelings, count)
    else:
        form = NailForm()

    return render(request, 'nails/index.html', {'form': form, 'images': images})
