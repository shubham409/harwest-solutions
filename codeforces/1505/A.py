try: 
    while True: 
        inp = input() 
        if inp == "Is it rated?": 
           print('NO')
        else: 
            break 
except EOFError: 
    pass 