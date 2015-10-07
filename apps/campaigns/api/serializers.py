from rest_framework import serializers
from photologue.models import Photo

from apps.campaigns.models import Campaign
from apps.metas.models import CampaignCircle
from apps.api.fields import Base64ImageField, ModelPropertyField


class CampaignSerializer(serializers.ModelSerializer):
    preview_image_url = serializers.SerializerMethodField()
    claimed_coupons_sum = serializers.SerializerMethodField()
    is_paid = ModelPropertyField()

    class Meta:
        model = Campaign
        exclude = ['image']

    def get_preview_image_url(self, obj):
        if obj.image:
            return obj.image.get_preview_url()
        else:
            return ''

    def get_claimed_coupons_sum(self, obj):
        return obj.coupons.claimed().coupons_value_sum()


class CreateCampaignSerializer(serializers.ModelSerializer):
    image = Base64ImageField(required=False)
    service_charges = serializers.DecimalField(max_digits=20, decimal_places=4, required=False)
    taxes = serializers.DecimalField(max_digits=20, decimal_places=4, required=False)
    circles = serializers.ListField(child=serializers.IntegerField(), required=False)

    class Meta:
        model = Campaign

    def create(self, validated_data):
        image = validated_data.get('image', None)
        if image:
            image = Photo.objects.create(
                image=image, title=image.name,
                slug=image.name,
            )
        i = validated_data
        service_charges = i.pop('service_charges', None)
        taxes = i.pop('taxes', None)
        circles = i.pop('circles', None)
        i['image'] = image
        campaign = Campaign.objects.create(**i)
        campaign.set_invoice(
                amount=campaign.budget,
                service_charges=service_charges,
                taxes=taxes
            )
        if circles and len(circles):
            for c in circles:
                print c
                CampaignCircle.objects.create(campaign=campaign, circle_id=c)
        return campaign

    def update(self, instance, validated_data):
        i = validated_data
        image = validated_data.get('image', None)
        if image:
            image = Photo.objects.create(
                image=image, title=image.name,
                slug=image.name,
            )
            i['image'] = image
        service_charges = i.pop('service_charges', None)
        taxes = i.pop('taxes', None)
        circles = set(i.pop('circles', None))
        # disabling the circles that are not part of 'circles'
        campaign_circles = CampaignCircle.objects.filter(campaign=instance) \
            .exclude(circle_id__in=circles).update(is_active=False)
        if len(circles):
            for c in circles:
                CampaignCircle.objects.get_or_create(
                    campaign=instance,
                    circle_id=c
                ).update(is_active=True)
        for attr, value in i.items():
            setattr(instance, attr, value)
        instance.save()
        return instance
