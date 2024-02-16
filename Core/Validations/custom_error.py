class CustomError(Exception):
  def __init__(self, code, message, details=None):
    self.code = code
    self.message = message
    self.details = details

  def __str__(self):
    error_dict = {
      "error": {
        "code": self.code,
        "message": self.message
      }
    }
    
    if self.details is not None:
      error_dict["error"]["details"] = self.details
    
    return error_dict
