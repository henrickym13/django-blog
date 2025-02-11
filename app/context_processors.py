from category.models import Category


def global_configurations(request):
    categories = Category.objects.all()
    return {'categories': categories}