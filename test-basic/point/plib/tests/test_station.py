import pytest
import copy
from plib import Station, StationError, StationMap

@pytest.fixture
def js1():
    js = {
        "code": "abdl",
        "height": 162.27803882118315,
        "status": "new",
        "location": {
            "lat": 0.0,
            "lon": 0.0
        },
        "xyz": [
            2243908.9008,
            3048443.7188,
            5116457.9962
        ]
    }
    return js

@pytest.fixture
def js2():
    js = {
        "code": "abdl",
        "height": 162.27803882118315,
        "status": "new",
        "location": {
            "lat": 15.5,
            "lon": 0.0
        },
        "xyz": [
            2243908.9008,
            3048443.7188,
            5116457.9962
        ]
    }
    return js

@pytest.fixture
def json_data():
    text = """
    [
        {
            "code": "abdl",
            "height": 162.27803882118315,
            "status": "new",
            "location": {
                "lat": 0.0,
                "lon": 0.0
            },
            "xyz": [
                2243908.9008,
                3048443.7188,
                5116457.9962
            ]
        },
        {
            "code": "abkn",
            "height": 219.23325751908123,
            "status": "new",
            "location": {
                "lat": 1.0,
                "lon": 0.0
            },
            "xyz": [
                -90768.799,
                3777267.336,
                5121588.168
            ]
        },
        {
            "code": "akta",
            "height": 9.000523968599737,
            "status": "new",
            "location": {
                "lat": 43.635784608238296,
                "lon": 51.16564178272316
            },
            "xyz": [
                2899263.731,
                3601532.113,
                4378898.794
            ]
        },
        {
            "code": "akya",
            "height": 330.27589765004814,
            "status": "new",
            "location": {
                "lat": 51.87357905297636,
                "lon": 58.21538535254553
            },
            "xyz": [
                2078592.977,
                3354438.194,
                4994390.812
            ]
        }
    ]
    """
    return text


class TestStation:
    
    def test_creation(self, js1):
        try:
            Station(**js1)
        except Exception as e:
            pytest.fail(f"Failed with exception: '{type(e)} -> {e}'")

        required_fields = [
            "code", 
            "height",
            "location",
            "status"
        ]

        for field in required_fields:
            data_copy = copy.deepcopy(js1)

            del data_copy[field]
            with pytest.raises(StationError): 
                Station(**data_copy)

    def test_distance_to_another_station(self, js1, js2):
        s1 = Station(**js1)
        s2 = Station(**js2)

        assert s1.distance_to(s2) == 15.5 


class TestStationMap:
    def test_creation(self, js1, js2):
        st1, st2 = Station(**js1), Station(**js2)
        stations = StationMap([st1, st2])
        assert stations['abdl'] == st1

    def test_load_from_json(self, json_data):
        stations = StationMap.from_json(json_data)
        names = list(stations)

        import json
        js = json.loads(json_data)
        names_js = [item["code"] for item in js]

        assert names == names_js


    def test_save_in_json(self, json_data):
        text = StationMap.from_json(json_data).to_json()
        print("JSON:", text)
        assert text == json_data

    def test_nearest_station(self, json_data):
        stations = StationMap.from_json(json_data)
        assert stations.nearest("abdl").code == "abkn"
