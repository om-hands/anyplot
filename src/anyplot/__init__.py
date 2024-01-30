import click
from matplotlib import pyplot as plt
from py_xrd_visualize.xrd import make_any_scan_naxis


@click.command()
@click.argument("paths", nargs=-1, type=click.Path(exists=True))
def plot(paths):
    make_any_scan_naxis(paths)
    plt.show()


if __name__ == "__main__":
    plot()
