from . import views
from django.urls import path

from . import views
urlpatterns = [
    # path('normaluser/', views.NormalUser, name="normaluser"),
    #here id comming from views.py of BlogApp Login class object user and it will store in this id
    #taking int type of url argument and it will pass to RegUser of NormalUser app view
    path('usr/<int:id>', views.RegUser.as_view(), name='userhome'),
    # path('usr/<int:id><str:username>', views.RegUser.as_view(), name='userhome'),
    path('usr/<int:id>/new_blog', views.NewBlog.as_view(), name='new_blog'),
    path('usr/<int:id>/my_blog', views.MyBlog.as_view(), name='my_blog'),
    path('usr/<int:id>/all_blog', views.AllBlogs.as_view(), name='all_blog'),
    path('usr/<int:id>/all_categories', views.AllCategory.as_view(), name='all_categories'),
    path('usr/<int:id>/new_category', views.NewCategory.as_view(), name='new_category'),
    path('usr/<int:id>/edit_category/<int:cid>', views.EditCategory.as_view(), name='edit_category'),
    path('usr/<int:id>/delete_category/<int:cid>', views.DeleteCategory.as_view(), name='delete_category'),

]
