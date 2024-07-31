from datetime import datetime


class Field:
    """
    Basic class for records fields
    """

    def __init__(self, value: str):
        self.value = value
        self.validate_field()

    def __str__(self):
        return str(self.value)

    def validate_field(self):
        pass


class Name(Field):
    """
    Class for saving and validating contact names
    """

    def validate_field(self):
        if len(self.value) < 1:
            raise ValueError("Name can't be empty")


class Phone(Field):
    """
    Class for saving and validating contact phones
    """

    def validate_field(self):
        if len(self.value) != 10:
            raise ValueError("Phone number must be 10 digits long")


class Birthday(Field):

    def validate_field(self):
        """
        convert input value to 'datetime' and validate format
        """
        try:
            self.value = datetime.strptime(self.value, "%d.%m.%Y").date()
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")
