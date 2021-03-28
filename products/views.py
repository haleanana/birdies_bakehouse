from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import *


# Create your views here.
def all_products(request):

    products = Product.objects.all()
    query = None
    categories = None

    if request.GET:

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request, "You did not enter any search criteria")
                return redirect(reverse('products'))
            queries = Q(name__icontains=query) | Q(
                description__icontains=query)
            products = products.filter(queries)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')           
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)

    if request.method == "POST":
        comment_obj = Comment()
        comment_obj.user = request.user
        comment_obj.product = product

        comment_obj.comment = request.POST['com']
        total_comments = product.total_comments
        Product.objects.filter(pk=product_id).update(
            total_comments=total_comments+1)

        comment_obj.save()
    try:
        all_comments = Comment.objects.filter(product=product)
        total_comments = len(all_comments)
    except:
        total_comments = 0
    context = {
        'product_id': product_id,
        'product': product,
        'all_comments': all_comments,
        'total_comments': total_comments,
    }

    return render(request, 'products/product_detail.html', context)
