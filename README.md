# IntCode

An advent tale of suffering, self improvements, torrijas (torrijas), ultrawide monitors and intcode.

## Installation

You can install `intcode` from Pypi via your favourite dependency manager:

```
pipenv install intcode
```

## Usage

If you are trying to use this library, this means that you probably failed the 2019 Advent of Code.

See, I nearly failed myself. 

I tried keeping up the pace of one kata a day, but december was a busy month for me!
It is my birthday and, in addition to this, I was responsible of a big ass deployment in the middle of the week and 
I had to work late.

For the sake of my own mental health, I stopped AoC all together and planned to quit, 
but my AoC-addict friend [@jenarvaez](https://github.com/jenarvaezg/) (famous creator of the brother in law bot) 
talked me into giving it another try.

Thank you man! I really enjoy doing this kind of shit with you!

Anyways, this is how to use it:

```python
from intcode import IntCodeMachine
from intcode.handlers.io.stack import StackIOHandler

code = "3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9"
stack_io_handler = StackIOHandler(["7"])
machine = IntCodeMachine(code, io_handler=stack_io_handler) # If not provided, io will be handled by std
machine.run()
print(stack_io_handler.io_stack)
```

Proper documentation will roll out in a few days