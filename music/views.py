from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

# # The very first version of the index view, used only in the setup phase.
# # It just prints something in the browser.
# def index(request):
#     return HttpResponse("<h1>Woodstock</h1>")


def index(request):
    """The index view that defines a context to be rendered in index.html.
    This context includes, e.g., the numbers of Performer and Festival objects in the database.
    These numbers can be retrieved using <Model>.objects.all().count().
    The context is specified as a dictionary with the items in the format:
        '<string to be used in the index.html template>': <data item (e.g., the number of performers)>
    The view returns the result of the render() function,
    passing it the request, the template file name, and the context.
    """


class PerformerListView(ListView):
    """Class-based view that handles lists of Performer objects.
    Typical fields that ListView-based classes specify include:
        - model (class name of the corresponding <Model> class
        - template_name ('<app>/<template file name>'; default: '<app>/<model>_list.html')
    Typically, such views also override ListView.get_queryset(),
    making it return a QuerySet of objects (such as (possibly filtered) <Model>.objects.all()))
    """


class PerformerDetailView(DetailView):
    """Class-based view that handles individual Performer objects.
    Typical fields that ListView-based classes specify include:
        - model (class name of the corresponding <Model> class
        - template_name ('<app>/<template file name>'; default: '<app>/<model>_detail.html')
    """


class FestivalListView(ListView):
    """Class-based view that handles lists of Festival objects.
    Typical fields that ListView-based classes specify include:
        - model (class name of the corresponding <Model> class
        - template_name ('<app>/<template file name>'; default: '<app>/<model>_list.html')
    Typically, such views also override ListView.get_queryset(),
    making it return a QuerySet of objects (such as (possibly filtered) <Model>.objects.all()))
    """


class FestivalDetailView(DetailView):
    """Class-based view that handles individual Festival objects.
    Typical fields that ListView-based classes specify include:
        - model (class name of the corresponding <Model> class
        - template_name ('<app>/<template file name>'; default: '<app>/<model>_detail.html')
    """




