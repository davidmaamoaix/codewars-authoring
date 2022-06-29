from solution import infer_type
import codewars_test as test

from itertools import product
from functools import reduce
from random import shuffle, randint, choice

adjs = [
    'adorable', 'big', 'small', 'amused', 'angry',
    'annoyed', 'anxious', 'arrogant', 'attractive', 'average',
    'bad', 'beautiful', 'bewildered', 'bloody', 'blushing',
    'bored', 'brainy', 'brave', 'breakable', 'bright',
    'busy', 'calm', 'careful', 'cautious', 'charming'
]

ppl = [
    'B4B', 'AwesomeAD', 'TwilightSun', 'Luksona', 'Madjosz',
    'Hobovsky', 'MikChan', 'Kacarott', 'Eloise', 'Ejini',
    'Johan', 'Voile', 'Ice', 'Monadius', 'Kazk'
]

# rand_id = [a + b for a, b in product(adjs, ppl)]
# shuffle(rand_id)

alp = 'abcdefghijklmnopqrstuvwxyz'
alpnum = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'

def get_id(is_type=False):
    start = choice(alp).upper() if is_type else choice(alp)
    return start + ''.join(choice(alpnum) for i in range(randint(4, 8)))


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

@test.describe('Basic "Random" Test')
def rand_id_tests():
    a, b = get_id(), get_id()
    A, B, C = get_id(True), get_id(True), get_id(True)
    abc, bca, comp = get_id(), get_id(), get_id()
    ctx = f'''
        {comp} : (((({B} -> (({C})))))) -> (({C} -> {A})) ->  ({B} -> {A})

        {a} : {A}
        {b} : {B}

        {abc} : {A} -> ({B} -> {C})
        {bca} : {B} -> ({C} -> {A})
    '''
    ctx = '\n'.join(i.strip() for i in ctx.split('\n') if i)

    print('Testing with context:\n')
    print(ctx)

    @test.it("Basics & Function Application")
    def basics():
        check(ctx, a, A)
        check(ctx, b, B)
        check(ctx, abc, f'{A} -> {B} -> {C}')

    @test.it("Partial Application")
    def basics():
        check(ctx, f'{comp} ({abc} {a})', f'({C} -> {A}) -> {B} -> {A}')
        check(ctx, f'{comp} ({abc} {a}) ({bca} {b})', f'{B} -> {A}')
        check(ctx, f'{comp} ({abc} {a}) ({bca} {b}) {b}', f'{A}')

    @test.it("Throwing Errors")
    def basics():
        test.expect_error(
            'Unexpected function application', lambda c=ctx: infer_type(c, f'{a} {b}')
        )
        test.expect_error(
            'Type error', lambda c=ctx: infer_type(c, f'{comp} ({bca} {b}) ({abc} {a})')
        )
        test.expect_error(
            'Type error', lambda c=ctx: infer_type(c, f'{comp} ({abc} {a}) {comp}')
        )
        test.expect_error(
            'Type error', lambda c=ctx: infer_type(c, f'{comp} ({abc} {a}) {b} {a}')
        )

@test.describe('More Type Errors')
def error_check_tests():
    a, b, c, d, abc, abcd = get_id(), get_id(), get_id(), get_id(), get_id(), get_id()
    A, B, C, D = get_id(True), get_id(True), get_id(True), get_id(True)
    ctx = f'''
    {abcd}:{A} -> ({B} -> {C})   -> {C} -> {D}
    {a}  :  {A}
    {b}:{B}
    {c} :{C}
    {abc}:({A} -> {B}) -> {C}
    '''
    ctx = '\n'.join(i.strip() for i in ctx.split('\n') if i)

    @test.it('Functions as Parameters')
    def abc():
        test.expect_error(
            'Type error', lambda c=ctx: infer_type(c, f'{abc} {a}')
        )
        test.expect_error(
            'Type error', lambda c=ctx: infer_type(c, f'{abcd} {a} {b}')
        )

    @test.it('Undefined Values')
    def undefined():
        test.expect_error(
            'Undefined value', lambda c=ctx: infer_type(c, f'{abcd} {a} {get_id()}')
        )


def to_str(arr, add_parens=False):
    if isinstance(arr, str):
        return arr

    tps = [to_str(arr[i], i != len(arr) - 1) for i in range(len(arr))]
    inner = ' -> '.join(tps)
    return f'({inner})' if add_parens else inner

# Random tests
# This tree represents an expression
class Node:

    def __init__(self, name, tp=None):
        self.name = name
        self.tp = tp
        self.subs = []

    def __str__(self, simple=True):
        return f'Node<{self.name}>(' + ', '.join(str(i) for i in self.subs) + ')'

    def gen_type(self, simple=True):
        if self.tp is not None: return

        if not self.subs:
            self.in_tp = []
            self.out_tp = get_id(True)
            return

        for i in self.subs: i.gen_type(simple)
        self.in_tp = [i.out_tp for i in self.subs]

        # results in another func, not a single value
        if not simple and randint(0, 100) < 65:
            self.out_tp = [
                get_id(True) if randint(0, 100) < 35 else choice(self.in_tp)
                for _ in range(randint(2, 3))
            ]
        else:
            self.out_tp = get_id(True)

    def get_type_repr(self):
        out_list = [self.out_tp] if isinstance(self.out_tp, str) else self.out_tp
        return to_str(self.in_tp + out_list)

    def gather(self, collector):
        collector.append(f'{self.name} : {self.get_type_repr()}')
        for i in self.subs: i.gather(collector)

    def get_exp(self, add_parens=False):
        if not self.subs:
            return self.name

        inner = ' '.join([self.name] + [i.get_exp(True) for i in self.subs])
        return f'({inner})' if add_parens else inner


def gen_random_tree(nodes):
    root = Node(get_id())
    collector = [root]

    for _ in range(nodes):
        new_node = Node(get_id())
        rand_node = choice(collector)

        rand_node.subs.append(new_node)
        collector.append(new_node)

    return root, collector


@test.describe('Complete Random Tests')
def complete_rand_tests():

    def test_tree(nodes, errno=0):
        root, nodes = gen_random_tree(nodes)
        root.gen_type(False)
        ans = to_str(root.out_tp)

        ctx_list = []
        root.gather(ctx_list)

        extra = get_id()
        extra_tp = get_id(True)
        if errno == 1: # undefined var
            rand_node = choice(nodes)
            rand_node.name = extra
        elif errno == 2: # wrong type
            rand_node = choice(nodes)
            rand_node.name = extra
            rand_node.tp = extra_tp
            ctx_list.append(f'{extra} : {extra_tp}')
        elif errno == 3: # too many params
            rand_nodes = [i for i in nodes if i.subs]
            rand_node = choice(rand_nodes)
            new_node = Node(extra, extra_tp)
            rand_node.subs.append(new_node)
            ctx_list.append(f'{extra} : {extra_tp}')

        exp = root.get_exp()
        shuffle(ctx_list)
        ctx = reduce(
            lambda a, b: a + ('\n' if randint(0, 100) < 91 else '\n\n') + b, ctx_list
        )

        if errno == 0:
            check(ctx, exp, ans)
        elif errno == 1:
            test.expect_error(
                f'Error expected: Value "{extra}" is not defined but no error is raised',
                lambda c=ctx, e=exp: infer_type(c, e)
            )
        elif errno == 2:
            test.expect_error(
                f'Error expected: Value "{extra}" is not acceptable here',
                lambda c=ctx, e=exp: infer_type(c, e)
            )
        elif errno == 3:
            test.expect_error(
                f'Error expected: Extra parameter "{extra}"',
                lambda c=ctx, e=exp: infer_type(c, e)
            )

    @test.it('Correctly infer the type of the expression (small)')
    def smol_correct():
        for _ in range(randint(10, 25)):
            test_tree(randint(5, 7))

    @test.it('Correctly infer the type of the expression (large)')
    def big_correct():
        for _ in range(randint(75, 150)):
            test_tree(randint(10, 50))

    @test.it('Detects type error correctly (small)')
    def smol_incorrect():
        for _ in range(randint(10, 25)):
            test_tree(randint(5, 7), randint(1, 3))

    @test.it('Detects type error correctly (large)')
    def smol_incorrect():
        for _ in range(randint(50, 100)):
            test_tree(randint(10, 50), randint(1, 3))
