from solution import start, return_, let, add, sub, mul, div
import codewars_test as test


@test.describe('Example Tests')
def tests():

    @test.it('Simple <value> Test')
    def basic_tests():
        test.assert_equals((start)(return_)(42), 42)
        test.assert_equals((start)(return_)(mul)(3)(8), 24)
        test.assert_equals((start)(return_)(div)(15)(5), 3)
        test.assert_equals((start)(return_)(add)(15)(2), 17)
        test.assert_equals((start)(return_)(sub)(20)(9), 11)

    @test.it('Variable Assignment Test')
    def variable_test():
        test.assert_equals((start)(let)('my_var')(1024)(return_)('my_var'), 1024)
        test.assert_equals((start)(let)('x')(add)(500)(12)(return_)('x'), 512)
        test.assert_equals((start)(let)('x')(add)(4)(60)(let)('y')(8)(return_)(div)('x')('y'), 8)

    @test.it('Nested Operator Test')
    def nested_test():
        test.assert_equals((start)(return_)(add)(mul)(2)(4)(9), 17) # 2 * 4 + 9
        test.assert_equals((start)(let)('x')(div)(mul)(5)(6)(mul)(3)(5)(return_)(sub)('x')(1), 1) # (5 * 6) / (3 * 5) - 1
        test.assert_equals((start)(let)('wat')(mul)(mul)(9)(8)(add)(2)(3)(return_)(add)('wat')(12), 372) # 9 * 8 * (2 + 3) + 12

    @test.it('Daniel the Egg Test')
    def daniel_test():
        test.assert_equals((start)(let)('daniel_the_egg')(add)(add)(add)(add)(add)(add)(add)(add)(add)(add)(add)(add)(add)(add)(add)(add)(add)(add)(add)(add)(1)(2)(3)(4)(5)(6)(7)(8)(9)(10)(11)(12)(13)(14)(15)(16)(17)(18)(19)(20)(21)(return_)('daniel_the_egg'), 231)

    @test.it('Immutability Check')
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
