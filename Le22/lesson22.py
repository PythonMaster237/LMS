def linear_shift(array: list, shift: int) -> list:
    '''
    array = [1, 2, 3, 4] shift = 1 => [0, 1, 2, 3]
    array = [1, 2, 3, 4] shift = 2 => [0, 0, 1, 2]
    array = [1, 2, 3, 4] shift = 3 => [0, 0, 0, 1]
    '''
    new_list = []
    shift = abs(int(shift))
    for i in range(shift):
        new_list.append(0)
    for i in range(len(array) - shift):
       new_list.append(array[i])
    return new_list


def circular_shift(array: list, shift: int) -> list:
    '''
    array = [1, 2, 3, 4] shift = 1 => [4, 1, 2, 3]
    array = [1, 2, 3, 4] shift = 2 => [3, 4, 1, 2]
    array = [1, 2, 3, 4] shift = 3 => [2, 3, 4, 1]
    '''
    new_list = []
    shift = abs(int(shift))
    for i in range(shift, 0, -1):
        new_list.append(array[len(array) - i])
    for j in range(len(array) - shift):
       new_list.append(array[j])
    return new_list



def nested_parentheses(incoming: str) -> bool:
    '''
    Функція отримує рядок, який складається тільки зі знаків "(" або ")"
    Рядок вважається таким, що містить коректно вкладені скобки, якщо для
    кожної скобки "(" існує відповідна ")". 
    Функція повертає булевську змінну, яка показує, чи містить вхідний рядок
    тільки правильно вкладені скобки - True, чи ні - False

    incoming = "((())(())())" => True
    incoming = "" => True
    incoming = "(((())))" => True
    incoming = "())" => False
    incoming = "(()()(())" => False
    '''
    if incoming.count('(') == incoming.count(')'):
        return True
    else:
        return False

test_list1 = [1, 2, 3, 4]

incoming1 = "((())(())())"
incoming2 = ""
incoming3 = "(((())))"
incoming4 = "())"
incoming5 = "(()()(())"

if __name__ == '__main__':
    print(nested_parentheses(incoming1))
    print(nested_parentheses(incoming2))
    print(nested_parentheses(incoming3))
    print(nested_parentheses(incoming4))
    print(nested_parentheses(incoming5))

    print(linear_shift(test_list1, 2))
    print(circular_shift(test_list1, 2))