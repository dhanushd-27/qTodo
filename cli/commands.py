import click


@click.group()
def app() -> None:
    """qTodo CLI."""


@app.command()
def hi() -> None:
    """Say hi."""
    click.echo("Hi")


def main() -> None:
    app()


if __name__ == "__main__":
    main()
