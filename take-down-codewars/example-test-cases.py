from solution import attack_plan
import codewars_test as test

@test.describe("Basic Tests")
def tests():
    
    @test.it("Simple Tests")
    def simple():
        test.assert_equals(attack_plan([30, 10, 0, 100, 200, 300, 20, 10, 30, 1000], 7), 1500)
        test.assert_equals(attack_plan([200, 300, 20, 10, 30, 1000], 3), 1000)
        test.assert_equals(attack_plan([100, 0, 100, 0, 100, 0, 100, 0, 100], 5), 200)
        test.assert_equals(attack_plan([11, 15, 97, 102, 33, 1, 98, 112, 19, 12, 87, 64, 101], 7), 346)
        test.assert_equals(attack_plan([100, 100, 100, 100, 5, 5, 10, 20], 7), 220)
        
    @test.it("Weird Edge Cases")
    def edge():
        test.assert_equals(attack_plan([0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0], 10), 0)
        test.assert_equals(attack_plan([1, 2, 3, 4, 5, 6, 7], 2), 0)
        test.assert_equals(attack_plan([0, 0, 0, 0, 0, 1, 0 ,0 ,0 ,0], 3), 1)
        test.assert_equals(attack_plan([0, 10000, 0, 0, 0, 1, 0 ,0 ,0 ,0], 3), 1)
        test.assert_equals(attack_plan([100, 0, 0, 0, 0, 0, 0 ,0 ,0 ,100], 6), 100)