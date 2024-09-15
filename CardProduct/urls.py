from .views import CardViewSet , CardViewSetDetail , CardViewSetSearch ,CardViewSetDetailsfind
from django.urls import path , include
from rest_framework import routers


router = routers.DefaultRouter()

router.register('search',CardViewSetSearch , basename='search')
router.register('detail',CardViewSetDetailsfind , basename='detail')



urlpatterns = [
    path('all/', CardViewSet.as_view()),
    path('all/<int:pk>/', CardViewSetDetail.as_view()),  
    path('', include(router.urls)), 
] 
