from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from . import serializers
from . import models
from rest_framework  import status
from . import permissions
from rest_framework.authentication import TokenAuthentication
import feedparser
import json

# Create your views here.

"""Hello APIView Class"""
class HelloApiView(APIView):
	"""Test API View."""

	serializer_class = serializers.HelloSerializer


	def get(self, request, format=None):
		"""Returns a list of APIView Features."""

		url = 'http://www.haribhoomi.com/rss/feed.aspx?catid=3'
		feeds = feedparser.parse(url)
		#serializer =  serializers.NewsRssFeedSerializer(data=feeds.entries[0])
		#serializer.save();
		#return feeds.entries[0].title

		return Response({'message': 'Hello!','api_view': feeds.entries[0].title})


	def post(self, request):
		"""Create a hello message with our name. """

		serializer =  serializers.HelloSerializer(data=request.data)

		if serializer.is_valid():
			name = serializer.data.get('name')
			message = 'Hello {0}'.format(name)
			return Response({'message': message})
		else:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


	def put(self, request, pk=None):
		"""Handles updating on object."""

		return Response({'method': 'put'})

	def patch(self, request, pk=None):
		"""Patch request, only update fields provided in the request"""

		return Response({'method': 'patch'})

	def delete(self, request, pk=None):
		"""Delete an object"""

		return Response({'method': 'Delete'})	



class HelloViewSet(viewsets.ViewSet):
	"""Test API ViewSet."""

	serializer_class = serializers.HelloSerializer

	def list(self, request):
		"""Return a hello message."""

		a_viewset = [
			'Uses actions (list, create, update, partical update, Destroy)',
			'Automatically maps to URLs using Routers',
			'Provides more functionality with less code.',
		]

		url = 'http://www.haribhoomi.com/rss/feed.aspx?catid=3'
		feeds = feedparser.parse(url)

		return Response({'message': 'Hello!', 'a_viewset': feeds.entries[0].title})

	def create(self, request):
		"""Create a new hello message."""

		serializer = serializers.HelloSerializer(data=request.data)

		if serializer.is_valid():
			name = serializer.data.get('name')
			message = 'Hello {0}'.format(name)
			return Response({'message': message})
		else: 
			return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

	def retrieve(self, request, pk=None):
		"""Handles getting an object by its ID."""

		return Response({'http_method': 'GET'})


	def update(self, request, pk=None):
		"""Handles updating an object."""

		return Response({'http_method': 'PUT'})

	
	def partial_update(self, request, pk=None):
		"""Handles updating part of an object"""

		return Response({'http_method': 'PATCH'})	


	def destroy(self, request, pk=None):
		"""Handles removing an object."""

		return Response({'http_method': 'DELETE'})



class UserProfileViewSet(viewsets.ModelViewSet):
	"""Handling creating, creating & updating profiles."""

	serializer_class = serializers.UserProfileSerializer
	queryset = models.UserProfile.objects.all()
	authentication_classes = (TokenAuthentication,)
	permission_classes = (permissions.UpdateOwnProfile,)


class NewsRssFeedViewSet(viewsets.ModelViewSet):
	"""News Feed handle"""
	#models.NewsRssFeed.objects.all().delete()
	serializer_class = serializers.NewsRssFeedSerializer
	queryset = models.NewsRssFeed.objects.all()

	
	def list(self, request):
		#url = 'http://www.haribhoomi.com/rss/feed.aspx?catid=3'
		#feeds = feedparser.parse(url)
		newsFeedList = []
				
		#for item in feeds.entries:
		newsFeedObject = {}
		newsFeedObject['title'] = 'item' #item.title
		newsFeedObject['description'] = 'description' #item.description
		newsFeedObject['newslink'] = 'link' #item.link
		newsFeedObject['imagelink'] = 'ssss'
		newsFeedObject['newsCategory'] = 'category' #item.category
		newsFeedObject['newsDate'] = 'ssd'
		newsFeedObject['created_on'] = 'now' 
		newsFeedList.append(newsFeedObject)
		serializer = serializers.NewsRssFeedSerializer(data=newsFeedObject)
		if serializer.is_valid():
			serializer.save()
		data = models.NewsRssFeed.objects.all()
		serializernew = serializers.NewsRssFeedSerializer(data, many=True)
		return Response(serializernew.data)

	#def get_queryset(self):
    		#return models.NewsRssFeed.objects.all()"""









