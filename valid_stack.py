# _*_ coding=utf-8 _*_


class Stack(object):
    """
    使用列表实现栈
    """

    def __init__(self):
        self.stack = []

    def push(self, element):
        """
        添加元素进栈
        :param element:
        :return:
        """
        self.stack.append(element)

    def pop(self):
        """
        从栈取出元素
        :return:
        """
        return self.stack.pop()

    def get_top(self):
        """
        获取栈顶的元素
        :return:
        """
        if len(self.stack) > 0:
            return self.stack[-1]
        else:
            return

    def is_empty(self):
        return len(self.stack) == 0


def is_valid(s: str) -> bool:
    match = {'{': '}', '(': ')', '[': ']'}
    stack = Stack()
    for i in s:
        if i in match:
            stack.push(i)
        else:
            if stack.is_empty():
                return False
            elif match[stack.pop()] != i:
                return False
    if stack.is_empty():
        return True
    else:
        return False


print(is_valid('({}[(]))'))

