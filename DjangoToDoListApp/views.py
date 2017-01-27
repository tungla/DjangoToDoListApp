from django.shortcuts import render, loader

from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from models import ToDoItem

# Create your views here.
def index(request):
    # template = loader.get_template('djangotodolistapp/index.html')
    # latest_todoitems_list = ToDoItem.objects.order_by('-id')[:20]
    # context = {
    #     'latest_todoitems_list': latest_todoitems_list
    # }
    # return HttpResponse(template.render(context, request))

    todoitems_list_all = ToDoItem.objects.all()
    paginator = Paginator(todoitems_list_all, 20)
    page = request.GET.get('page')
    try:
        latest_todoitems_list = paginator.page(page)
    except PageNotAnInteger:
        latest_todoitems_list = paginator.page(1)
    except EmptyPage:
        latest_todoitems_list = paginator.page(paginator.num_pages)
    maximumPageDisplay = 5
    pageToDisplay = []
    if len(paginator.page_range) <= maximumPageDisplay:
        pageToDisplay = paginator.page_range
    else:
        totalPageNumber = len(paginator.page_range)
        page = int(page)
        pageIndex = list(paginator.page_range).index(page)
        print page, pageIndex, totalPageNumber
        if pageIndex == (totalPageNumber - 1):
            pageToDisplay = range(page - 4, page + 1)
        elif pageIndex == (totalPageNumber - 2):
            pageToDisplay = range(page - 3, page + 2)
        elif pageIndex == 0 or pageIndex == 1:
            pageToDisplay = range(1, maximumPageDisplay + 1)
        else:
            pageToDisplay = range(page - 2, page + 3)
        print pageToDisplay
    return render(request, 'djangotodolistapp/index.html', {'latest_todoitems_list': latest_todoitems_list,
                                                            'pageToDisplay': pageToDisplay})

def create(request):
    return True