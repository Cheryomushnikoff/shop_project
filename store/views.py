from django.shortcuts import render, get_object_or_404
from .models import Category, Product

def homepage_view(request):
    return render(request, 'store/home_page.html')

def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    catalog = Product.objects.all()

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        catalog = Product.objects.filter(category=category)

    context = {
        'category': category,
        'categories': categories,
        'catalog': catalog
    }

    return render(request, 'store/catalog.html', context)