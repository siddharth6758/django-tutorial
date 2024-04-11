from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from app.models import *
from app.serializers import *
from rest_framework.views import APIView

#ApiView is a compact way of defining all methods i.e GET,PUT,POST as a view
class PersonAPIview(APIView):
    def get(self,req):
        person_obj = Person.objects.all()
        serializer = PersonSerializer(person_obj,many=True)
        return Response({           
            'data':serializer.data
        })
       
        
    def post(self,req):
        serializer = PersonSerializer(data=req.data)
        if not serializer.is_valid():
            return Response({'error':serializer.errors})
        serializer.save()
        return Response({
            'data':serializer.data,
            'message':'data inserted successfully'
        })
        
        
    def put(self,req):
        #for updating a particular id, the id is also required in json
        try:
            person = Person.objects.get(id=req.data['id'])
            serializer = PersonSerializer(person,data=req.data)
            if not serializer.is_valid():
                return Response({'error':serializer.errors})
            serializer.save()
        except Exception as e:
            return Response({
                'Exception':e
            })
        return Response({
            'data':serializer.data,
            'message':'data updated successfully'
        })
    
    
    def patch(self,req):
        try:
            person = Person.objects.get(id=req.data['id'])
            serializer = PersonSerializer(person,data=req.data,partial=True)
            if not serializer.is_valid():
                return Response({'error':serializer.errors})
            serializer.save()
        except Exception as e:
            return Response({
                'Exception':e
            })
        return Response({
            'data':serializer.data,
            'message':'data updated successfully'
        })        


    def delete(self,req):
        try:
            person = Person.objects.get(id=req.data['id'])
            person.delete()
        except Exception as e:
            return Response({
                'Exception':e
            })
        return Response({
            'message':'data deleted successfully'
        })        


@api_view(['GET'])
def company(req):
    comp = Company.objects.all()
    serializer = CompanySerializer(comp,many=True)
    return Response({           
        'data':serializer.data
    })

#token authenticator vs JWT token authenticator-JWT provides more security by periodically refreshing the tokens generated so it cannot be accessed easily by any unauthorised access


#converts the normal function into an api based function, without the api_view this request is a wsgi request while with api_view() it becomes a rest_frameworkAPI request
# @api_view(['GET'])
# def home(req):   
#     person_obj = Person.objects.all()
#     #serialize the queryset data into json using serializer, set many=True as multiple data is being fetched
#     serializer = PersonSerializer(person_obj,many=True)
#     #sends response as a json   
#     return Response({           
#         'data':serializer.data
#     })
    
# @api_view(['POST'])
# def add_person(req):
#     #to add data through serializer, converts json data to object
#     serializer = PersonSerializer(data=req.data)
#     #check whether is valid or not, use serializer.errors to show the errors occured
#     if not serializer.is_valid():
#         return Response({'error':serializer.errors})
#     #save the data if no error
#     serializer.save()
#     return Response({
#         'data':serializer.data,
#         'message':'data inserted successfully'
#     })
    

# #put allows you to update data, but all fields of the json should be mentioned
# #patch allows you to update data, only the updating fields of the json should be mentioned,for patch method all those fields present in the validate() of serializer should be present else KEY_ERROR occurs
# @api_view(['PUT','PATCH'])
# def update_person(req,id):
#     #to update data through serializer
#     try:
#         person = Person.objects.get(id=id)
#         #with partial=True it allows us to update the record by only providing the changes
#         serializer = PersonSerializer(person,data=req.data,partial=True)
#         if not serializer.is_valid():
#             return Response({'error':serializer.errors})
#         serializer.save()
#     except Exception as e:
#         return Response({
#             'Exception':e
#         })
#     return Response({
#         'data':serializer.data,
#         'message':'data updated successfully'
#     })

# @api_view(['DELETE'])
# def delete_person(req,id):
#     try:
#         person = Person.objects.get(id=id)
#         person.delete()
#     except Exception as e:
#         return Response({
#             'Exception':e
#         })
#     return Response({
#         'message':'data deleted successfully'
#     })
    