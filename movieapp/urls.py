from django.urls import path
from .import views
app_name='movieapp'
urlpatterns = [
    path('',views.index,name='index.html'),
    path('adding/',views.adding,name='adding'),
    path('movie/<int:movie_id>/',views.detail,name='detail'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete')
]