from django.urls import path, re_path

from . import views
app_name = 'tracking'
urlpatterns = [
    path('', views.list_items, name='list_items'),
    re_path(r'^items/$', views.items, name='items'),
    path('<int:item_id>/', views.delete, name='delete'),
    re_path(r'^edit_item/$', views.edit_item, name='edit_item'),
    re_path(r'^export_csv/$', views.export_csv, name='export_csv'),
]
