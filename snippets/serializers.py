from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES
from hotel_finder.models import (
    PerfectHotel,
    TopDestination,
    USP,
    DiscoverTheWorld,
    VisitorExp,
)


class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')

    class Meta:
        model = Snippet
        fields = ['url', 'id', 'highlight', 'owner',
                  'title', 'code', 'linenos', 'language', 'style']


class UserProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'url' , 'email', 'username', 'password']

        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        """Create and return a new user"""

        user = User(
            email=validated_data['email'],
            username=validated_data['username'],
        )

        user.set_password(validated_data['password'])
        user.save()
        return user


class PerfectHotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerfectHotel
        fields = ['url', 'star', 'img']


class TopDestinationSerializer(serializers.ModelSerializer):
    class Meta:
        model = TopDestination
        fields = ['wifi', 'breakfast',
                  'balcony', 'bathroom',
                  'content', 'img',
                  'name', 'star',
                  'price',]


class USPSerializer(serializers.ModelSerializer):
    class Meta:
        model = USP
        fields = ['name', 'desc', 'img']


class DiscoverWorldSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiscoverTheWorld
        fields = ['img', 'flag', 'subname', 'catename', 'numpro']


class VisitorExpSerializer(serializers.ModelSerializer):
    class Meta:
        model = VisitorExp
        fields = ['img', 'name', 'firm', 'context',]


# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     snippets = serializers.HyperlinkedRelatedField(many=True, view_name='snippet-detail', read_only=True)
#
#     class Meta:
#         model = User
#         fields = ['url', 'id', 'username', 'snippets', 'email', 'password']
#
#         extra_kwargs = {'password': {'write_only': True}}


# class SnippetSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(required=False, allow_blank=True, max_length=100)
#     code = serializers.CharField(style={'base_template': 'textarea.html'})
#     linenos = serializers.BooleanField(required=False)
#     language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
#     style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')



# class SnippetSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Snippet
#         fields = ['id', 'title', 'code', 'linenos', 'language', 'style']
#         owner = serializers.ReadOnlyField(source='owner.username')
#
#     def create(self, validated_data):
#         """
#         Create and return a new `Snippet` instance, given the validated data.
#         """
#         return Snippet.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         """
#         Update and return an existing `Snippet` instance, given the validated data.
#         """
#         instance.title = validated_data.get('title', instance.title)
#         instance.code = validated_data.get('code', instance.code)
#         instance.linenos = validated_data.get('linenos', instance.linenos)
#         instance.language = validated_data.get('language', instance.language)
#         instance.style = validated_data.get('style', instance.style)
#         instance.save()
#         return instance
#
# class UserSerializer(serializers.ModelSerializer):
#     snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())
#
#     class Meta:
#         model = User
#         fields = ['id', 'username', 'snippets']