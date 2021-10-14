from solution import start, return_, let, add, sub, mul, div
import random
import types
import codewars_test as test


ops = [
    (add, lambda a, b: a + b, 'add'),
    (sub, lambda a, b: a - b, 'sub'),
    (mul, lambda a, b: a * b, 'mul'),
    (div, lambda a, b: a // b, 'div')
]


@test.describe('No Cheating!')
def cheats():

    @test.it('No usage of keyword "class" and "type"')
    def keyword_test():
        with open('solution.py', 'r') as f:
            content = f.read()
            test.expect('class' not in content and 'type' not in content, 'Custom classes are not allowed!')

    @test.it('Custom object/classes are not allowed')
    def object_test():
        check_type = type(start(return_))
        test.expect(check_type == types.FunctionType, f'Object {check_type} is not allowed! Only functions and lambdas!')


@test.describe('Simple Tests')
def tests():

    @test.it('Basic Tests')
    def basic_tests():
        test.assert_equals((start)(return_)(add)(20)(5), 25, "(start)(return_)(add)(20)(5)")
        test.assert_equals((start)(return_)(12345), 12345, "(start)(return_)(12345)")
        test.assert_equals((start)(let)('x')(12)(return_)('x'), 12, "(start)(let)('x')(12)(return_)('x')")
        test.assert_equals((start)(let)('a')(22)(return_)(div)('a')(11), 2, "(start)(let)('a')(22)(return_)(div)('a')(11)")
        test.assert_equals((start)(let)('x')(mul)(9)(8)(return_)('x'), 72, "(start)(let)('x')(mul)(9)(8)(return_)('x')")
        test.assert_equals((start)(return_)(div)(100)(5), 20, "(start)(return_)(div)(100)(5)")
        test.assert_equals((start)(return_)(sub)(100)(5), 95, "(start)(return_)(sub)(100)(5)")
        test.assert_equals((start)(let)('x')(sub)(100)(50)(return_)(add)('x')(10), 60, "(start)(let)('x')(sub)(100)(50)(return_)(add)('x')(10)")
        test.assert_equals((start)(let)('potato')(0)(let)('potato')(add)('potato')(10)(return_)('potato'), 10, "(start)(let)('potato')(0)(let)('potato')(add)('potato')(10)(return_)('potato')")
        test.assert_equals((start)(let)('bottle')(div)(10000)(200)(return_)(mul)(50)('bottle'), 2500, "(start)(let)('bottle')(div)(10000)(200)(return_)(mul)(50)('bottle')")

    @test.it('Tests with Nested Operators')
    def nested_tests():
        test.assert_equals((start)(return_)(add)(add)(10)(503)(5), 518, "(start)(return_)(add)(add)(10)(503)(5)")
        test.assert_equals((start)(let)('x')(sub)(100)(mul)(20)(4)(return_)(add)('x')(10), 30, "(start)(let)('x')(sub)(100)(mul)(20)(4)(return_)(add)('x')(10)")
        test.assert_equals((start)(let)('pizza')(div)(20)(4)(return_)(add)('pizza')(mul)(2)(3), 11, "(start)(let)('pizza')(div)(20)(4)(return_)(add)('pizza')(mul)(2)(3)")
        test.assert_equals((start)(let)('apple')(54)(return_)(add)(mul)('apple')(8)('apple'), 486, "(start)(let)('apple')(54)(return_)(add)(mul)('apple')(8)('apple')")
        test.assert_equals((start)(return_)(add)(mul)(div)(250)(25)(4)(sub)(40)(div)(60)(3), 60, "(start)(return_)(add)(mul)(div)(250)(25)(4)(sub)(40)(div)(60)(3)")

    @test.it('Tests with Multiple Variables')
    def multivar_tests():
        test.assert_equals((start)(let)('x')(mul)(7)(9)(let)('y')(div)(296)(8)(return_)(add)('x')('y'), 100, "(start)(let)('x')(mul)(7)(9)(let)('y')(div)(296)(8)(return_)(add)('x')('y')")
        test.assert_equals((start)(let)('x')(mul)(8)(9)(let)('y')(div)(296)('x')(return_)(mul)('x')('y'), 288, "(start)(let)('x')(mul)(8)(9)(let)('y')(div)(296)('x')(return_)(mul)('x')('y')")
        test.assert_equals((start)(let)('x')(1942)(let)('y')(58)(return_)(div)('x')('y'), 33, "(start)(let)('x')(1942)(let)('y')(58)(return_)(div)('x')('y')")
        test.assert_equals((start)(let)('x')(9)(let)('y')(div)(487)('x')(let)('z')(mul)('y')('y')(return_)('z'), 2916, "(start)(let)('x')(9)(let)('y')(div)(487)('x')(let)('z')(mul)('y')('y')(return_)(mul)('x')('y')")
        test.assert_equals((start)(let)('x')(1)(let)('y')(2)(return_)('x'), 1, "(start)(let)('x')(1)(let)(y)(2)(return_)('x')")

    @test.it('Daniel the Egg Test')
    def daniel_test():
        test.assert_equals((start)(let)('daniel_the_egg')(add)(add)(add)(add)(add)(add)(add)(add)(add)(add)(add)(add)(add)(add)(add)(add)(add)(add)(add)(add)(1)(2)(3)(4)(5)(6)(7)(8)(9)(10)(11)(12)(13)(14)(15)(16)(17)(18)(19)(20)(21)(return_)('daniel_the_egg'), 231)
        test.assert_equals((start)(let)('daniel_the_egg')(sub)(sub)(sub)(sub)(sub)(sub)(sub)(sub)(sub)(sub)(sub)(sub)(sub)(sub)(sub)(sub)(sub)(sub)(sub)(sub)(1)(2)(3)(4)(5)(6)(7)(8)(9)(10)(11)(12)(13)(14)(15)(16)(17)(18)(19)(20)(21)(return_)('daniel_the_egg'), -229)


@test.describe('Random Tests')
def randoms():

    @test.it('Random Values')
    def keyword_test():
        for _ in range(50):
            a, b, c, d = [random.randint(1, 1000) for _ in range(4)]

            # remove div as combining operator to prevent potential division by 0
            op_choice = [random.choice(ops) for _ in range(2)] + [random.choice(ops[: -1])]

            prediction = (start)(let)('x')(op_choice[0][0])(a)(b)(let)('y')(op_choice[1][0])(c)(d)(return_)(op_choice[2][0])('x')('y')
            label = op_choice[2][1](op_choice[0][1](a, b), op_choice[1][1](c, d))
            code = f"(start)(let)('x')({op_choice[0][2]})({a})({b})(let)('y')({op_choice[1][2]})({c})({d})(return_)({op_choice[2][2]})('x')('y')"

            test.assert_equals(prediction, label, code)

@test.describe('Immutability Check')
def mutability():

    @test.it('Simple Checks')
    def simple_immutability():
        f = (start)(let)('banana')(add)(20)
        g = (f)(10)(return_)
        h = (f)(-20)

        a = (g)(add)(5)(8)
        b = (g)(mul)('banana')(2)
        c = (h)(return_)('banana')

        print("""
Testing immutability with the following context:

f = (start)(let)('banana')(add)(20)
g = (f)(10)(return_)
h = (f)(-20)

a = (g)(add)(5)(8)
b = (g)(mul)('banana')(2)
c = (h)(return_)('banana')"""
        )

        test.assert_equals(a, 13, "(start)(let)('banana')(add)(20)(10)(return_)(add)(5)(8)")
        test.assert_equals(b, 60, "(start)(let)('banana')(add)(20)(10)(return_)(mul)('banana')(2)")
        test.assert_equals(c, 0, "(start)(let)('banana')(add)(20)(-20)(return_)('banana')")

    @test.it('Random Partial Code Reuse')
    def partial():

        def rand_name(length=5):
            return random.choice('abcdefg') + ''.join(random.choice('abcdefg1234567') for _ in range(length - 1))

        for _ in range(5):
            ns = [rand_name() for _ in range(4)]
            a, b = [random.randint(1, 1000) for _ in range(2)]
            f = (start)(let)(ns[0])(a)(let)(ns[1])(b)
            g = (f)(let)(ns[0])(0)(let)(ns[1])(10)

            for _ in range(5):
                c, d = [random.randint(1, 1000) for _ in range(2)]
                g = (f)(let)(ns[2])(c)(let)(ns[3])(d)

                op_choice = [random.choice(ops) for _ in range(2)] + [random.choice(ops[: -1])]
                prediction = (g)(return_)(op_choice[2][0])(op_choice[0][0])(ns[0])(ns[1])((op_choice[1][0]))(ns[2])(ns[3])
                label = op_choice[2][1](op_choice[0][1](a, b), op_choice[1][1](c, d))
                code = f"(start)(let)('a')({a})(let)('b')({b})(let)('c')({c})(let)('d')({d})(return_)({op_choice[2][2]})('a')('b')({op_choice[0][2]})('c')('d')"

                test.assert_equals(prediction, label, code)
