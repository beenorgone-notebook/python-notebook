# To explain how multiple dispatch can make more readable and less
# bug-prone code, let us implement the game of rock/paper/scissors in
# three styles.


class Thing(object):
    pass


class Rock(Thing):
    pass


class Paper(Thing):
    pass


class Scissors(Thing):
    pass


# First, a purely imperative version
def beats(x, y):
    if isinstance(x, Rock):
        if isinstance(y, Rock):
            return None  # No winner
        elif isinstance(y, Paper):
            return y
        elif isinstance(y, Scissors):
            return x
        else:
            raise TypeError("Unknown second thing.")
    if isinstance(x, Paper):
        if isinstance(y, Paper):
            return None  # No winner
        elif isinstance(y, Scissors):
            return y
        elif isinstance(y, Rock):
            return x
        else:
            raise TypeError("Unknown second thing.")
    if isinstance(x, Scissors):
        if isinstance(y, Scissors):
            return None  # No winner
        elif isinstance(y, Rock):
            return y
        elif isinstance(y, Paper):
            return x
        else:
            raise TypeError("Unknown second thing.")


# Mulitple dispatch version:
from multipledispatch import dispatch


@dispatch(Rock, Rock)
def beats_dp(x, y): return None


@dispatch(Rock, Scissors)
def beats_dp(x, y): return x


@dispatch(Rock, Paper)
def beats_dp(x, y): return y


@dispatch(Paper, Paper)
def beats_dp(x, y): return None


@dispatch(Paper, Scissors)
def beats_dp(x, y): return y


@dispatch(Paper, Rock)
def beats_dp(x, y): return x


@dispatch(Scissors, Scissors)
def beats_dp(x, y): return None


@dispatch(Scissors, Rock)
def beats_dp(x, y): return y


@dispatch(Scissors, Paper)
def beats_dp(x, y): return x


@dispatch(object, object)
def beats_dp(x, y):
    if not isinstance(x, (Rock, Paper, Scissors)):
        raise TypeError("Unknown first thing")
    else:
        raise TypeError("Unknown second thing")


r, s, p = Rock(), Scissors(), Paper()

print(beats(r, s))
print(beats_dp(s, p))
