from softmachine.models.vm import VM

import click

@click.group()
def cli():
    pass

@cli.command()
@click.option("-f", "--file", "file")
@click.option("-s", "--stdin", "stdin")
def exec(file, stdin):
    if file is not None and stdin is None:
        with open(file) as f:
            lines = f.readlines()
        code = "\n".join(x[:-1] for x in lines)
    elif file is None and stdin is not None:
        # 0x12345 0x12345
        # 0x12345;0x12345
        # are correct expected code
        code = stdin.replace(";","\n").replace(" ", "\n")
    elif file is None and stdin is None:
        print("Either one of file or stdin must be set. Exiting.")
        exit(1)

    vm = VM()
    vm.exec(code)

@cli.command()
@click.option("-f", "--file", "file")
@click.option("-s", "--stdin", "stdin")
def assemble(file, stdin):
    pass

@cli.command()
@click.option("-f", "--file", "file")
@click.option("-s", "--stdin", "stdin")
def disassemble(file, stdin):
    pass

