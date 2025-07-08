PORT="5001"
import requests
class CommunicationProdService:
    def __init__(self):
        self.PORT="5001"
        self.URL=f"http://localhost:{PORT}/products/getProduct"

    def obtainProductInfo(self,product_id)->dict:
        try:
            request=requests.get(
                self.URL,params=product_id
            )
            response=request.json()
            return response
        except Exception as e:
            raise ValueError (str(e))


