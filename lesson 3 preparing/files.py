my_file = open("file.txt", "a")

my_file.write("Текст")
my_file.close()

my_file = open("file.txt", "r")
my_text = my_file.read()
print(my_text)
my_file.close()
