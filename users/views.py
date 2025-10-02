# users/views.py
from rest_framework import generics, permissions
from .models import User
from .serializers import UserSerializer


# Register (anyone can create an account)
class UserRegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]


# List users (only admin can see all users)
class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]


# Retrieve, Update, Delete user
class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    # Ensure normal users can only access their own profile
    def get_queryset(self):
        user = self.request.user
        if user.is_admin:  # Admins can see all users
            return User.objects.all()
        return User.objects.filter(id=user.id)
