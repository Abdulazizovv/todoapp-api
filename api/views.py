from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from .serializers import (
    UserSerializer, RegisterSerializer, TodoListSerializer, TodoCategorySerializer, TodoItemSerializer, TodoListCreateSerializer
)
from rest_framework.views import APIView
from main.models import TodoList, TodoCategory, TodoItem
from rest_framework.permissions import IsAuthenticated


# For registering a new user
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        refresh = RefreshToken.for_user(user)
        response_data = serializer.data
        response_data['refresh'] = str(refresh)
        response_data['access'] = str(refresh.access_token)

        return Response(response_data, status=status.HTTP_201_CREATED)


# For testing user authentication
class UserDetailView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        user = request.user
        serializer = self.get_serializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)


# For getting user details
class UserDetailView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer

    def get(self, request):
        user = request.user
        data = self.serializer_class(user).data
        return Response(data, status=status.HTTP_200_OK)


# For getting todo lists
class TodoListView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TodoListSerializer

    def get(self, request):
        user = request.user
        todo_lists = user.todolist_set.all()
        data = self.serializer_class(todo_lists, many=True).data
        if not data:
            return Response({"detail": "No todo lists found"}, status=status.HTTP_204_NO_CONTENT)
        return Response(data, status=status.HTTP_200_OK)


# For creating a todo list
class CreateTodoList(generics.CreateAPIView):
    serializer_class = TodoListCreateSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        data = request.data.copy()
        serializer = self.get_serializer(data=data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


# For getting todo categories
class TodoCategoryView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TodoCategorySerializer

    def get(self, request):
        user = request.user
        todo_categories = user.todocategory_set.all()
        data = self.serializer_class(todo_categories, many=True).data
        if not data:
            return Response({"detail": "No todo categories found"}, status=status.HTTP_204_NO_CONTENT)
        return Response(data, status=status.HTTP_200_OK)


# For creating todo categories
class TodoCategoryCreateView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TodoCategorySerializer

    def post(self, request):
        pass


# For getting todo items
class TodoItemView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TodoItemSerializer

    def get(self, request):
        user = request.user
        todo_items = user.todoitem_set.all()
        data = self.serializer_class(todo_items, many=True).data
        if not data:
            return Response({"detail": "No todo items found"}, status=status.HTTP_204_NO_CONTENT)
        return Response(data, status=status.HTTP_200_OK)


# For getting todo items by todo list
class TodoItemsByListView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TodoItemSerializer

    def get(self, request, pk):
        user = request.user
        todo_list = user.todolist_set.filter(pk=pk).first()
        if not todo_list:
            return Response({"detail": "Todo list not found"}, status=status.HTTP_404_NOT_FOUND)
        todo_items = todo_list.todoitem_set.all()
        data = self.serializer_class(todo_items, many=True).data
        if not data:
            return Response({"detail": "No todo items found"}, status=status.HTTP_204_NO_CONTENT)
        return Response(data, status=status.HTTP_200_OK)
