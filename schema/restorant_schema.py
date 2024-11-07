from pydantic import BaseModel


class Restorant(BaseModel):
    restorant_id: str
    name: str


class RestorantResponse(Restorant):
    pass
