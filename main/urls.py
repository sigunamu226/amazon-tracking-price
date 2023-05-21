from django.contrib import admin
from django.urls import path
from accounts.views import AccountView
from items.views import ItemsView

urlpatterns = [
    path('am-tracking/admin/', admin.site.urls),
    path('am-tracking', AccountView.login, name='login'),
    path('am-tracking/signup', AccountView.signup, name='signup'),
    path('am-tracking/login', AccountView.login, name='login'),
    path('am-tracking/logout', AccountView.logout, name="logout"),
    path('am-tracking/items/', ItemsView.itemtable, name="items"),
    path('am-tracking/items/regist', ItemsView.itemregist, name="items_regist"),
    path('am-tracking/items/delete', ItemsView.itemdelete, name="items_delete")
]
