from re import compile
from typing import NamedTuple

MESSAGE = {
    'USERNAME': 'Username:',
    'EMAIL_ADDRESS': 'Email Address:',
    'INVALID_USER_DATA': 'Невалидные данные пользователя:',
    'INVALID_DATA_TYPE': 'Невалидное значение для',
}

EMAIL_PATTERN = compile(r'^[a-zA-Z0-9][a-zA-Z0-9._%+-]*@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')


class Validator:
    @staticmethod
    def validate_username(username: str) -> tuple[bool, str]:
        if not isinstance(username, str):
            return False, "должен быть строкой"
        if not username or not username.strip():
            return False, "не может быть пустым"
        if len(username) < 3 or len(username) > 50:
            return False, "длина должна быть 3-50 символов"
        if not username.isalnum():
            return False, "только буквы и цифры"
        if not any(c.isalpha() for c in username):
            return False, "должна быть хотя бы одна буква"
        return True, username

    @staticmethod
    def validate_email(email: str) -> tuple[bool, str]:
        if not isinstance(email, str):
            return False, "должен быть строкой"
        if not email or not email.strip():
            return False, "не может быть пустым"
        if len(email) > 254:
            return False, "слишком длинный email"
        if not EMAIL_PATTERN.fullmatch(email):
            return False, "неверный формат email"
        return True, email.lower()


class UserData(NamedTuple):
    username: str
    email: str


class User:
    def __init__(self, username: str, email: str):
        valid_user, msg_user = Validator.validate_username(username)
        if not valid_user:
            raise ValueError(f"{MESSAGE['INVALID_USER_DATA']} username: {msg_user}")

        valid_email, msg_email = Validator.validate_email(email)
        if not valid_email:
            raise ValueError(f"{MESSAGE['INVALID_USER_DATA']} email: {msg_email}")

        self.__username = username
        self.__email = msg_email

    @property
    def username(self) -> str:
        """Геттер для username (только чтение)"""
        return self.__username

    @property
    def email(self) -> str:
        """Геттер для email (только чтение)"""
        return self.__email

    @username.setter
    def username(self, value: str) -> None:
        """Сеттер для username с валидацией"""
        valid, msg = Validator.validate_username(value)
        if not valid:
            raise ValueError(f"{MESSAGE['INVALID_DATA_TYPE']} username: {msg}")
        self.__username = value

    @email.setter
    def email(self, value: str) -> None:
        """Сеттер для email с валидацией"""
        valid, msg = Validator.validate_email(value)
        if not valid:
            raise ValueError(f"{MESSAGE['INVALID_DATA_TYPE']} email: {msg}")
        self.__email = msg

    def get_all(self) -> UserData:
        return UserData(username=self.__username, email=self.__email)

    def __str__(self) -> str:
        return f"{MESSAGE['USERNAME']} {self.__username}, {MESSAGE['EMAIL_ADDRESS']} {self.__email}"

user = User('StalerG', 'buhaem@pivo.com')
print(user)