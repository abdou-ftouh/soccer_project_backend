from os import defpath
from rest_framework import serializers
from .models import Location, Reservation, Stadium, User

class UserSerializer(serializers.ModelSerializer):
 
    # reservations = serializers.HyperlinkedRelatedField(
    #     view_name='reservation_detail',
    #     many=True,
    #     read_only=True
    # )
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email','phone', 'gendre','reservations',)

        depth =1


class StadiumSerializer(serializers.ModelSerializer):

    # reservations = serializers.HyperlinkedRelatedField(
    #     view_name='reservation_detail',
    #     many=True,
    #     read_only=True
    # )
  
    # location = serializers.HyperlinkedRelatedField(
    #     view_name='location_detail',
    #     read_only=True,
    # )
    
    location = serializers

    class Meta:
        model = Stadium
        fields = ('id','location','name','photo','description','address', 'zip','reservations')

       

       

class LocationSerializer(serializers.ModelSerializer):

    # stadiums = serializers.HyperlinkedRelatedField(
    #     view_name='stadium-detail',
    #     many=True,
    #     read_only=True
    # )
    class Meta:
        model = Location
        fields = ('id', 'city', 'stadiums',)

        depth =1
     

class ReservationSerializer(serializers.ModelSerializer):

    # user = serializers.HyperlinkedRelatedField(
    #     view_name='user_detail',
    #     read_only=True,
    # )

    # stadium = serializers.HyperlinkedRelatedField(
    #     view_name='stadium_detail',
    #     read_only=True,
    # )

    user = serializers
    stadium = serializers


    class Meta:
        model = Reservation
        fields = ('id','user','stadium','reserved_start_date', 'reserved_end_date',)

     

      

