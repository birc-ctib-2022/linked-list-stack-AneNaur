"""Testing our stack implementation."""

from stack import EmptyStack, Stack
import pytest


def test_me() -> None:
    """I really hope you test your code."""
    assert 2 + 2 == 4

def test_push() -> None:
    stack1 = Stack()
    stack1.push(1)
    assert stack1.is_empty() == False

def test_top() -> None:
    stack2 = Stack()
    stack2.push(1)
    assert stack2.top()==1

def test_pop() -> None:
    stack3 = Stack()
    stack3.push(1)
    stack3.pop()
    assert stack3.is_empty()==True

def test_exception() -> None:
    stack4 = Stack()
    with pytest.raises(EmptyStack):
        stack4.pop()
        stack4.top()
