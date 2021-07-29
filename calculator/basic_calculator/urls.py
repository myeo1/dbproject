from django.urls import path
from . import views

# All the class based views will need to be imported
from basic_calculator.views import AddView, SubView, DivView, MultiView
# All the classes will be used as views and each one will have a path defined.


urlpatterns = [
    path('', views.contact),
    path('basic_calculator/add/', AddView.as_view(), name='add'),
    path('basic_calculator/sub/', SubView.as_view(), name='sub'),
    path('basic_calculator/div/', DivView.as_view(), name='div'),
    path('basic_calculator/multi/', MultiView.as_view(), name='multi')
    # path('add/', AddView.as_view(), name='add'),
    # path('sub/', SubView.as_view(), name='sub'),
    # path('div/', DivView.as_view(), name='div'),
    # path('multi/', MultiView.as_view(), name='multi')
]

