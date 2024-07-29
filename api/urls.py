from django.urls import path
from .views import (RegisterView, UserDetailView, UserDetailView, 
                    TodoItemView, TodoListView, CreateTodoList, TodoCategoryView, TodoItemView,
                    CreateTodoList, TodoItemsByListView)
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView





schema_view = get_schema_view(
    openapi.Info(
        title="Todo API",
        default_version='v1',
        description="Your API description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@yourapi.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    authentication_classes=[],
)



app_name = 'api'

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('user/', UserDetailView.as_view(), name='user'),
    path('todo/lists/', TodoListView.as_view(), name='get_todo_lists'),
    path('todo/categories/', TodoCategoryView.as_view(), name='get_todo_categories'),
    path('todo/items/', TodoItemView.as_view(), name='get_todo_items'),
    path('get-todo-items-by-list/<int:pk>/', TodoItemsByListView.as_view(), name='get_todo_items_by_list'),

    path('create-todo-list/', CreateTodoList.as_view(), name='create_todo_list'),


    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('swagger/', SpectacularSwaggerView.as_view(url_name='api:schema'), name='swagger-ui'),
    path('redoc/', SpectacularRedocView.as_view(url_name='api:schema'), name='redoc'),
]
