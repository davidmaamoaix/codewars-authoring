from solution import count_horses
import codewars_test as test

@test.describe("Counting Horses")
def tests():
    # Use "it" to identify the conditions you are testing for
    @test.it("Example Cases")
    def horses_test():
        test.assert_equals(sorted(count_horses('010101010')), [2])
        test.assert_equals(sorted(count_horses('00000000')), [])
        test.assert_equals(sorted(count_horses('0001000100010001000100')), [4])
        test.assert_equals(sorted(count_horses('11111')), [1])
        test.assert_equals(sorted(count_horses('0111020111')), [2, 3])
        test.assert_equals(sorted(count_horses('0212030212')), [2, 2, 3])
        test.assert_equals(sorted(count_horses('122213122213122')), [1, 2, 3])
