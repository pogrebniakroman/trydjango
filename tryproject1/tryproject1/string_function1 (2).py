
string = input('Enter your string: ')   #Enter string
def string_list(string):                #This function take string
    print(list(string))                 #This funciton is not necessary
                                        #necessary though
string_list(string)

def string_list_back(string):           #This function the reversed string
    return string[::-1]                 #A loop isn't required when 
string_list_back(string)                #using this method
print(string_list_back(string))


