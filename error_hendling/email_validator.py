class Error(Exception):
    pass


class NameTooShortError(Error):
    def __init__(self, message="Name must be more than 4 characters"):
        self.message = message
        super().__init__(message)


class MustContainAtSymbolError(Error):
    pass


class InvalidDomainError(Error):
    pass


def validate_name_length(email):
    email = email.split("@")
    return len(email[0]) < 4


def validate_domain(email):
    email = email.split(".")
    domain = "." + email[-1]
    return domain not in [".com", ".bg", ".net", ".org"]


valid_email = True
line = input()
while line != "End":
    if validate_name_length(line):
        valid_email = False
        raise NameTooShortError()
    if "@" not in line:
        valid_email = False
        raise MustContainAtSymbolError("Email must contain @")
    if validate_domain(line):
        valid_email = False
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")
    if valid_email:
        print("Email is valid")
    line = input()

