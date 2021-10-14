from solution import help_me_exit_vim_or_i_will_miss_mid_term_due_and_fail_fp_course
import codewars_test as test

from preloaded import Keyboard

@test.describe("Escaping Vim")
def tests():

    keyboard = Keyboard()
    help_me_exit_vim_or_i_will_miss_mid_term_due_and_fail_fp_course(keyboard)

    @test.it("Did Thomas' keyboard survive?")
    def keyboard_ok():
        test.expect(not keyboard.broken, "You broke Thomas\' keyboard!")

    @test.it("Are all keys released after function ends?")
    def keyboard_empty():
        test.assert_equals(keyboard.pressed, [], 'Some keys are not released!')

    @test.it("Is Vim closed?")
    def thomas_happy():
        test.expect(keyboard.saved, "You didn't save the file! Thomas lost all his work!")
        test.expect(keyboard.closed, "Vim isn't closed!")
