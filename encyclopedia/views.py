from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.urls import reverse

from . import util

import markdown2


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def showentry(request, entry):
    entry_text = util.get_entry(entry)

    if entry_text is None:
        wiki_page = "<h2>" + entry + " : Entry not found</h2>"
        page_edit_menu = ""
    else:
        wiki_page = markdown2.markdown(util.get_entry(entry))
#        page_edit_menu = '<br><a href="' + reverse(updateform) + entry + '">Edit this page</a>'

    return render(request, "encyclopedia/entry.html", {
        "title": entry,
        "wiki_page": wiki_page,
#        "page_edit_menu": page_edit_menu
    })


