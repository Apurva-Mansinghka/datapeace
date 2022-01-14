from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, RetrieveUpdateDestroyAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import LimitOffsetPagination

from datapeaceApp.serializers import UserSerializer
from datapeaceApp.models import User

class UsersPagination(LimitOffsetPagination):
    default_limit = 5
    max_limit = 100

class UserList(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filter_fields = ('id',)
    search_fields = ('firstName','lastName',)
    pagination_class = UsersPagination


class UserCreate(CreateAPIView):
    serializer_class = UserSerializer
    def create(self, request, *args, **kwargs):
        try:
            age = request.data.get('age')
            if age is not None and float(age) <= 0.0:
                raise ValidationError({ 'age': 'Must be above 10' })
        except ValueError:
            raise ValidationError({ 'age': 'A valid number is required' })
        return super().create(request, *args, **kwargs)

class UserDestroy(DestroyAPIView):
    queryset = User.objects.all()
    lookup_field = 'id'

    def delete(self, request, *args, **kwargs):
        user_id = request.data.get('id')
        response = super().delete(request, *args, **kwargs)
        if response.status_code == 204:
            from django.core.cache import cache
            cache.delete('user_data_{}'.format(user_id))
        return response


class UserUpdate(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    lookup_field = 'id'
    serializer_class = UserSerializer

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        if response.status_code == 200:
            from django.core.cache import cache
            user = response.data
            cache.set('user_data_{}'.format(user['id']), {
                'firstName': user['firstName'],
		'lastName': user['lastName'],
	#	'company': user['company'],
                'age': user['age'],
	#	'city': user['city'],
	#	'state': user['state'],
	#	'zip': user['zip'],
	#	'email': user['email'],
	#	'web': user['web'],                
            })
        return response
