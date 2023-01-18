def test_list_breeds(dog_api):
    """
    Unit test to list dog breeds

    :param dog_api: Class Object Parameter from conftest. Type - DogAPI
    :return: None
    """

    expected_response = [
        {
            "weight": {"imperial": "50 - 60", "metric": "23 - 27"},
            "height": {"imperial": "25 - 27", "metric": "64 - 69"},
            "id": 2,
            "name": "Afghan Hound",
            "country_code": "AG",
            "bred_for": "Coursing and hunting",
            "breed_group": "Hound",
            "life_span": "10 - 13 years",
            "temperament": "Aloof, Clownish, Dignified, Independent, Happy",
            "origin": "Afghanistan, Iran, Pakistan",
            "reference_image_id": "hMyT4CDXR",
            "image": {
                "id": "hMyT4CDXR",
                "width": 606,
                "height": 380,
                "url": "https://cdn2.thedogapi.com/images/hMyT4CDXR.jpg",
            },
        }
    ]

    actual_response = dog_api.list_breeds(
        query_dict={"attach_breed": 1, "page": 1, "limit": 1}
    )

    assert actual_response == expected_response
