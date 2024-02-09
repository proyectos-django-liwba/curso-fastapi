from starlette import status


class CustomValidationError(Exception):
    def __init__(self, error_msg, status_code=status.HTTP_400_BAD_REQUEST):
        self.error_msg = error_msg
        self.status_code = status_code
