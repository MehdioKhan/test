from django.db import connections


def call_function(function_name,*args):

    with connections['data'].cursor() as cursor:
        cursor.callproc(function_name,list(args))
        data = cursor.fetchall()[0][0]
        return data

