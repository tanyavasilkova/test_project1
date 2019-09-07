"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from entry.views import NoteList, NoteDetail, NoteCreate
from categories.views import CategoryList, CategoryDetail, CategoryCreate, CategoryUpdate



urlpatterns = [
    path('admin/', admin.site.urls),

    path('note/', NoteList.as_view(), name='note_list_view'),
    path('note/<int:pk>/', NoteDetail.as_view(), name='note_detail_view'),
    path('note/create', NoteCreate.as_view(), name='note_create_view'),

    path('category/', CategoryList.as_view(), name='category_list_view'),
    path('category/<int:pk>/', CategoryDetail.as_view(), name='category_detail_view'),
    path('category/create/', CategoryCreate.as_view(), name='category_create_view'),
    path('category/update/<int:pk>', CategoryUpdate.as_view(), name='category_update_view'),






]
