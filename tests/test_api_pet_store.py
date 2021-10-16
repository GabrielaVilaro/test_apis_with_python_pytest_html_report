import json
from apis.base_api_pet_store import BaseApiPetStore
from apis.body.body_pet_store import BodyPetStore
from utils.utils import random_number


class TestApiStore:

    @classmethod
    def setup_class(cls):
        print("Pre-Condiciones")
        cls.randomNum = random_number()

    def test_add_new_pet_validate(self):
        """Este test agrega una nueva mascota y valida que se haya hecho de manera correcta, status code 200"""

        response = BaseApiPetStore.post_new_pet(data=BodyPetStore.body_add_pet(name="Lola",
                                                                               type="Dog",
                                                                               status="Available",
                                                                               num=self.randomNum))
        status_code = response.status_code
        json_response = json.loads(response.text)
        print(json.dumps(json_response, indent=3))

        assert status_code == 200

    def test_get_body_by_id(self):
        """Este test agrega una nueva mascota, después realiza un get de la misma y valida status code 200"""

        response = BaseApiPetStore.post_new_pet(data=BodyPetStore.body_add_pet(name="Luna",
                                                                               type="Dog",
                                                                               status="Available",
                                                                               num=self.randomNum))
        json_response = json.loads(response.text)
        print(json.dumps(json_response, indent=3))

        id_pet = json_response['id']

        response_get = BaseApiPetStore.get_pet_by_id(id_pet=id_pet)

        assert response_get.status_code == 200

    def test_delete_pet_by_id(self):
        """Este test primero crea una mascota y deespues la elimina por id"""

        response = BaseApiPetStore.post_new_pet(data=BodyPetStore.body_add_pet(name="Luna",
                                                                               type="Dog",
                                                                               status="Available",
                                                                               num=self.randomNum))
        json_response = json.loads(response.text)
        print(json.dumps(json_response, indent=3))

        id_pet = json_response['id']

        response_get = BaseApiPetStore.delete_pet_by_id(id_pet=id_pet)

        assert response_get.status_code == 200

    def test_put_existing_pet_by_id(self):
        """Este test primero crea una mascota y deespues la actualiza por id"""

        response = BaseApiPetStore.post_new_pet(data=BodyPetStore.body_add_pet(name="Luna",
                                                                               type="Dog",
                                                                               status="Available",
                                                                               num=self.randomNum))
        json_response = json.loads(response.text)
        print(json.dumps(json_response, indent=3))

        id_pet = json_response['id']

        response_get = BaseApiPetStore.post_new_pet(data=BodyPetStore.body_add_pet(name="Lola",
                                                                                   type="Dog",
                                                                                   status="OK",
                                                                                   num=id_pet))

        assert response_get.status_code == 200
