# MinusMinus
MinusMinus is a minimalistic programming language, much more so than my first attempt at that, [Minus](https://github.com/vanjac/Minus/). The entire interpreter is 95 lines of Python 3 code, and it was written during a long plane ride using the iPhone app "Pythonista 3."

An example program is included.

Some fun features of MinusMinus:
- **No error checking:** MinusMinus silently ignores all errors, throws an unrelated exception, or does something stranger.
- **Broken hash codes:** MinusMinus uses a bad hash code algorithm for variable names. If two different variables have the same hash code, they are treated as the same.
- **No memory deallocation:** MinusMinus has commands to allocate memory, but not to free it. As a result, badly written programs will constantly grow in size until they reach the 512KB limit and start writing to variable memory (without any errors of course).
- **Whitespace:** Due to the design, MinusMinus is very picky about whitespace. Some characters (like `[` and `]` work with no whitespace surrounding them, whereas other characters (like `+` and `-`) do not.
- **No documentation:** I'm too lazy, so you'll just have to figure it out.

This combination of features results in a unique development experience.

To use, pipe the program to standard input. The result is a list of numbers.
