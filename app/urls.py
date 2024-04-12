from django.urls import path
import app.views as av
from rest_framework.authtoken import views

urlpatterns = [
    # path('',av.home,name='home'),
    # path('person/',av.add_person,name='add_person'),
    # path('person/<int:id>',av.update_person,name='update_person'),
    # path('delete-person/<int:id>',av.delete_person,name='delete_person'),
    path('company/',av.company,name='company'),
    path('person/',av.PersonAPIview.as_view(),name='person'),
    path('usertokens/',av.UserAPIview.as_view(),name='userview'),
    path('api-token-auth/', views.obtain_auth_token),
]
