#!/usr/bin/env python
import click

@click.command()
@click.option('--name', default = 'Grader', help = 'This is your name')
@click.option('--repeat', default = 1, help = 'This is the number of times you will be greeted')
def hello(repeat, name):
    '''This script greets you.'''
    for i in range(repeat):
        click.echo('Hello %s!' % name)
    

if __name__ == '__main__':
    hello()