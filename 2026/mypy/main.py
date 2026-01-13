# old way
# from typing import Optional
from typing import NewType, TypedDict


def create_user_1(
    first_name: str, last_name: str, age: int | None = None
) -> dict[str, str | int | None]:
    email = f"{first_name.lower()}_{last_name.lower()}@example.com"

    return {
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "age": age,
    }


# introduce from python 3.12
RGB = NewType("RGB", tuple[int, int, int])
HSL = NewType("HSL", tuple[int, int, int])


# type User = dict[str, str | int | RGB | None]
class User(TypedDict):
    first_name: str
    last_name: str
    email: str
    age: int | None
    fav_color: RGB | None


def create_user(
    first_name: str,
    last_name: str,
    age: int | None = None,
    fav_color: RGB | None = None,
) -> User:
    email = f"{first_name.lower()}_{last_name.lower()}@example.com"

    return {
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "age": age,
        "fav_color": fav_color,
    }


user1 = create_user("Rohil", "Prajapati", age=25, fav_color=RGB((129, 133, 214)))
user2 = create_user("John", "Doe", fav_color=RGB((206, 10, 65)))

print(user1)
print(user2)
