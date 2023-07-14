import re

"""
    ^ começo da string
    $ final da string

    \w é alfa
    \W não é alfa

    \s caracter vazio
    \S não vazio

    \d numeros de 0 a 9
    \D nao esta entre 0 a 9

    [^a] diferente de caractere "a"

    + uma ou mais
    * 0 ou mais
    ? 0 ou 1
"""


# Pattern
registration_pattern = re.compile("SP[0-9]{7}")

registration = "SP0000000"
registrations = ["SP1234567", "SP1234566", "SP1234560"]
str_registrations = "SP1234567,SP1234566,SP1234560,RG1233567,MA3213dsad,1234567SP"
c_registrations = []

"""fullmatch verifica se a string é exatamente o pattern"""
# x = re.fullmatch(registration_pattern, registration)
# for r in registrations:
#     c_registrations.append(re.fullmatch(registration_pattern, r))

"""search verifica se o pattern esta presente na string (1ª aparição)"""
# x = re.search(registration_pattern, registration)
# for r in registrations:
#     c_registrations.append(re.search(registration_pattern, r))

"""findall: retorna uma lista de aparições numa string"""
# c_registrations = re.findall(registration_pattern, str_registrations)
# print(c_registrations)

# x = re.findall("[^S]", registration)  -> ['P', '0', '0', '0', '0', '0', '0', '0']

# x = re.findall("[a-zA-Z]", registration) -> ['S', 'P']

# x = re.findall("[a-zA-Z0-9]", registration) -> ['S', 'P', '0', '0', '0', '0', '0', '0', '0']

"""Exercicios"""

# CPF
cpf_pattern = "[0-9]{3}\.[0-9]{3}\.[0-9]{3}\.[0-9]{2}"
cpf = "123.455.300.91"
x = re.fullmatch(cpf_pattern, cpf)

# Email
email = "joao@gmail.com.br"
# email_pattern = re.compile("[a-zA-Z0-9]+@gmail.com")
# email_pattern = re.compile("[\w]+@gmail.com")
email_pattern = re.compile("[\w]+@[\w]+\.com[\.\w]*")
x = re.fullmatch(email_pattern, email)
print(x)
