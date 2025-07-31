# -------------------------------------------- Excersize - Exceptions --------------------------------------------


def try_except():
    try:
        num = 0
        res = 5000 / num
    except ZeroDivisionError:
        return print("Can't divide by zero")
    return res


def continue1():
    with open("../txts/text_data.txt", "w+") as f:
        f.write("this is some data inserted")
        f.seek(0)
        content2 = f.read()
        print(content2)


def q10():
    with open("../txts/text_data.txt", "w+") as f:
        f.write("this is some data inserted")
        f.seek(0)
        f.close()


def thirdLesson():
    # Comment
    """
    Options of open():
    - Open a file for reading. (default) = r
    - Open a file for writing. Creates a new file if it does not exist or truncates the file if it exists. = w
    - Open a file for exclusive creation. If the file already exists, the operation fails. = x
    - Open a file for appending at the end of the file without truncating it. Creates a new file if it does not exist. = a
    - Open in text mode. (default) = t
    - Open in binary mode. = b
    - Open a file for updating (reading and writing) = +
   """
    # file = open("data.txt", "r")
    # print(file)
    # content = file.read(20)
    # print(content)
    # file.close()
    # try:
    #     file2 = open("non_existing_file.txt", "r")
    # except FileNotFoundError:
    #     print("File does not exist")
    # with open("aaa.txt", "w+") as file3:
    #     file3.write("Hello world!")
    #     file3.seek(0)  # returns the pointer to the start of the file, needed after using write()
    #     con = file3.read(2)
    #     print(con)
    #     print(try_except())
    #     continue1()


def run():
    q10()
# -------------------------------------------- The End -----------------------------------------------------------
