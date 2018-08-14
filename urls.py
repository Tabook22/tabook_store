from django.urls import path
from . import views
app_name='tabook_store'

urlpatterns=[
    path('slist/',views.slist_view,name='slist')
]