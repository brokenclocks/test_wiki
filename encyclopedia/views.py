import markdown2
from django.core.exceptions import ValidationError
from django.shortcuts import render , redirect
from django.urls import reverse
from encyclopedia.forms import Wiki_Form
from . import util


def index(request):  # get index page run setup filter function than display content
    setup = request.POST.get('search') or ""
    val_list = index_filter(setup)  # value of list to send to context
 # random variable sent to context and liked in link will allow random page link to work

    if len(val_list) == 1:
        return redirect('detail', name=val_list[0])

    return render(request, "encyclopedia/index.html", {
        "entries": val_list,

    })


def index_filter(c):  # function to filter a list
    data = util.list_entries()
    send = []
    for item in data:
        if c in item:
            send.append(item)
    if c == "" or c is None:
       send = data
    return send


def detail(request, name):  # view a specific page needs argument
    entry = util.get_entry(name)
    context = markdown2.markdown(entry)
    return render(request, "encyclopedia/detail.html", {
        "post": context
    })


def create(request):  # create a markdown page
    form = Wiki_Form()

    if request.method == "POST":
         form = Wiki_Form(request.POST)
         title = request.POST.get('title')
         body = request.POST.get('body')
         if util.get_entry(title) != True:
             raise ValidationError(_('title used'), code=title)
         else:
            util.save_entry(title, body)

    else:
        form = Wiki_Form()
    return render(request, 'encyclopedia/create.html', {'form': form})

def edit(request): # edit a markdown page
    pass
#
# def error_404(request,exception):
#    return render(request, 'encyclopedia/404.html')
#
#
#
# def error_500(request):
#     return render(request, 'encyclopedia/404.html')
