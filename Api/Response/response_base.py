from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi import status

class ResponseBase:
    def __init__(self, status, message, data = None):
        self.status = status
        self.message = message
        self.data = data

    def to_dict(self):
        status_res = status.HTTP_200_OK
        
        if self.status == 201:
            status_res = status.HTTP_201_CREATED
        elif self.status == 202:
            status_res = status.HTTP_202_ACCEPTED
        elif self.status == 204:
            status_res = status.HTTP_204_NO_CONTENT
            
        res_content = {
            'status': self.status,
            'message': self.message
        }
        
        if self.data is not None:
            res_content['data'] = jsonable_encoder(self.data)
            
        return JSONResponse(
            status_code=status_res,
            content = res_content
        )
