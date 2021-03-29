from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404

# Create your views here.
def view_bag(request):

    return render(request, 'bag/bag.html')

def add_to_bag(request, item_id):

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
        # messages.success(
        #     request, f'Updated {product.name} to {bag[item_id]}')
    else:
        bag[item_id] = quantity
        # messages.success(request, f'Added {product.name} to your bag! ')

    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity

    if quantity > 0:
        bag[item_id] = quantity
    else:
        bag.pop(item_id)

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))

def remove_from_bag(request, item_id):
    """Remove the item from the shopping bag"""
    try:
        product = get_object_or_404(Product, pk=item_id)
        info = None
        if 'product_info' in request.POST:
            size = request.POST['product_info']
        bag = request.session.get('bag', {})

        if size:
            del bag[item_id]['items_by_info'][info]
            if not bag[item_id]['items_by_info']:
                bag.pop(item_id)
        else:
            bag.pop(item_id)

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)
