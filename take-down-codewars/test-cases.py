from solution import attack_plan
import codewars_test as test

from random import randint
from functools import lru_cache

def sol(user_count, k):
    n = len(user_count)

    @lru_cache(None)
    def dp(time, acc, active):
        if time < 2: return 0
        if acc <= 2: return 0
        if active:
            prev_cont = dp(time - 1, acc - 1, True) + user_count[time]
            new_block = dp(time - 3, acc - 3, False) + user_count[time]
            return max(prev_cont, new_block)
        else:
            prev_on = dp(time - 1, acc, True)
            prev_off = dp(time - 1, acc, False)
            return max(prev_on, prev_off)

    return max(dp(n - 1, k, True), dp(n - 1, k, False))

light = lambda l: [randint(0, 25) for i in range(l)]
heavy = lambda l: [randint(150, 200) for i in range(l)]
gen = lambda l, a, b: [randint(a, b) for i in range(l)]
cmp = lambda arr, k, sol=sol: test.assert_equals(attack_plan(arr, k), sol(arr, k))

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

@test.describe("Random Tests")
def rand_tests():

    @test.it("Data with Peaks")
    def peaks():
        cmp(light(5) + heavy(5) + light(5) + heavy(5) + light(5), 14)
        cmp(light(7) + heavy(6) + light(7) + heavy(6), 12)
        cmp(light(2) + heavy(18) + light(6) + heavy(12), 20)

    @test.it("Random Elements")
    def random():
        cmp(gen(30, 0, 50), 12)
        cmp(gen(30, 10, 100), 22)
        cmp(gen(40, 20, 30), 20)
        cmp(gen(50, 20, 30), 20)
        cmp(gen(55, 0, 5), 12)

    @test.it("Large Tests")
    def large():
        for _ in range(50):
            n = randint(400, 450)
            start = randint(30, 120)
            offset = randint(20, 300)
            arr = gen(n, start, start + offset)
            k = randint(20, n >> 1)
            cmp(arr, k)