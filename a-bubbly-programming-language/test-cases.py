from solution import start, end, push, add, sub, mul, div
import codewars_test as test
from random import randint, choice

ops = [
    (add, lambda stack: stack.append(stack.pop() + stack.pop())),
    (sub, lambda stack: stack.append(stack.pop() - stack.pop())),
    (mul, lambda stack: stack.append(stack.pop() * stack.pop())),
    (div, lambda stack: stack.append(stack.pop() // stack.pop()))
]

def push_stack(stack, bubble):
    value = randint(0, 1000)
    stack.append(value)
    return bubble(push)(value)

def random_operator(stack, bubble):
    op = choice(ops) if stack[-2] != 0 else choice(ops[:-1])
    op[1](stack)
    return bubble(op[0])

def make_test(n_operations=50):
    stack = []
    bubble = (start)

    for _ in range(n_operations):
        if len(stack) < 2:
            bubble = push_stack(stack, bubble)
        else:
            if randint(0, 1) != 0:
                bubble = push_stack(stack, bubble)
            else:
                bubble = random_operator(stack, bubble)

    # add operations until only one element in stack
    while len(stack) > 1:
        bubble = random_operator(stack, bubble)

    test.assert_equals(bubble(end), stack[-1])

@test.describe("bubbly_language")
def tests():
    # Use "it" to identify the conditions you are testing for
    @test.it("Basic Test Cases")
    def test_bubbly():
        test.assert_equals((start)(push)(5)(push)(3)(add)(end), 8)
        test.assert_equals((start)(push)(3)(push)(5)(sub)(end), 2)
        test.assert_equals((start)(push)(8)(push)(9)(push)(3)(mul)(mul)(end), 216)
        test.assert_equals((start)(push)(2)(push)(5)(div)(push)(3)(push)(8)(mul)(mul)(end), 48)
        test.assert_equals((start)(push)(1)(push)(1)(add)(push)(2)(add)(end), 4)

    @test.it("Random Test Cases")
    def random_test_bubbly():
        for _ in range(75):
            make_test()
