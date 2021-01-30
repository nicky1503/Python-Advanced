class Error(Exception):
    pass


class ValueCannotBeNegative(Error):
    pass


for _ in range(5):
    line = int(input())
    if line < 0:
        raise ValueCannotBeNegative

