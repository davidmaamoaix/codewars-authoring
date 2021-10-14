_This kata is a harder version of [A Bubbly Programming Language](https://www.codewars.com/kata/5f7a715f6c1f810017c3eb07). If you haven't done that, I would suggest doing it first._

You are going to make yet another interpreter similar to [A Bubbly Programming Language](https://www.codewars.com/kata/5f7a715f6c1f810017c3eb07), but with completely different syntax.

Your goal is to create an interpreter for a programming language (bubbly language) with the following tokens:

~~~if:python,
- `start`: marks the start of a program
- `return_` (`return_ <value>`): marks the end of a program, and returns the given `<value>`
- `let` (`let <var_name> <value>`): sets the variable `<var_name>` to the given `<value>`
- `add` (`add <value> <value>`) returns the sum of the two `<value>`
- `sub` (`sub <value> <value>`) returns the result of the first `<value>` minus the second `<value>`
- `mul` (`mul <value> <value>`) returns the product of the two `<value>`
- `div` (`div <value> <value>`) returns the result of the first `<value>` divided by the second `<value>` (integer division)
~~~
~~~if:javascript,
- `start`: marks the start of a program
- `return_` (`return_ <value>`): marks the end of a program, and returns the given `<value>`
- `let_` (`let_ <var_name> <value>`): sets the variable `<var_name>` to the given `<value>`
- `add` (`add <value> <value>`) returns the sum of the two `<value>`
- `sub` (`sub <value> <value>`) returns the result of the first `<value>` minus the second `<value>`
- `mul` (`mul <value> <value>`) returns the product of the two `<value>`
- `div` (`div <value> <value>`) returns the result of the first `<value>` divided by the second `<value>` (integer division )
~~~

Each `<value>` can either be an integer (immediate value), a string (value of the variable), or an operator (`add`, `sub`, etc) (return value of the operator).

An example code in the bubbly language (but without the bubbles) looks like:

```python
start
let 'my_var' add 5 8
let 'banana' mul 'my_var' 2
return_ 'banana'
```
```javascript
start
let_ 'my_var' add 5 8
let_ 'banana' mul 'my_var' 2
return_ 'banana'
```

and is equivalent to this pseudo code:

```
let my_var = 5 + 8
let banana = my_var * 2
return banana
```

and should return `26`.

Just like the easier counterpart of this kata, each token must be engulfed by a bubble (parenthesis)!

So the above code should look like:

```python
(start)(let)('my_var')(add)(5)(8)(let)('banana')(mul)('my_var')(2)(return_)('banana')
```
```javascript
(start)(let_)('my_var')(add)(5)(8)(let_)('banana')(mul)('my_var')(2)(return_)('banana')
```

and returns `26`.

~~~if:python,
Your goal is to create appropiate definitions for `start`, `let`, `return_`, `add`, `sub`, `mul`, `div` so that the bubbly language is valid Python syntax.
~~~
~~~if:javascript,
Your goal is to create appropiate definitions for `start`, `let_`, `return_`, `add`, `sub`, `mul`, `div` so that the bubbly language is valid JavaScript syntax.
~~~

More examples:

```python
>>> (start)(let)('x')(20)(return_)(sub)(10)('x')
-10

>>> (start)(return_)(mul)(10)(15)
150
```
```javascript
>>> (start)(let_)('x')(20)(return_)(sub)(10)('x')
-10

>>> (start)(return_)(mul)(10)(15)
150
```

## Extra Requirements

~~~if:python,
___Custom classes are not allowed in the solution___, as Python's \_\_call\_\_ overloading makes this problem too trivial. Your solution must use functions and lambdas to achieve this instead (the `class` and `type` keywords are banned! _Muhahahahahaha!_).
~~~
~~~if:javascript,
_**`Proxy`s are not allowed as solutions**_, as `call` overloading makes this problem too trivial. Your solution must use functions to achieve this instead ( `start`, `let_`, `return_`, `add`, `sub`, `mul` and `div` will be tested to be actual functions ).
~~~

___In addition, your interpreter should allow nested operators___. Since each operator takes in exactly `2` parameters, it is possible to deduce the hierarchy of the nested structure.

This:

```
add add 5 add 3 2 5
```

has this structure:

```
add(add(5, add(3, 2)), 5)
```

And therefore this should be valid syntax:

```python
>>> (start)(return_)(add)(add)(5)(add)(3)(2)(5)
15
```

__Lastly, there will be partial code__.
```python
>>> f = (start)(let)('a')(20)(return_)(add)('a')
>>> (f)(10)
30
>>> (f)(5)
25
```

## Notes

- There will be no indication of line-breaks (or end of statement) in bubbly language. You will need to deduce that from the tokens yourself.

- You may assume that all inputs are valid.

~~~if:python,
- `eval` and `exec` are also not allowed.
~~~
~~~if:javascript,
- Division is _integer division._ Truncate results, instead of rounding up or down, and assume full JS safe integer range! so `x | 0` won't work; you'll have to use `Math.trunc(x)`.
~~~
