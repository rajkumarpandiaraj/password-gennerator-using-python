import random

def createPassword(password, randomPassChar) :
    print(randomPassChar)
    splChar = ['!','#','%','^','&','*'] * 5
    Numbers = ['1','2','3','5','6','7','8','9','0'] * 5
    low = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'] * 3
    up = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'] * 3
    random.shuffle(splChar)
    random.shuffle(Numbers)
    random.shuffle(low)
    random.shuffle(up)

    if randomPassChar == 's' :
        password += splChar[random.randrange(0, len(splChar))]
        return password
    if randomPassChar == 'n' :
        password += Numbers[random.randrange(0, len(Numbers))]
        return password
    if randomPassChar == 'l' :
        password += low[random.randrange(0, len(low))]
        return password
    if randomPassChar == 'u' :
        password += up[random.randrange(0, len(up))]
        return password
        

print("Enter the number of char you want in password")
print('minimun 8 to maximum 20')
numOfChar = int(input())
if 8 <= numOfChar <= 20 :
    print("Type 's' for special char")
    print("Type 'n' for numbers")
    print("Type 'u' for uppercase char")
    print("Type 'l' for lowercase char")
    print("Example :")
    print("snl include the specialchar/number/lowercase in the password")
    passChar = input('Enter the char you want in password : ').lower()
    passCharList = ['s', 'n', 'l', 'u']
    passCharResult = True
    for i in passChar :
        if i in passCharList :
            print('ok')
        else : 
            passCharResult = False
            print('Please enter the valid char')
            break
    if passCharResult :
        password = ''
        for i in range(0, 20) :
            tempPassChar = passChar
            randomPassChar = tempPassChar[random.randint(0, len(passChar)-1)]
            tempPassword = createPassword(password, randomPassChar)
            password += tempPassword
        print(password[:numOfChar])



else :
    print('Please, Enter the  value between 8-20')