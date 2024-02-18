

class ResponseBase:
    def __init__(self, status, message, data = None):
        self.status = status
        self.message = message
        self.data = data

    def to_dict(self):
        return {
            'status': self.status,
            'message': self.message,
            'data': self.data
        }