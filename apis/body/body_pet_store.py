class BodyPetStore:

    @staticmethod
    def body_add_pet(type, status, name, num):
        request_body = {
            "id": num,
            "category": {
                "id": num,
                "name": type
            },
            "name": name,
            "photoUrls": [
                "string"
            ],
            "tags": [
                {
                    "id": num,
                    "name": "string"
                }
            ],
            "status": status
        }

        return request_body
