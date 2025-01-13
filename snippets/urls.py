from django.urls import path
from snippets import views


urlpatterns = [
    path('snippets/', view=views.snippet_list),
    path('snippets/<int:pk>/', view=views.snippet_detail),
]