from django.utils.timesince import timesince
from rest_framework import serializers

from accounts.api.serializers import UserDisplaySerializer
from tweets.models import Tweet



class ParentTweetModelSerializer(serializers.ModelSerializer):
	user = UserDisplaySerializer(read_only=True)  #write_only
	date_display = serializers.SerializerMethodField()
	timesince = serializers.SerializerMethodField()
	likes = serializers.SerializerMethodField()
	did_like = serializers.SerializerMethodField()
	
	class Meta:
		model = Tweet
		fields = [
			'id',
			'user',
			'content',
			'timestamp',
			'date_display',
			'timesince',
			'likes',
			'did_like',


		]


	def get_did_like(self, obj):
		request = self.context.get("request")
		user = request.user
		if user.is_authenticated():
			if user in obj.liked.all():
				return True
		return False

	def get_likes(self, obj):
		return obj.liked.all().count()

	def get_date_display(self, obj):
		return obj.timestamp.strftime("%b %d, %Y at %I : %M %p")

	def get_timesince(self, obj):
		return timesince(obj.timestamp) + " ago "


class TweetModelSerializer(serializers.ModelSerializer):
	user = UserDisplaySerializer(read_only=True)  #write_only
	date_display = serializers.SerializerMethodField()
	timesince = serializers.SerializerMethodField()
	parent = ParentTweetModelSerializer(read_only=True)
	likes = serializers.SerializerMethodField()
	did_like = serializers.SerializerMethodField()
	
	class Meta:
		model = Tweet
		fields = [
			'id',
			'user',
			'content',
			'timestamp',
			'date_display',
			'timesince',
			'parent',
			'likes',
			'did_like',
			'reply',


		]

	def get_did_like(self, obj):
		request = self.context.get("request")
		user = request.user
		if user.is_authenticated():
			if user in obj.liked.all():
				return True
		return False



	def get_likes(self, obj):
		return obj.liked.all().count()

	def get_date_display(self, obj):
		return obj.timestamp.strftime("%b %d, %Y at %I : %M %p")

	def get_timesince(self, obj):
		return timesince(obj.timestamp) + " ago "
			