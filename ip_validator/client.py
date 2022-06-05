import grpc

from ip_validator.proto.grpc_ip import ip_pb2_grpc as ip_pb2_grpc, ip_pb2 as ip_pb2

channel = grpc.insecure_channel('localhost:8000')

stub1 = ip_pb2_grpc.IPValidatorStub(channel)

ip_val = ip_pb2.IPRequest(ipAddress='128.101.101.101', countries=['US', 'CA'])

response = stub1.ValidateIP(ip_val)

print(response.valid)
