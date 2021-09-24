# mode = 'a' : append
# with open("writing_file.txt", mode='a') as f:
#     f.write("mode=a appends text")


with open("writing_file.txt", mode='r+') as f:
    f.write("You can write and read with r+ mode!")
