import click
from arrow.cli import pass_context, json_loads
from arrow.decorators import apollo_exception, dict_output

@click.command('merge_exons')
@click.argument("exon_a", type=str)
@click.argument("exon_b", type=str)

@click.option(
    "--organism",
    help="Organism Common Name",
    type=str
)
@click.option(
    "--sequence",
    help="Sequence Name",
    type=str
)

@pass_context
@apollo_exception
@dict_output
def cli(ctx, exon_a, exon_b, organism="", sequence=""):
    """Merge two exons
    """
    return ctx.gi.annotations.merge_exons(exon_a, exon_b, organism=organism, sequence=sequence)
