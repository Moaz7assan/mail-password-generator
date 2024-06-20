from rich.console import Console
from rich.table import Table
from rich import print
import pyfiglet
from passwd_generator import default_passwd, custom_passwd
from mail_generator import default_mail
from colllection import default_collection, custom_collection

 
welcome_msg = pyfiglet.figlet_format('G e n e r a t o r', font='big')
print(welcome_msg)

console = Console()


def mail():
    while True:
        print('1 - Popular Mail Domain Providers\n2 - Randomly Choose Any Mail Domain Providers')
        mail_choice = input('>> ')

        match mail_choice:
            case '1':
                firstname, surname, mail = default_mail('popular')
                break
            case '2':
                firstname, surname, mail = default_mail('any')
                break
            case _:
                print('enter a valid choice')

    mail_table = Table()
    mail_table.add_column("Name", justify="left", style="cyan", no_wrap=True)
    mail_table.add_column("Mail", justify="center", style="magenta", no_wrap=True)
    mail_table.add_column("Suggested Password", justify="center", style="green", no_wrap=True)

    mail_table.add_row(firstname + ' ' + surname, mail, default_passwd())
    console.print(mail_table)
    work_again()


def passwd():
    pass_table = Table()
    pass_table.add_column('Strong Password', justify='center')
    pass_table.add_row(default_passwd(), style='green')
    console.print(pass_table)
    work_again()


def collection_saver(df, table):
    while True:
        print('1 - Watch the collection in the terminal\n2 - Save it as .xlsx file at the same path'
              '\n3 - Do both')
        collection_choice = input('>> ')
        match collection_choice:
            case '1':
                console.print(table)
                work_again()
                break
            case '2':
                df.to_excel("Generated_Mails_Collection.xlsx")
                print('Saved as "Generated_Mails_Collection.xlsx" !!')
                work_again()
                break
            case '3':
                console.print(table)
                df.to_excel("Generated_Mails_Collection.xlsx")
                print('Saved as "Generated_Mails_Collection.xlsx" !!')
                work_again()
                break


def collection():
    print('Enter the Collection Length')
    while True:
        try:
            length = input('>> ')
            length = int(length)
            if length >= 1:
                break
            else:
                print('Please enter a valid positive integer.')
        except ValueError:
            print('Please enter a valid integer.')

    while True:
        print('1 - Popular Mail Domain Providers\n2 - Randomly Choose Any Mail Domain Providers')
        mail_choice = input('>> ')

        match mail_choice:
            case '1':
                length = int(length)
                df, table = default_collection(length, 'popular')
                break
            case '2':
                length = int(length)
                df, table = default_collection(length, 'any')
                break
            case _:
                print('enter a valid choice')
    collection_saver(df, table)


def custom_mail_input():
    print('Enter the custom mail domain')
    custom_domain = input('>> ')
    firstname, surname, mail = default_mail(custom_domain)
    table = Table(title='Custom Mail')
    table.add_column("Name", justify="left", style="cyan", no_wrap=True)
    table.add_column("Mail", justify="center", style="magenta", no_wrap=True)
    table.add_row(firstname + ' ' + surname, mail)
    return table, custom_domain


def custom_pass():
    print('Enter the number of [bold green]Lows letters[/bold green], [bold green]Numbers[/bold green],'
          ' [bold green]Caps letters[/bold green], [bold green]Special characters[/bold green] '
          '\nand leave space between the values'
          '\n\nfor example >>[bold green] 10 5 2 3 [/bold green]\n')
    while True:
        values = input('>> ').split()
        try:
            values_dict = {
                'lower_letters': int(values[0]),
                'numbers': int(values[1]),
                'cap_letters': int(values[2]),
                'special_char': int(values[3])
            }

            pass_table = Table()
            pass_table.add_column('Custom Password', justify='center')
            pass_table.add_row(custom_passwd(values_dict), style='green')

            break
        except:
            print("Invalid input: Please enter valid numeric values separated by spaces.")

    return pass_table, values_dict


def advanced():
    while True:
        print('\n1 - Mail\n2 - Password\n3 - Collection\n')
        advanced_choice = input('>> ')
        match advanced_choice:
            case '1':
                table, domain = custom_mail_input()
                del domain
                console.print(table)
                work_again()
            case '2':
                pass_table, values_dict = custom_pass()
                console.print(pass_table)
                work_again()
            case '3':
                print('Enter the Collection Length')
                while True:
                    try:
                        length = input('>> ')
                        length = int(length)
                        if length >= 1:
                            break
                        else:
                            print('Please enter a valid positive integer.')
                    except ValueError:
                        print('Please enter a valid integer.')
                y, domain = custom_mail_input()
                del y
                df, table = custom_collection(length, domain)
                collection_saver(df, table)

            case _:
                print('Enter a valid choice')


def main():
    print("1 - Generate a Mail\n2 - Generate a strong Password\n3 - Generate a Collection of Mails and Passwords"
          "\n0 - Advanced\n'to quite press q'")
    choice = input('>> ')
    if choice.lower() in ['1', '2', '3', '4', '0', 'q']:
        match choice.lower():
            case '1':
                mail()
            case '2':
                passwd()
            case '3':
                collection()
            case '0':
                advanced()
            case 'q':
                quit()
    else:
        print('Please enter a valid choice')
        main()


def work_again():
    choice = input('do u wish to start again? (y/n) >> ').lower()
    if choice == 'y':
        main()
    else:
        print('see you later, quiting...')
        quit()


main()
