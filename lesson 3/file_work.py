
my_file = open("text.txt", "a")

my_file.write("Привет, Мир!")

my_file.close()



my_file = open("text.txt", "w")

string = my_file.read()
my_file.write("Ку")
print(string)
my_file.close()