import random as rd
from passwd_generator import chars_lists


lower_letters, numbers, cap_letters, special_char = chars_lists()
del cap_letters
del special_char


def default_mail(domain='popular'):
    if domain == 'any':
        file = open('data/domains/all_email_provider_domains.txt')
        domain_file = file.readlines()
        file.close()
        domain = list(domain_file[rd.randint(0, 6013)])
        domain.remove('\n')
        domain = ''.join(str(x) for x in domain)
    elif domain == 'popular':
        domain = rd.choice(['gmail.com', 'yahoo.com', 'icloud.com', 'hotmail.com', 'protonmail.com', 'outlook.com'])

    lang = rd.choice(['ar', 'en'])
    fn_file = open(f"data/names/{lang}_firstname.txt", 'r')
    firstname = fn_file.readlines()
    fn_file.close()
    sn_file = open(f"data/names/{lang}_surname.txt", 'r')
    surname = sn_file.readlines()
    sn_file.close()

    if lang == 'ar':
        fn = list(firstname[rd.randint(0, 228)])
        sn = list(surname[rd.randint(0, 118)])
    elif lang == 'en':
        fn = list(firstname[rd.randint(0, 119)])
        sn = list(surname[rd.randint(0, 149)])

    fn.remove('\n')
    sn.remove('\n')
    fn = ''.join(str(x) for x in fn)
    sn = ''.join(str(x) for x in sn)

    mail = list()
    mail.append(sn)
    mail = mail + rd.choices(numbers, k=rd.randint(2, 5))
    rd.shuffle(mail)
    mail.insert(0, fn)
    mail = ''.join([str(x) for x in mail])
    mail = mail + f'@{domain}'
    return fn, sn, mail


if __name__ == '__main__':
    print(default_mail())

