from django.shortcuts import render
from items.forms import ItemRegistForm
from django.http import HttpRequest
from main.common.template_path import items_path
from items.service import deleteItem, registerItem
from django.shortcuts import redirect

class ItemsView:
    def itemtable(request: HttpRequest):
        if not request.user.is_authenticated:
            return redirect("login")
        if request.POST:
            form = ItemRegistForm(request.POST or None)
            if form.is_valid():
                url = form.cleaned_data["url"]
                hope_price = form.cleaned_data["hope_price"]
                registerItem(url, request.user, hope_price)
        user = request.user
        items = user.items.all()
        return render(request, items_path('index'), {'items': items, 'userEmail': user.email})

    def itemregist(request: HttpRequest):
        if not request.user.is_authenticated:
            return redirect("login")
        form = ItemRegistForm()
        user = request.user
        return render(request, items_path('regist'), {'form': form, 'userEmail': user.email})

    def itemdelete(request: HttpRequest):
        if not request.user.is_authenticated:
            return redirect("login")
        if request.POST:
            deleteItem(request.POST["delete-item-id"])
        return redirect("items")