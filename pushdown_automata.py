'''
    ** Program by Rafi Mochamad Fahreza **

    q1 = [q1, q2] --> state yang digunakan
    I = [a,b] -> jenis inputan yang akan diterima
    δ digantikan dengan 'pop'
    di persilahkan untuk menambahkan func_transition
'''

class Push_Automata:

    def __init__(self):
        self.stack = ['Z']

    def transitions(self, state):
        func_transition = {
                                        ('q1', 'a', 'Z' ) : ['q1', 'A'] ,
                                        ('q1', 'b' ,'Z') : ['q2', 'B'],
                                        ('q1','a', 'A') : ['q1', 'A'],
                                        ('q1', 'b', 'A') : ['q2', 'pop'],
                                        ('q1', 'a', 'B') : ['q2', 'pop'],
                                        ('q1','b','B') : ['q2', 'B'],
                                        ('q1','pop', 'Z') : ['q2', 'Z']
                                        }
        return func_transition[state][-1]

    def solve(self, string):

        for letter in string:
            item = self.transitions(('q1', letter, self.stack[-1]))
            if item == 'pop':
                self.stack.pop()
            else:
                self.stack.append(item)

        if self.stack[-1] != 'Z' :
            return 'TIDAK DAPAT DI TERIMA'
        return 'DI TERIMA' 

print(Push_Automata().solve('ab'))
print(Push_Automata().solve('aaabbb'))
print(Push_Automata().solve('aa'))
print(Push_Automata().solve('aba'))
            
    
