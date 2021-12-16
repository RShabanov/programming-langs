from typing import Any, Union
from plib import Point
from typing import List, Dict, Union

class StationError(Exception):
    ...

class Station:
    def __init__(self,
        code: Union[str, None] = None,
        height: Union[float, None] = None,
        status: Union[str, None] = None,
        location: Union[Dict[str, float], None] = None,
        xyz: Union[List[float], None] = None
    ):
        if code is None: 
            raise StationError("Station must have its code")
        if height is None: 
            raise StationError("Station must have height")
        if status is None: 
            raise StationError("Station must have some status")
        if location is None: 
            raise StationError("Station must have location")

        if not isinstance(code, str):
            raise StationError("Constructor argument 'code' is supposed to be 'str'")
        if not isinstance(height, float):
            raise StationError("Constructor argument 'height' is supposed to be 'float'")
        if not isinstance(status, str):
            raise StationError("Constructor argument 'status' is supposed to be 'str'")
        if 'lat' not in location.keys() or 'lon' not in location.keys():
            raise StationError("Constructor argument 'location' is supposed to have 'lat' and 'lon'")
        else:
            pass
        
        self.code = code
        self.height = height
        self.status = status
        self.location = Point(location['lat'], location['lon'])

    def distance_to(self, other: "Station") -> float:
        return self.location.distance_to(other.location)

    def __eq__(self, other: object) -> bool:
        # for a while we check only codes
        return self.code == other.code



class StationMap:
    def __init__(self, stations: List[Station]) -> None:
        if not isinstance(stations, list):
            raise StationMapError
        
        self._stations = {station.code : station for station in stations}

    def __getitem__(self, key: str) -> Station:
        return self._stations[key]

    @classmethod
    def from_json(cls, json_file: str):
        import json
        json_data = json.loads(json_file)
        stations = []

        for item in json_data:
            stations.append(Station(**item))

        return cls(stations)

    def to_json(self):
        import json
        return json.dumps(self._stations)

    def __len__(self):
        return len(self._stations)

    def __iter__(self):
        for station in self._stations:
            yield station
        



class StationMapError(Exception):
    ...