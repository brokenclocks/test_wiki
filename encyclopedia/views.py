from django.shortcuts import render

from . import util

# how i view main page 
def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

