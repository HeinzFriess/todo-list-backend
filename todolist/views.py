from django.shortcuts import render
from rest_framework.authtoken.views import ObtainAuthToken, APIView
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from todolist.models import TodoItem
from todolist.serializers import TodoItemSerializer


# Create your views here.

class TodoItemView(APIView):
    """
    View to list all todos in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    #authentication_classes = [authentication.TokenAuthentication]
    permission_classes = []

    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        todos = TodoItem.objects.all()
        serializer = TodoItemSerializer(todos, many=True)
        return Response(serializer.data)

class loginview(ObtainAuthToken):
    
    def post(self, request): #, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                    context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
             'user_id': user.pk,
             'email': user.email
            })
