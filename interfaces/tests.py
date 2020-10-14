import typing as typ 


class Stat(typ.NamedTuple):
    name: str
    age: int


s = Stat('1111','1111')

s.name = 111
