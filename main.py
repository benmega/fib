class InvalidStartingConditions(Exception):
    """Raised when user-defined starting conditions dictionary does not include 1 or 2 as a key"""

    def __init__(self, memory, message="The starting condition dictionary must include keys with value of 1 and 2"):
        self.memory = memory
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.memory} -> {self.message}'

    pass


def fib(n, memory=None):
    # This recursive function returns the nth Fibonacci number using dynamic programming
    # The starting values may be changed by pre-filling the memory

    # If no starting conditions are specified, set to 1,1,...
    if memory is None:
        memory = {1: 1, 2: 1}

    # Confirm memory is valid
    if 1 not in memory or 2 not in memory:
        raise InvalidStartingConditions(memory)

    # check memory
    if n in memory:
        return memory[n]

    # add to memory and return value
    if n < 1:
        memory[n] = fib(n + 2, memory) - fib(n + 1, memory)
    else:
        memory[n] = fib(n - 1, memory) + fib(n - 2, memory)
    return memory[n]


if __name__ == '__main__':
    print(fib(500, {1:2,2:2}))
    print(fib(5, {1: 1, 2: -1}))
    print(fib(500))
