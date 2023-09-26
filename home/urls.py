from django.urls import path,include
from home import views
urlpatterns = [
    path("",views.home),
    path("save",views.save),
    path('show2',views.show2),
    path('delete/<int:id>',views.delete),
    path('update/<int:id>',views.update)

]