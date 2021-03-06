import click
from arrow.cli import pass_context
from arrow.decorators import custom_exception, dict_output


@click.command('update_membership')
@click.argument("group_id", type=int)
@click.option(
    "--users",
    help="List of emails",
    type=str,
    multiple=True
)
@pass_context
@custom_exception
@dict_output
def cli(ctx, group_id, users=None):
    """Update the group's membership

Output:

    dictionary of group information
    """
    return ctx.gi.groups.update_membership(group_id, users=users)
