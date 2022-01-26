import click
from app.db import load_csv_file
from app.db import insert_rows_db

@click.group()
def cli():
    pass

@cli.command("carregar_base")
def cmd_carregar_base_dados():
    load_csv_file()

@cli.command("inserir_banco")
def cmd_inserir_banco():
    insert_rows_db()

if __name__ == '__main__':
    cli()
