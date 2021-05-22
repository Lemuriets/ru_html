from os import system
from compile import Compile


def help_command(*args, **kwargs) -> None:
    with open('help_text.txt', 'r', encoding='utf-8') as help_file:
        help_text = help_file.read()
    print(help_text)


def start_compile(path: str, *args, **kwargs) -> None:
    Compile(path)


commands = {
    'help': help_command,
    'create': start_compile,
    'clear': lambda: system('cls'),
    'q': lambda: exit(0)
}


def main() -> None:
    try:
        input_command = input('>>> ')
    except KeyboardInterrupt:
        exit(0)
    options = input_command.split(' ')[1::]
    command = input_command.split(' ')[0]

    if command not in commands.keys():
        print('unknown command, enter "help" for looking all commands')
        main()

    commands[command](*options)
    main()


if __name__ == '__main__':
    main()