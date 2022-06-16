The `concat` function on lists has the following type:
```haskell
concat :: [[a]] -> [a]
```

Simply put, it flattens a list:
```haskell
concat [[1, 2], [3, 4], [], [5]] == [1, 2, 3, 4, 5]
```

Farmer Thomas wants to write `concat` in terms of `foldr`. Specifically, he wants you to find `p`, `q` and `r` such that:
```
concat = foldr (foldr p q) r
```

Now get working!

After doing this one, you may want to check out [Lambda Calculus: Lists as folds II](https://www.codewars.com/kata/60b76ecdbec5c4003163f869/haskell)  (this might act as a hint for this kata :P).
