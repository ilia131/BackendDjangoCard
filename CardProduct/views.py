from rest_framework.views import APIView
from .serializers import CardSerializer
from .models import Card
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q
from rest_framework import generics , mixins , viewsets
from rest_framework.parsers import MultiPartParser, FormParser  

# Create your views here.



# class CardViewSet(APIView):
    
#         def get(self, request):
#          queryset = Card.objects.all()
#          serializer = CardSerializer(queryset, many=True)
#          return Response(serializer.data)
 
#         def post(self, request):  
#            serializer = CardSerializer(data=request.data)  
#            if serializer.is_valid():  
#               serializer.save()  
#               return Response(serializer.data, status=status.HTTP_201_CREATED)  
#            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  


class CardViewSet(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)





   
class CardViewSetDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    queryset =Card.objects.all()
    serializer_class = CardSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)








# class CardViewSetDetail(APIView):
#       # parser_classes = (MultiPartParser, FormParser )

#       def get_object(self, pk):
#          try:
#              return Card.objects.get(pk=pk)
#          except Card.DoesNotExist:
#             raise Http404
#       def get(self, request, pk, format=None):
#         card = self.get_object(pk)
#         serializer = CardSerializer(card)
#         return Response(serializer.data)
#       def put(self, request, pk, format=None):
#         card = self.get_object(pk)
#         serializer = CardSerializer(card, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
      
#       def delete(self, request, pk, format=None):
#         card = self.get_object(pk)
#         card.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


class CardViewSetSearch(viewsets.GenericViewSet, mixins.ListModelMixin):
          queryset = Card.objects.all()
          serializer_class = CardSerializer
          
          def get_queryset(self):
           text = self.request.query_params.get('query', None)
           if not text: 
             return self.queryset
         
           return self.queryset.filter(Q(title__icontains=text) | Q(description__icontains=text))
     
     
class CardViewSetDetailsfind(viewsets.GenericViewSet, mixins.ListModelMixin):
          queryset = Card.objects.all()
          serializer_class = CardSerializer
          
          def get_queryset(self):
           text = self.request.query_params.get('query', None)
           if not text: 
             return self.queryset
         
           return self.queryset.filter(Q(id=text))