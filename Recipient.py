import pickle


recipients = {}


class Recipient:
    def __init__(self, shortname):
        self.__shortname = shortname
        self.fullname = ""
        self.address = ""

    @property
    def shortname(self):
        return self.__shortname

    def substitute(self, text):
        sub = text.replace("{shortname}", self.__shortname)
        sub = sub.replace("{fullname}", self.fullname)
        sub = sub.replace("{address}", self.address)
        return sub


def menu():
    global recipients
    while True:
        while True:
            print("Enter your choice:")
            print("1) Create letters from template")
            print("2) List recipients")
            print("3) Add recipient")
            print("4) Delete recipient")
            print("5) Import recipient list")
            print("6) Export recipient list")
            print("7) Quit")
            try:
                num = int(input())
                if num < 1 or num > 7:
                    raise ValueError()
                break
            except ValueError:
                print("Please enter an integer from 1 to 7")
                print()
        print()
        if num == 1:
            if recipients:
                filename = input("Please input the file name: ")
                print()
                try:
                    if filename[-4:] != ".txt":
                        print("File name must end in .txt")
                        raise FileNotFoundError()
                    file = open(filename, 'r')
                    template = file.read()
                    file.close()
                    name = filename[:-4]
                    for person in recipients:
                        new_filename = name + "." + recipients[person].shortname + ".txt"
                        temp_file = open(new_filename, 'w')
                        temp_file.write(recipients[person].substitute(template))
                        temp_file.close()
                except FileNotFoundError:
                    print("File could not be opened")
                    print()
                print("Substitution completed")
            else:
                print("No recipients in list")
            print()
        elif num == 2:
            print("Recipient List:")
            print("---------------")
            names = recipients.keys()
            for name in names:
                print(name)
            print("---------------")
            print()
        elif num == 3:
            while True:
                shortname = input("Please input a shortname: ")
                print()
                if shortname in recipients:
                    print("Recipient exists")
                    print()
                else:
                    obj = Recipient(shortname)
                    obj.fullname = input("Please input a fullname: ")
                    print()
                    obj.address = input_address()
                    recipients[shortname] = obj
                    break
        elif num == 4:
            while True:
                name = input("Please input the recipient's shortname (blank to cancel): ")
                print()
                if name == "":
                    print()
                    break
                if name not in recipients:
                    print("Recipient not found")
                    print()
                else:
                    del recipients[name]
                    print(name, "successfully deleted")
                    print()
                    break
        elif num == 5:
            file = open("recipients.bin", 'rb')
            recipients = pickle.load(file)
            file.close()
            print("Recipients imported from recipients.bin")
            print()
        elif num == 6:
            file = open("recipients.bin", 'wb')
            pickle.dump(recipients, file)
            file.close()
            print("Recipients exported to recipients.bin")
            print()
        else:
            print("Goodbye!")
            break


def input_address():
    print("Please input the recipient's address:")
    lines = []
    while True:
        line = input()
        if line == '':
            break
        else:
            lines.append(line)
    return '\n'.join(lines)


menu()