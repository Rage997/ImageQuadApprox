import click
from imageQuadTree import ImageQuad

@click.command()
@click.argument('filename')
@click.option('-e', '--epsilon', default=10, help='Threshold wheter to split a quadtree or not.')
@click.option('-o', '--output', default=None, help='Output file')
@click.option('-l', '--line', is_flag=True, help='Outline for each quadrant box')


def main(filename, epsilon, output, line):
    quadart = ImageQuad(filename, epsilon=epsilon, draw_outine=line)
    quadart.generate()
    # quadart.save(output)
    if output:
        quadart.save(output)

if __name__ == '__main__':
    main()