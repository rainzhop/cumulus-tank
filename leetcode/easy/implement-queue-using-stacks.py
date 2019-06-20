# https://leetcode.com/problems/implement-queue-using-stacks/
#
# Implement the following operations of a queue using stacks.
#
# push(x) -- Push element x to the back of queue.
# pop() -- Removes the element from in front of queue.
# peek() -- Get the front element.
# empty() -- Return whether the queue is empty.
#
# Notes:
# You must use only standard operations of a stack
# -- which means only push to top, peek/pop from top, size, and is empty operations are valid.
#
# Depending on your language, stack may not be supported natively.
# You may simulate a stack by using a list or deque (double-ended queue),
# as long as you use only standard operations of a stack.
#
# You may assume that all operations are valid
# (for example, no pop or peek operations will be called on an empty queue).

class Queue(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.upStack = []
        self.downStack = []


    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.downStack.append(x)


    def pop(self):
        """
        :rtype: nothing
        """
        if self.empty():
            return
        if self.upStack == []:
            while self.downStack != []:
                self.upStack.append(self.downStack.pop())
        self.upStack.pop()


    def peek(self):
        """
        :rtype: int
        """
        if self.empty():
            return
        if self.upStack == []:
            while self.downStack != []:
                self.upStack.append(self.downStack.pop())
        return self.upStack[-1]


    def empty(self):
        """
        :rtype: bool
        """
        return self.upStack == [] and self.downStack == []


if __name__ == '__main__':
    q = Queue()
    print q.empty()
    for i in xrange(0, 10):
        q.push(i)
    print q.peek()
    print q.peek()
    print q.peek()
    for i in xrange(0, 4):
        q.pop()
    print q.peek()
    for i in xrange(0, 4):
        q.push(i)
    for i in xrange(0,100):
        q.pop()
    print q.empty()
