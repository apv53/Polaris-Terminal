from http import HTTPStatus

class AppException(Exception):
    
    #Base exception class for application specific errors
    def __init__(self, message:str, error_code: str, 
                 status_code: HTTPStatus = HTTPStatus.BAD_REQUEST) -> None:
        
        super().__init__(message)
        
        self.message = message
        self.error_code = error_code
        self.status_code = status_code