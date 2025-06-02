from itertools import product

def solution(word):
    letters = ['A', 'E', 'I', 'O', 'U']
    alpha_list = []
    
    for i in range(1, 6):
        alpha_list += list(product(letters, repeat = i))
        
    alpha_list.sort()
    for i in range(len(alpha_list)):
        alpha_list[i] = "".join(alpha_list[i])
    
    for i in range(len(alpha_list)):
        if alpha_list[i] == word:
            return i + 1
    
    return 0