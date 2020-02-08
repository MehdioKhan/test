from rest_framework.views import APIView
from rest_framework.response import Response
from .functions import call_function


class Status(APIView):

    def get(self,request,tbl_num,format=None):
        data=call_function('status',tbl_num)
        return Response(data)


class Path(APIView):

    def get(self,request,tbl_num,device_id,format=None):
        data = call_function('path',tbl_num,device_id)
        return Response(data)


class Stops(APIView):
    def get(self,request,tbl_num,device_id,format=None):
        data = call_function('stops',tbl_num,device_id)
        return Response(data)
