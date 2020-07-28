from django.shortcuts import render
import markdown2
from . import util

# how i view main page and connect to the rest 
def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })
# view a specific page
def detail(request , name ):
    entry = util.get_entry(name)
    context = markdown2.markdown(entry)
    return render(request, "encyclopedia/detail.html", {
        "post": context
    })

# make create a page with file system and webform 


# function to display random page 