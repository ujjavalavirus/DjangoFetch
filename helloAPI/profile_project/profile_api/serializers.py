from rest_framework import serializers
from . import models
import json

class HelloSerializer(serializers.Serializer):
	"""serializers a name field for testing our APIView."""

	name = serializers.CharField(max_length=10)


class UserProfileSerializer(serializers.ModelSerializer):
	"""A serializer for our user profile objects."""

	class Meta:
		model = models.UserProfile
		fields = ('id', 'email', 'name', 'password')
		extra_kwargs = {'password': {'write_only': True}}


	def create(self, validated_data):
		"""Create & return a new user."""

		user = models.UserProfile(
			email = validated_data['email'],
			name = validated_data['name']
		)

		user.set_password(validated_data['password'])
		user.save()

		return user	


class NewsRssFeedSerializer(serializers.ModelSerializer):
	"""A serializer for profile feed items"""

	class Meta:
		model = models.NewsRssFeed
		fields = ('id','title','description','newslink','imagelink','newsCategory','newsDate','created_on')
