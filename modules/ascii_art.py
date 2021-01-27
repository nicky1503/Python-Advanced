from pyfiglet import figlet_format


def print_art(msg, font):
    msg = figlet_format(msg, font=font)
    return msg


print(print_art(input("Msg:"), input("Font:")))

