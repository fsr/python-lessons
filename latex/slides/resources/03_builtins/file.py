with open(myfile, mode='r') as f:

    for line in f:
        # code


with open(myfile, mode="w+") as f:

    for line in document:
        f.write(line)
        # oder
        print(line, file=f)

f = open(myfile)

# code

f.close()
