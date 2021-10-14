Thomas opened Vim on his computer, and now he is stuck in it! Help Thomas figure out how to __save the current file__ and __exit__ Vim!

## Task

Thomas' Vim is currently in "Normal" mode.

You are given a `Keyboard` intsobject with the method `key_down` and `key_up`. Invoke the methods with the appropiate keys that executes the command to save and quit Vim.

The keys should be entered in string format:
```python
board.key_down('a') # presses down the 'A' key
board.key_down('shift')  # presses down the 'shift' key
board.key_down('b') # presses 'b'; since 'shift' is already down, the input will be capital 'B'
board.key_up('a') # releases 'a' before pressing it again
board.key_down('a')
```

The above code will enter `aBa` into Thomas's computer.

Good luck!

## Notes
- Valid keys are `a` to `z`, `shift`, `enter` and `;`.
- You must release a key before pressing it again, or Thomas will smash the key into his keyboard and break his computer! Similarly, you mustn't release a key that isn't pressed down.
- All keys must be released at the end of the function!
- For simplicity, all irrelevant commands and features are disabled.

## Hints
- Pressing `;` when `shift` is pressed will enter `:` into the computer.
- Stuck? Check out [this Vim command guide](https://learnbyexample.gitbooks.io/vim-reference/content/Command_Line_mode.html).
- Capitalization of commands matters! `:w` is different from `:W`.
