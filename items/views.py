import uuid
from django.shortcuts import render
from items.forms import ItemRegistForm
from items.models import Item
from django.http import HttpRequest
from main.common.template_path import items_path
from items.service import amazonTrackingPrice
from django.shortcuts import redirect


# Create your views here.
class ItemsView:
    def itemtable(request: HttpRequest):
        if not request.user.is_authenticated:
            return redirect("login")
        if request.POST:
            form = ItemRegistForm(request.POST or None)
            if form.is_valid():
                url = form.cleaned_data["url"]
                hope_price = form.cleaned_data["hope_price"]
                item_list = amazonTrackingPrice(url)
                item = Item(name=item_list[0], image=item_list[1], now_price=item_list[2], hope_price=hope_price, url=url)
                item.save()
        items = Item.objects.all()
        return render(request, items_path('index'), {'items': items})

    def itemregist(request: HttpRequest):
        if not request.user.is_authenticated:
            return redirect("login")
        form = ItemRegistForm()
        return render(request, items_path('regist'), {'form': form})

    def itemdelete(request: HttpRequest):
        if not request.user.is_authenticated:
            return redirect("login")
        if request.POST:
            deleteItemId = request.POST["delete_item_id"]
            Item.objects.filter(id=deleteItemId).delete()
        return redirect("items")