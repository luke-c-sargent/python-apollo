import click
from arrow.cli import pass_context, json_loads
from arrow.decorators import apollo_exception, dict_output

@click.command('set_longest_orf')
@click.argument("feature_id", type=str)

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
def cli(ctx, feature_id, organism="", sequence=""):
    """Automatically pick the longest ORF in a feature
    """
    return ctx.gi.annotations.set_longest_orf(feature_id, organism=organism, sequence=sequence)
