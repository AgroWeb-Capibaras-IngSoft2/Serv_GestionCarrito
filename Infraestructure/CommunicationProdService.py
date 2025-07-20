import requests
class CommunicationProdService:
    def __init__(self):
        self.PORT="5000"
        self.URL=f"http://localhost:{self.PORT}/products"

    def obtainProductInfo(self,product_id):
        try:
            url=f"{self.URL}/{product_id}"
            response=requests.get(
                url
            )
            response.raise_for_status()
            return response.json()
        except Exception as e:
            raise ValueError (str(e))


