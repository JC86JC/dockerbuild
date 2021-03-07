#!/usr/bin/env python
import click
import numpy as np

@click.command()
@click.option('--start', default = 2, help = 'This is the beginning of the range.')
@click.option('--end', default = 10, help = 'This is the end of the range.')

def primes_between(start, end):
    """Return primes between start and end."""
    
    def is_prime(n):
        """Check if n is prime."""
    
        if n == 2:
            return True
        elif n % 2 == 0 or n < 2:
            return False
        else:
            for i in range(3, 1 + int(np.sqrt(n)), 2):
                if n % i == 0:
                    return False
        return True
    
    click.echo('Prime numbers are: {}'.format(np.array([i for i in range(start, end) if is_prime(i)])))

if __name__ == '__main__':
    primes_between()