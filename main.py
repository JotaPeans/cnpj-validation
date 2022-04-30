
FSTDIGITLISTNUMBERS = "543298765432"
SNDDIGITLISTNUMBERS = "6543298765432"

listMultOne = []
listMulttwo = []

def rmv_chars(string):
    new_string = string.replace('.', '')
    new_string = new_string.replace('/', '')
    new_string = new_string.replace('-', '')
    return new_string


def verify_number(list):
    number = 11 - (sum(list) % 11)
    return number if number <= 9 else 0


cnpj = input("insira o cnpj que deseja validar (xx.xxx.xxx/xxxx-xx): ")
old_cnpj = rmv_chars(cnpj)

cnpjWoutChars = rmv_chars(cnpj)
cnpjWoutChars = cnpjWoutChars[:-2]

try:
    for index in range(len(cnpjWoutChars)):
        num = int(cnpjWoutChars[index]) * int(FSTDIGITLISTNUMBERS[index])
        listMultOne.append(num)

    firstnumber = str(verify_number(listMultOne))
    cnpjWoutChars += firstnumber

    for index in range(len(cnpjWoutChars)):
        num = int(cnpjWoutChars[index]) * int(SNDDIGITLISTNUMBERS[index])
        listMulttwo.append(num)

    secondnumber = str(verify_number(listMulttwo))
    cnpjWoutChars += secondnumber

    new_cnpj = cnpjWoutChars

    print("\nCNPJ válido" if new_cnpj == old_cnpj else "\nCNPJ invalido")
except:
    print("\nCNPJ inválido")