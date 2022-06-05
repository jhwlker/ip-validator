import time
from concurrent import futures

import grpc

from proto.grpc_ip import ip_pb2_grpc as ip_pb2_grpc, ip_pb2 as ip_pb2
from service import ip_validator


class IPValidatorServicer(ip_pb2_grpc.IPValidatorServicer):

    def ValidateIP(self, request, context):
        ip = request.ipAddress
        countries = request.countries
        response = ip_pb2.IPResponse(valid=ip_validator.validate_ip_address(ip, countries))
        return response


server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

ip_pb2_grpc.add_IPValidatorServicer_to_server(IPValidatorServicer(), server)

print('Starting server. Listening on port 8000')
server.add_insecure_port('[::]:8000')
server.start()

try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)
