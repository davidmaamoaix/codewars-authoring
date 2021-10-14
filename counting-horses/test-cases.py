from solution import count_horses
from random import randint
import codewars_test as test

def generate_sound(horses, length=20):
    sound = []
    for i in range(length):
        period = i + 1
        amount = sum(period % horse == 0 for horse in horses)
        sound.append(str(amount))

    return ''.join(sound)

@test.describe("Counting Horses")
def tests():
    # Use "it" to identify the conditions you are testing for
    @test.it("Trivial Test Cases")
    def horses_test():
        test.assert_equals(sorted(count_horses('010101010')), [2])
        test.assert_equals(sorted(count_horses('00000000')), [])
        test.assert_equals(sorted(count_horses('0001000100010001000100')), [4])
        test.assert_equals(sorted(count_horses('11111')), [1])
        test.assert_equals(sorted(count_horses('0111020111')), [2, 3])
        test.assert_equals(sorted(count_horses('0212030212')), [2, 2, 3])
        test.assert_equals(sorted(count_horses('122213122213122')), [1, 2, 3])
        test.assert_equals(sorted(count_horses('01120202110301120202')), [2, 3, 4])
        test.assert_equals(sorted(count_horses('25463736462826562727')), [1, 1, 2, 2, 2, 3, 3, 4, 5, 7])
        test.assert_equals(sorted(count_horses('001111112102012102022002102202')), [3, 4, 5, 7, 9])

    @test.it("Random Test Cases")
    def random_horses_test():
        for _ in range(500):
            horses = sorted([randint(1, 10) for _ in range(randint(4, 9))])
            sound = generate_sound(horses, randint(75, 200))
            test.assert_equals(sorted(count_horses(sound)), horses)

    @test.it("Large Random Test Cases")
    def large_random_horses_test():
        for _ in range(250):
            a,b = (1, 5) if randint(0,1) else (1, 100)
            horses = sorted([randint(a,b) for _ in range(randint(7, 9))])
            sound = generate_sound(horses, randint(450, 1000))
            test.assert_equals(sorted(count_horses(sound)), horses)
