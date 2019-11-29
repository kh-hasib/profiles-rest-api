from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    """Test API VIEW """
    def get(self, reequest, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'It is similar to traditional django view',
            'Gives you the most control over your application logic',
            'It is mapped manually to URLs',
        ]
        return Response({'message':'Hi there', 'an_apiview':an_apiview})
