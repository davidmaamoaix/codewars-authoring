from solution import infer_type
import codewars_test as test

basic_ctx = '''
conv : A -> B
coconv : B -> A

a : A
b : B
'''.strip()

func_ctx = '''
myValue : A
concat : List -> List -> List
append : List -> A -> List
map : (A -> B) -> (List -> List)

conv : (A -> B)
pure : A -> List
'''.strip()

def cmp(a, b, msg=None):
    test.assert_equals(a.replace(' ', ''), b.replace(' ', ''), msg)

def check(ctx, raw, expected):
    cmp(infer_type(ctx, raw), expected, f'Evaluating "{raw}"')

@test.describe("Basic Context")
def tests():
    ctx = basic_ctx

    print('Testing with context:\n')
    print(ctx)

    @test.it("Basic Types")
    def basics():
        check(ctx, 'a', 'A')
        check(ctx, 'b', 'B')
        check(ctx, 'conv', 'A -> B')

    @test.it("Function Application")
    def basic_func():
        check(ctx, 'conv a', 'B')
        check(ctx, 'coconv b', 'A')

    @test.it("Throwing Errors")
    def basic_func():
        test.expect_error('"conv" should not accept type "B"', lambda c=ctx: infer_type(c, 'conv b'))
        test.expect_error('"coconv" should not accept type "A"', lambda c=ctx: infer_type(c, 'coconv a'))
        test.expect_error('"a conv" is ill-formed', lambda c=ctx: infer_type(c, 'a conv'))

@test.describe('Slightly Harder: Functions are Values')
def func_tests():
    ctx = func_ctx

    print('Testing with context:\n')
    print(ctx)

    @test.it("Result should be in simplest form")
    def basics():
        cmp(infer_type(ctx, 'map'), '(A -> B) -> List -> List', 'Checking for simplest form')
        cmp(infer_type(ctx, 'conv'), 'A -> B', 'Checking for simplest form')

    @test.it("Partial Application")
    def partial_app():
        check(ctx, 'map conv', 'List -> List')

    @test.it("Complex Expressions")
    def partial_app():
        check(ctx, 'concat (pure myValue)', 'List -> List')
        check(ctx, 'concat (pure myValue) (pure myValue)', 'List')
        check(ctx, 'concat (map conv (pure myValue))', 'List -> List')
        check(ctx, 'append (concat (map conv (pure myValue)) (pure myValue))', 'A -> List')

    @test.it("Tricky Expression Formatting")
    def tricky_expressions():
        check(ctx, '((concat) ((pure) myValue) (pure (myValue)))', 'List')
        check(ctx, ' map        conv      (pure   (myValue)) ', 'List')

    @test.it("Bad Expressions! Throw Error!")
    def error_check():
        test.expect_error('Too many arguments to "pure"', lambda c=ctx: infer_type(c, 'pure myValue myValue'))
        test.expect_error('Too many arguments to "concat"', lambda c=ctx: infer_type(c, 'concat (pure myValue) (pure myValue) (pure myValue)'))
        test.expect_error('"map conv myValue": "myValue" is not of type "List"', lambda c=ctx: infer_type(c, 'map conv myValue'))
