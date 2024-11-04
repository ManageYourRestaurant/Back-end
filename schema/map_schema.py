from typing import Optional

from pydantic import BaseModel


class map_search_request(BaseModel):
    keyword: Optional[str]
    my_location_latitude: Optional[float]
    my_location_longitude: Optional[float]
    map_latitude_1: Optional[float]
    map_latitude_2: Optional[float]
    map_longitude_1: Optional[float]
    map_longitude_2: Optional[float]
