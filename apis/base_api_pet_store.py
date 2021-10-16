import json

import requests
from apis import initialize


class BaseApiPetStore:

    @staticmethod
    def post_new_pet(data):
        """:param data: body json
        :return: response json body"""

        response = requests.post(url=initialize.BASE_URL_PET + f"pet",
                                 data=json.dumps(data),
                                 headers=initialize.API_HEADER)

        return response

    @staticmethod
    def get_pet_by_id(id_pet):
        """:param data: body json
        :param id_pet: int
        :return: response json body"""

        response = requests.get(url=initialize.BASE_URL_PET + f"pet/{id_pet}",
                                 headers=initialize.API_HEADER)

        return response

    @staticmethod
    def delete_pet_by_id(id_pet):
        """:param data: body json
              :return: response json body"""

        response = requests.delete(url=initialize.BASE_URL_PET + f"pet/{id_pet}",
                                 headers=initialize.API_HEADER)

        return response

    @staticmethod
    def put_existing_pet(data):
        """:param data: body json
        :return: response json body"""

        response = requests.put(url=initialize.BASE_URL_PET + f"pet",
                                 data=json.dumps(data),
                                 headers=initialize.API_HEADER)

        return response

