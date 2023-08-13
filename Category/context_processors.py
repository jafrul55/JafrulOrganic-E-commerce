from .models import Category
# Context processors
def menu_links(request):
    links = Category.objects.all()
    return dict(links=links)