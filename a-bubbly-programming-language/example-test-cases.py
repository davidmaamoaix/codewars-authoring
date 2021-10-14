from solution import start, end, push, add, sub, mul, div
import codewars_test as test

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
