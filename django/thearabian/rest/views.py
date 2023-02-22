from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest.models import country
from rest_framework import permissions, generics, authentication
from .serializers import UserSerializer, GroupSerializer, CountrySerializer
from rest_framework.permissions import DjangoModelPermissions


class CountryDetailAPIView(generics.RetrieveAPIView):
    queryset = country.objects.all()
    serializer_class = CountrySerializer
    permission_classes = [permissions.AllowAny]
    authentication_classes = [authentication.SessionAuthentication,
                              authentication.TokenAuthentication]


country_detail_view = CountryDetailAPIView.as_view()


class CountryListCreateAPIView(generics.ListCreateAPIView):
    queryset = country.objects.all()
    serializer_class = CountrySerializer
    permission_classes = (DjangoModelPermissions)
    authentication_classes = [authentication.SessionAuthentication,
                              authentication.TokenAuthentication]


country_list_create_view = CountryListCreateAPIView.as_view()


class CountryUpdateAPIView(generics.UpdateAPIView):
    queryset = country.objects.all()
    serializer_class = CountrySerializer
    permission_classes = [permissions.AllowAny]
    authentication_classes = [authentication.SessionAuthentication,
                              authentication.TokenAuthentication]


country_update_view = CountryUpdateAPIView.as_view()


class CountryDestroyAPIView(generics.DestroyAPIView):
    queryset = country.objects.all()
    serializer_class = CountrySerializer
    permission_classes = [permissions.AllowAny]
    authentication_classes = [authentication.SessionAuthentication,
                              authentication.TokenAuthentication]


country_destroy_view = CountryDestroyAPIView.as_view()
