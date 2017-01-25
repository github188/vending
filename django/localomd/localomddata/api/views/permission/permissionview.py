import os
from threading import Thread

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response


@api_view(['GET'])
@permission_classes((IsAdminUser,))
def adminPermView(request, format=None):
    content = {'detail':'OK'}
    return Response(content)

@api_view(['GET'])
def shutdownView(request, format=None):
    shutdownOps = ShutdownOps(request.data)
    shutdownOps.setDaemon(True)
    shutdownOps.start()
    return Response({'detail':'OK'})

class ShutdownOps(Thread):
    def __init__(self, requestData):
        Thread.__init__(self)
        self.operateName = requestData['operateName']

    def run(self):
        if(self.operateName == "shutdown"):
            os.system("sudo shutdown ")
        if(self.operateName == "restart"):
            os.system("sudo restart")