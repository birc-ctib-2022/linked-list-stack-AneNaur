"""A linked list implementation of a stack."""

from __future__ import annotations
from dataclasses import dataclass
from typing import Generic, TypeVar, Optional

T = TypeVar('T')


@dataclass
class Link(Generic[T]):
    """A link in a linked list."""

    head: T
    tail: List[T]


List = Optional[Link[T]]

class EmptyStack(Exception):
    pass

class Stack(Generic[T]):
    """A stack of elements of (generic) type T."""

    def __init__(self) -> None:
        """Create a new stack of values of type T."""
        # FIXME: code here
        self.stack = None

    def push(self, x: T) -> None:
        """Push x on the top of this stack."""
        # FIXME: code here
        self.stack = Link(x, self.stack)

    def top(self) -> T:
        """Return the top of the stack."""
        # FIXME: code here
        if self.stack is None:
            raise EmptyStack()
        return self.stack.head

    def pop(self) -> T:
        """Pop the top element off the stack and return it."""
        # FIXME: code here
        if self.stack is None:
            raise EmptyStack()
        x = self.stack.head
        self.stack = self.stack.tail
        return x

    def is_empty(self) -> bool:
        """Test if the stack is empty."""
        # FIXME: code here
        return self.stack == None

stack1 = Stack()
print(stack1.is_empty())
stack1.push(1)
stack1.push(2)
print(stack1.top())
print(stack1.pop())
print(stack1.is_empty())
print(stack1.top())
