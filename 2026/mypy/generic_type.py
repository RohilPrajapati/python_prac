import random
from dataclasses import dataclass

# from typing import Any, TypeVar
from typing import NewType

RGB = NewType("RGB", tuple[int, int, int])
HSL = NewType("HSL", tuple[int, int, int])


@dataclass
class User:
    first_name: str
    last_name: str
    email: str
    age: int | None = None
    fav_color: RGB | None = None


def create_user(
    first_name: str,
    last_name: str,
    age: int | None = None,
    fav_color: RGB | None = None,
) -> User:
    email = f"{first_name.lower()}_{last_name.lower()}@example.com"

    return User(
        first_name=first_name,
        last_name=last_name,
        email=email,
        age=age,
        fav_color=fav_color,
    )


# generic typevar
# T = TypeVar("T")

# instead of TypeVar we can directly use like this :: New Approach
# def random_choice[T](items: list[T]) -> T:

# instead of using any where IDE/Text editor dont suggest anything use generic type
# def random_choice(items: list[Any]) -> User:
#     return random.choice(items)


def random_choice[T](items: list[T]) -> T:
    return random.choice(items)


user1 = create_user("Rohil", "Prajapati", age=25, fav_color=RGB((129, 133, 214)))
user2 = create_user("John", "Doe", fav_color=RGB((206, 10, 65)))

users = [user1, user2]
random_user = random_choice(users)
print(random_user)

emails = [user.email for user in users]
random_email = random_choice(emails)  # invalid type issue
print(random_email)
