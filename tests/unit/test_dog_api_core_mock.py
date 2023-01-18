def test_mock_list_breeds(mocker, dog_api):
    mocked_call_api_value = [
        {
            "weight": {"imperial": "44 - 66", "metric": "20 - 30"},
            "height": {"imperial": "30", "metric": "76"},
            "id": 3,
            "name": "African Hunting Dog",
            "bred_for": "A wild pack animal",
            "life_span": "11 years",
            "temperament": "Wild, Hardworking, Dutiful",
            "origin": "",
            "reference_image_id": "rkiByec47",
            "image": {
                "id": "rkiByec47",
                "width": 500,
                "height": 335,
                "url": "https://cdn2.thedogapi.com/images/rkiByec47.jpg",
            },
        }
    ]
    mocker.patch("dog_api.core.DogAPI.call_api", return_value=mocked_call_api_value)

    actual_mock_response = dog_api.list_breeds(
        query_dict={"attach_breed": 1, "page": 2, "limit": 1}
    )

    assert mocked_call_api_value == actual_mock_response
