class GatewayTimeoutException(Exception):
    pass

class ServiceTimeoutException(Exception):
    pass

class GatewayUnavailableException(Exception):
    pass

class ServiceUnavailableException(Exception):
    pass

class ServiceReadException(Exception):
    pass

class GatewayReadException(Exception):
    pass

class DatabaseReadException(Exception):
    pass

class DatabaseUnavailableException(Exception):
    pass

class ServiceNotFoundException(Exception):
    pass

class UnsupportedActionException(Exception):
    pass

class EndpointAlreadyExistsException(Exception):
    pass