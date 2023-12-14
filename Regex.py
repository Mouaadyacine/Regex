import re
def isCharinSTR(mot, chaine):
    pattern = re.escape(mot)
    match = re.search(pattern, chaine)
    return bool(match)

def isDigitInSTR(chaine):
    match = re.search(r"\d" , chaine)
    return bool(match)

def replace(chaine):
    match = re.sub(r"\s" , "-" , chaine )
    return bool(match) 

def verifyNumber(num):
    match = re.search(r"^\d{2}-\d{3}-\d{4}$" , num)
    return bool(match) 


def verifie_email(email):
    match = re.search(r"^\w+@\w+\.(com)$" , email)
    return bool(match)