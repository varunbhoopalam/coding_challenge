class ProfileNotFoundError(Exception):
    def __init__(self, message, data):
        super().__init__(message)
        self.data = data


class ServiceNotAvailable(Exception):
    def __init__(self, message, data):
        super().__init__(message)
        self.data = data
