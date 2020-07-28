from django.shortcuts import render
from .models import Wiki_Page
from .forms import Wiki_Form
from . import util

# how i view main page 
def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def create_view(request):
    context = {}

    form = Wiki_Form(request.POST or None)
    if form.is_valid():
        form.save()

    context['form'] = form