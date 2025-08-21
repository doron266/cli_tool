import click
import crud


@click.group(chain=True)
def cli() -> None:
    pass

cli.add_command(crud.create)

cli.add_command(crud.list_objects)


if __name__ == '__main__':
    cli()

