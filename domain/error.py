class Error(Exception):
  def __init__(self, code, message):
    self.code = code
    self.message = message

  def __str__(self):
    return {
      "error":{
        "code": self.code,
        "message": self.message
      }
    }
