In this kata, you are going to infer the type of an expression based on a given context. Your goal is to implement the `infer_type` function so that it can take in a context like:

```python
"""
myValue : A
concat : List -> List -> List
append : List -> A -> List
map : (A -> B) -> (List -> List)

pure : A -> List
"""
```
and evaluate the type of an expression like:
```python
"append (concat (pure a) (pure a)) a" # should be "List"
```

Each line in the context string is a type declaration that defines what type the value on the left of the `:` should be of: `<value_name> : <type>`. This syntax is similar to declarations in Haskell/Idris.

In the above context, `myValue` is a value of type `A`, and `pure` is a function that takes in a value of type `A` and produces a value of type `List`. `map`, on the other hand, is a function that takes in a function from `A` to `B`, and produces a function from `List` to `List`.

In this kata, the syntax for a `type` is:
```
type := [A-Z][a-zA-Z0-9]*
      | type -> type
      | '(' type ')'
```

Note that the arrow `->` in a type is right associative (due to [currying](https://en.wikipedia.org/wiki/Currying)), i.e. `A -> B -> C -> D` is equivalent to `A -> (B -> (C -> D))`.

The syntax for an `expression` (whose type is to be evaluated by the `infer_type` method) is:
```
expression := [a-z][a-zA-Z0-9]*
            | expression expression
            | '(' expression ')'
```
(the second production rule is function application)

If the expression is ill-formed (e.g. doing `foo param` when `foo` is not a function, or `param` is not of the type that `foo` expects), then throw an error.

## Notes
- Functions are values!!! They can be passed as an argument to another function.
- Functions can be partially applied, e.g. `A -> B -> C` applied to a value of type `A` should be of type `B -> C`.
- Your code must be able to handle extra whitespaces and parentheses in both the context and the expression, e.g. `myFunc:A ->   (((B) -> C))` for context, and `func (val)` for expression.
- The return value of `infer_type` must not contain any unnecessary parentheses, e.g. `A -> (B -> C)` should be written as `A -> B -> C`. The return value is allowed to contain extra spaces though.