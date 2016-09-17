import click
import random
import sys


@click.command()
@click.option('--rounds', default=1, help='Number of Rounds.')
@click.option('--max_number', default=10, help='The Highest Guessable Number')
def main(rounds, max_number):
    """
    Try to guess the secret number!
    Fewer guesses means more points!
    A higher max number is harder but means more points too!
    """
    secret_number = random.randint(1, max_number)
    for x in range(rounds):
        user_guess = guess()
        if (user_guess == secret_number):
            victory(rounds, x, max_number)
        elif (user_guess > secret_number):
            click.echo("Guess a smaller number")
        else:
            click.echo("Guess a bigger number")
    loss(secret_number)


def victory(rounds, x, max_number):
    click.echo("Great Job!")
    click.echo("You guessed it in {0} guess(es)!".format(x + 1))
    score = int(max_number * rounds / (x + 1))
    click.echo("Score: {0}".format(score))
    sys.exit(0)


def loss(secret_number):
    click.echo("Oh No you lose!")
    click.echo("It's a Secret to Everybody: {0}".format(secret_number))


def guess():
    guess = click.prompt("Please guess a number")
    return int(guess)

if __name__ == '__main__':
    main()
