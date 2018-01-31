# main

import command

while True:
    query = input(">: ")
    if query == "exit": break
    elif query == 'test':
        import tests
        tests.all()
    else: print(command.query(query))
