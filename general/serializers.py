from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from general.models import Women

# class WomenModel:
#     def __init__(self, title, content) -> None:
#         self.title = title
#         self.content = content


class WomenSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Women
        fields = ("__all__")

    # title = serializers.CharField(max_length=255)
    # content = serializers.CharField()
    # time_create = serializers.DateTimeField()
    # time_update = serializers.DateTimeField()
    # is_published = serializers.BooleanField(default=True)
    # cat_id = serializers.IntegerField()

    # def create(self, validated_data):
    #     return Women.objects.create(**validated_data)

    # def update(self, instance, validated_data):
    #     instance.title = validated_data.get('title', instance.title)
    #     instance.content = validated_data.get('content', instance.content)
    #     instance.time_update = validated_data.get('time_update', instance.time_update)
    #     instance.is_published = validated_data.get('is_published', instance.is_published)
    #     instance.cat_id = validated_data.get('cat_id', instance.cat_id)
    #     instance.save()
    #     return instance
# def encode():
#     model = WomenModel('angel jolly', 'Content: Angela jolly')
#     model_sr = WomenSerializer(model)
#     print(model_sr)
#     json = JSONRenderer().render(model_sr.data)
#     print(json)
