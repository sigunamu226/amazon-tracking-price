from django.contrib import admin
from django.urls import path
from accounts.views import AccountView
from items.views import ItemsView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', AccountView.login, name='login'),
    path('signup', AccountView.signup, name='signup'),
    path('login', AccountView.login, name='login'),
    path('logout', AccountView.logout, name="logout"),
    path('items/', ItemsView.itemtable, name="items"),
    path('items/regist', ItemsView.itemregist, name="items_regist"),
]
