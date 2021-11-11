

class Stack:
    def __init__(self, list_stack):
        self.list_stack = list_stack

    '''isEmpty - проверка стека на пустоту. Метод возвращает True или False.'''
    def isEmpty(self):
        if not self.list_stack:
            return True
        else:
            return False

    '''push - добавляет новый элемент на вершину стека. Метод ничего не возвращает.'''
    def push(self, item_stack):
        self.list_stack = self.list_stack + item_stack
        return

    '''pop - удаляет верхний элемент стека. Стек изменяется. Метод возвращает верхний элемент стека'''
    def pop(self):
        self.list_stack = self.list_stack[0:-1]
        return self.list_stack[-1]

    '''peek - возвращает верхний элемент стека, но не удаляет его. Стек не меняется.'''
    def peek(self):
        return self.list_stack[-1]

    '''size - возвращает количество элементов в стеке'''
    def size(self):
        return len(self.list_stack)

    def correct_stack(self, text):
        while '()' in text or '[]' in text or '{}' in text:
            text = text.replace('()', '')
            text = text.replace('[]', '')
            text = text.replace('{}', '')

        if not text:
            rezult = 'Сбалансированно'
        else:
            rezult = 'Несбалансированно'

        return rezult

my_list = '{{[(])]}}'

stack = Stack(my_list)

print()
print('=== isEmpty ===')
print(stack.isEmpty())

print()
print('=== push ===')
stack.push('678')
print(stack.peek())

print()
print('=== pop ===')
print(stack.pop())


print()
print('=== peek ===')
print(stack.peek())

print()
print('=== size ===')
print(stack.size())

print()
print('=== correct ===')
text = input('Введите стек: ')
print(stack.correct_stack(text))
