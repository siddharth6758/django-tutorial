#Serializer converts the backend data into json format for the frontend
#Allows to convert complex datatypes such as Querysets and Objects into primitive python 
#python datatype that is inturn converted to json,xml etc.
'''There are 2 types of serializers:
    -HyperLinkedModelSerializer serializer
    -Model serializer
    '''

#all database related logic is implemented in models or serializers rather than implementing in view

from rest_framework import serializers
from app.models import Person,Company
from django.contrib.auth.models import User

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'
        #to exclude particular fields, you can either use fields or exclude
        # exclude = ['id']
        
    #defining a validation method to validate the data
    def validate(self,data):
        if data['age'] >= 120:
            raise serializers.ValidationError({
                'error':'Age not valid'
            })
        if any([i.isdigit() for i in data['name']]):
            raise serializers.ValidationError({
                'error': 'Name contains Digit'
            })
        return data
    

class CompanySerializer(serializers.ModelSerializer):
    #this is the foreign key in the Company Model, to initialize the foreign key(fetch data of foreign key), column_name = TableNameSerializer(), i.e. it looks for the field names specified by the table of the foreign key. Example if person table has fields = ['id','name','age'], then it this would show only these fields
    person_id = PersonSerializer()
    class Meta:
        model = Company
        fields = '__all__'
        #depth is used to define the depth of information shown by the foreign key
        # depth = 1
        

#for token authorization we need to serialize the user data/user credentials
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','password']
    
    #overriding the create method of user.objects.create() so the password stored is hashed
    def create(self,data):
        user = User.objects.create(username=data['username'])
        user.set_password(data['password'])
        user.save()
        return user