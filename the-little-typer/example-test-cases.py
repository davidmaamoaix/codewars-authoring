from solution import infer_type
import codewars_test as test


def cmp(a, b, msg=None):
    if a is None:
        return test.fail('Return type must not be None')

    test.assert_equals(a.replace(' ', ''), b.replace(' ', ''), msg)

def check(ctx, raw, expected):
    cmp(infer_type(ctx, raw), expected, f'Evaluating "{raw}"')

@test.describe("Basic Context")
def tests():
    ctx = '''
    conv : A -> B
    coconv : B -> A

    a : A
    b : B
    '''.strip()
    ctx = '\n'.join(i.strip() for i in ctx.split('\n') if i)

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
        test.expect_error('"banana" is undefined', lambda c=ctx: infer_type(c, 'conv banana'))

@test.describe('Slightly Harder: Functions are Values')
def func_tests():
    ctx = '''
    myValue : A
    concat : (List -> (List -> (List)))
    append : List->    A->List
    map  :  (A   ->   B) -> (List -> List)

    conv : (A->B)
    pure  : A->List
    '''.strip()
    ctx = '\n'.join(i.strip() for i in ctx.split('\n') if i)

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

@test.describe('Harder: Some Compositions')
def func_tests():
    ctx = '''
    id : (A -> B) -> (B -> A) -> (A -> A)
    inv : (A -> B) -> (B -> A)

    a:A
    b:B
    c:A
    d:B

    aB : A -> B
    bA : B -> A
    '''.strip()
    ctx = '\n'.join(i.strip() for i in ctx.split('\n') if i)

    print('Testing with context:\n')
    print(ctx)

    @test.it("Functions are Values")
    def basics():
        check(ctx, 'inv  ( aB )  b', 'A')
        check(ctx, 'inv  ( aB )  d', 'A')
        check(ctx, '( ( id  aB )  bA )', 'A -> A')
        check(ctx, '( ( id  aB )  bA ) a', 'A')
        check(ctx, '( ( id  aB )  bA ) c', 'A')
        check(ctx, 'aB  ( ( ( id  aB )  bA ) c )', 'B')
        check(ctx, 'bA ( aB  ( ( ( id  aB )  bA ) c ) )', 'A')
        check(ctx, '( ( id  aB )  bA ) ( bA ( aB  ( ( ( id  aB )  bA ) c ) ) )', 'A')