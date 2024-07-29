from rest_framework import serializers
from django.contrib.auth.models import User
from main.models import TodoList, TodoCategory, TodoItem
from django.contrib.auth import authenticate


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data['email']
        )
        return user


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect Credentials")


class TodoListSerializer(serializers.ModelSerializer):

    class Meta:
        model = TodoList
        fields = ['id', 'title', 'description', 'created', 'updated']


class TodoListCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoList
        fields = ['id', 'title', 'description', 'created', 'updated']

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['user'] = user
        return TodoList.objects.create(**validated_data)


class TodoCategorySerializer(serializers.ModelSerializer):
    # user = UserSerializer(read_only=True)

    class Meta:
        model = TodoCategory
        fields = ['id', 'title', 'description', 'created', 'updated']

    def create(self, validated_data):
        user = User.objects.get(id=validated_data['user_id'])
        validated_data['user'] = user
        return TodoCategory.objects.create(**validated_data)


class TodoItemSerializer(serializers.ModelSerializer):
    todo_list = TodoListSerializer(read_only=True)

    class Meta:
        model = TodoItem
        fields = ['id', 'todo_list' ,'title', 'description', 'created', 'updated']
