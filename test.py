import sys
import argparse
import pexpect
import os


current_input = []


def run_session_with_commands(process, prompts_to_expect=(), commands=()):
    commands = list(commands)
    global current_input

    current_input = ''

    def log_input(s):
        global current_input
        current_input += s
        if s == '\r':
            # warning: very broken because user must type undo, exit, or quit
            # without using arrow keys or other readline-style editing
            if 'undo\r' in current_input:
                current_input = ''
                return '\x1d'
            if 'exit' in current_input or 'quit' in current_input:
                sys.exit()
            commands.append(current_input[:-1])
            current_input = ''
        return s

    while True:
        os.system('clear')
        p = pexpect.spawn(process)
        for command in commands:
            if prompts_to_expect:
                p.expect(prompts_to_expect)
            p.sendline(command)

        p.interact(input_filter=log_input)
        if not commands:
            sys.exit(0)
        commands.pop()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('cli',
                        help="command line interpreter to add undo to",
                        default=('python -i'),
                        nargs='*')

    args = parser.parse_args(sys.argv[1:])
    run_session_with_commands(args.cli, prompts_to_expect=['>>> ', '... '])
