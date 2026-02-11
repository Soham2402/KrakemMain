# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status


# class Project(APIView):

#     def validate_request_data(data: dict) -> str:
        
#     def post(self, request):
#         try:
            
#             data: dict = request.data

#             return Response(data=data, status=status.HTTP_200_OK)
#         except Exception as e:
#             return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR, data={"error":str(e)})
        
