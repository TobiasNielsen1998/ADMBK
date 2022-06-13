class Requests:
    """
    Requests class holds attributes and methods for a request
    """
    def __init__(self, request_status = "Pending"):
        request = ""
        self.request_status = request_status
        self.request = {request_status, request}

    def schedule_request(self, request :str):
        """
        Creats requests
        """
        if request != "Write your request here...":
            return self.request
        
    
