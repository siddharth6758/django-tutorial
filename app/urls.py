from django.urls import path
import app.views as av

urlpatterns = [
    # path('',av.home,name='home'),
    # path('person/',av.add_person,name='add_person'),
    # path('person/<int:id>',av.update_person,name='update_person'),
    # path('delete-person/<int:id>',av.delete_person,name='delete_person'),
    path('company/',av.company,name='company'),
    path('person/',av.PersonAPIview.as_view(),name='person'),
]
