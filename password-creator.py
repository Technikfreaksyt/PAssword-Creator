import secrets
import string



auswahl = string.digits + string.ascii_letters + string.punctuation
 
print(len(auswahl)) 
print('Mit 5 Zeichen:')
print(''.join(secrets.choice(auswahl) for _ in range(5)))
print('         ')
print('Mit 10 Zeichen')
print(''.join(secrets.choice(auswahl) for _ in range(10)))
print('   ')
print('Mit 20 Zeichen')
print(''.join(secrets.choice(auswahl) for _ in range(20)))
print('')
print('Mit 30 Zeichen')
print(''.join(secrets.choice(auswahl) for _ in range(30)))
print('    ')
print('Mit 40 Zeichen')
print(''.join(secrets.choice(auswahl) for _ in range(40)))
print('   ')
print('Mit 50 Zeichen')
print(''.join(secrets.choice(auswahl) for _ in range(50)))



      
        




