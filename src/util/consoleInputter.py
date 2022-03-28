def ConsoleMsg(msg, width=65):
    """Display a beautiful terminal topic heading

    Args:
        msg (any): msg shown in heading
        width (int, optional): width of the heading. Defaults to 65.

    Returns:
        _type_: decorated string of the message heading
    """
    msg = f'|{msg.center(width - 2)}|'
    border = '-' * width
    return f'{border}\n{msg}\n{border}\n'


def ErrorlessInput(msg, type=str):
    """Keep prompting for user input until errorless input is received

    Args:
        msg (string): message show in prompting user input
        type (<python type>, optional): type of casting after receiving user input. Defaults to str. e.g. type = int, type(input()) -> int(input())

    Returns:
        type: user input after casting to type(args)
    """
    while True:
        try:
            return type(input(msg))
        except Exception as e:
            print(f"Some error happened during input. <{repr(e)}>")


def ClampInput(msg, range, type=float):
    """Keep prompting for user input until input which is errorless, in-range is received

    Args:
        msg (string): message show in prompting user input
        range (list<int>): inclusive range of [max, min]
        type (<python type>, optional): Type of casting used in ErrorlessInput. Defaults to float.

    Returns:
        type: casted value get from user input
    """
    value = ErrorlessInput(msg, type)
    while not (value >= range[0] and value <= range[1]):
        print(f"Inputted value should be between {range[0]} and {range[1]}")
        value = ErrorlessInput(msg, type)
    return value


def OptionInput(msg, options, case_sensitive=False):
    """Keep prompting for user input until input which is errorless, in the option is received

    Args:
        msg (string): message show in prompting user input
        options (list<str>): option allow user to enter
        case_sensitive (bool, optional): Options to check character cases in input. Defaults to False. (e.g 'b' input will be accepted for option "B" if case_sensitive is False)

    Returns:
        string: option get from user input
    """

    msg = f"{msg}  ({', '.join(options)})\n"
    value = ErrorlessInput(msg)

    value = value.lower() if not case_sensitive else value
    while value not in [opt for opt in options]:
        print(f"Input should be choose between ({', '.join(options)})")
        value = ErrorlessInput(msg)
        value = value.lower() if not case_sensitive else value
    return value
