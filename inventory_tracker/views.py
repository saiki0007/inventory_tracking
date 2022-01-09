from django.http import HttpResponse
from django.shortcuts import redirect
from django.template import loader
from .models import Items
from .utils import download_csv


def list_items(request):
    """
    Returns the index page displaying the latest items available in the inventory
    """
    latest_product_list = Items.objects.order_by('item_id')
    template = loader.get_template('index.html')
    context = {
        'items': latest_product_list,
        'title': "Summary"
    }
    return HttpResponse(template.render(context, request))


def items(request):
    """
    Returns the items' page after addition of new item.
    """
    current_items = Items.objects.order_by('item_id')
    template = loader.get_template('items.html')
    message = None
    if request.method == 'POST':
        item_name = request.POST['item_name']
        item_type = request.POST['item_type']
        quantity = request.POST['item_quantity']
        is_allowed = False
        if item_name not in ['', ' ', None] and item_type not in ['', ' ', None] and quantity not in ['', ' ', None]:
            is_allowed = True

        if is_allowed:
            new_items = Items(item_name=item_name, item_type=item_type, item_quantity=quantity)
            new_items.save()
            message = f"{item_name} has been added to the inventory!"

    context = {
        'items': current_items,
        'message': message,
        'title': 'Items'
    }
    return HttpResponse(template.render(context, request))


def edit_item(request):
    """
    Returns the items page after saving the edits for an item
    """
    item_id = request.POST['item_id']
    item_name = request.POST['item_name']
    item_type = request.POST['item_type']
    item_quantity = request.POST['item_quantity']
    item = Items.objects.get(item_id=item_id)
    if item_name:
        item.item_name = item_name
    if item_type:
        item.item_type = item_type
    if item_quantity:
        item.item_quantity += int(item_quantity)
    item.save()
    return redirect('tracking:items')


def delete(request, item_id):
    """
    Returns the items page after deleting the item
    """
    item = Items.objects.get(item_id=item_id)
    item.delete()
    return redirect('tracking:items')


def export_csv(request):
    """
    Returns a csv file containing the inventory list.
    """
    data = download_csv(Items.objects.all())
    response = HttpResponse(data, content_type='text/csv')
    return response
