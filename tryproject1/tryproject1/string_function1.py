
string = input('Enter your string: ')   #Enter string
def string_list(string):                #This function take string
    print(list(string))
string_list(string)

def string_list_back(string):           #This function the reversed string
    for i in range(len(string), 0, -1 ):
        print(string[::-1])
    return
string_list_back(string)



