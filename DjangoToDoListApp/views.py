from django.shortcuts import render, loader

from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from models import ToDoItem

# Create your views here.
def index(request):
    # Get all to do item in database
    allToDoItems = ToDoItem.objects.all()
    # Create paginator Object with 20 item per page
    paginator = Paginator(allToDoItems, 20)
    # Get requested page number by user
    page = request.GET.get('page')
    # Set page number = 1 if page is None
    if page == None:
        page = 1
    try:
        # Create current page object based on user request
        currentToDoItems = paginator.page(page)
    except PageNotAnInteger:
        # If user request non-exist page number, return page number 1
        currentToDoItems = paginator.page(1)
    except EmptyPage:
        # If user request page number exceed maximum page, return max page number
        currentToDoItems = paginator.page(paginator.num_pages)
    maximumPageDisplay = 5 # Maximum page to display in paging section
    pageToDisplay = [] # List of page number to dispaly in paging section
    if len(paginator.page_range) <= maximumPageDisplay:
        pageToDisplay = paginator.page_range
    else:
        totalPageNumber = len(paginator.page_range) # Largest page number from paginator object
        page = int(page)
        pageIndex = list(paginator.page_range).index(page) # Index of current page in list of page range
        print page, pageIndex, totalPageNumber
        # If current page is last page
        if pageIndex == (totalPageNumber - 1):
            pageToDisplay = range(page - 4, page + 1)
        # If current page is last page - 1
        elif pageIndex == (totalPageNumber - 2):
            pageToDisplay = range(page - 3, page + 2)
        # If current page is first page or second page
        elif pageIndex == 0 or pageIndex == 1:
            pageToDisplay = range(1, maximumPageDisplay + 1)
        else:
            pageToDisplay = range(page - 2, page + 3)
        print pageToDisplay
    return render(request, 'djangotodolistapp/index.html', {'currentToDoItems': currentToDoItems,
                                                            'pageToDisplay': pageToDisplay})

def create(request):
    return True