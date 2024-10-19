import os
def lexer(c):
    lex='' 
    arg='' 
    l=True 
    for i in c:
        if i==' ' and l:
            l=False
        elif l:
            lex+=i 
        else:
            arg+=i
    return shell(lex,arg)
def shell(lex,arg):
    if lex=='ls':
        print(arg)
    elif lex=='exit':
        return True
    elif lex=='cd':
        try:
            os.chdir(arg)
        except FileNotFoundError:
            print('Ошибка: Указанный путь не найден.')
while True:
    com=input(os.getcwd()+' # ') # Приглашение
    if lexer(com): break # Проверяем, возвращено ли True