def ConsoleMsg(msg, width=65):
    msg = f'|{msg.center(width - 2)}|'
    border = '-' * width
    return f'{border}\n{msg}\n{border}'


def ErrorlessInput(msg, type=str):
    while True:
        try:
            return type(input(msg))
        except Exception as e:
            print(f"Some error happened during input. <{repr(e)}>")


def ClampInput(msg, range, type=float):
    value = ErrorlessInput(msg, type)
    while not (value >= range[0] and value <= range[1]):
        print(f"Inputted value should be between {range[0]} and {range[1]}")
        value = ErrorlessInput(msg, type)
    return value


def OptionInput(msg, options, case_sensitive=False):
    value = ErrorlessInput(f"{msg}  ({', '.join(options)})\n")

    value = value.lower() if case_sensitive else value
    while value not in [opt for opt in options]:
        print(f"Input should be choose between ({', '.join(options)})")
        value = ErrorlessInput(msg)
        value = value.lower() if case_sensitive else value
    return value
