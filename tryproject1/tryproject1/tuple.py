#students dictionary
#student names
#student grades
#student class 6

#change class to 8

#add student ages





my_dictionary_student = {'names':'qwerty', 'grades':'5', 'class':6}
print(my_dictionary_student)
my_dictionary_student['class'] = 8
print(my_dictionary_student)
my_dictionary_student['ages'] = 33
print(my_dictionary_student)

print(my_dictionary_student.keys())
print(my_dictionary_student.values())

for i in my_dictionary_student.keys():
    print(i)
    print(my_dictionary_student[i])


for key in my_dictionary_student.keys():
    print(key, '>>>', my_dictionary_student[key])


###print(my_dictionary[key]) #value
#print() #for new line
#Make a dictionary of the days of the week
# and their according temperature in Celcius
# Read the whole dictionary, and change the
# temperature from celcius to Fehrenheit

#mon = 12 #celcius
#tue = 15

#formula for converting from celcius to fehrenheit
#F = (9/5)*C + 32

my_dictionary_tempr = {'mon':12, 'tue':14, 'wed':22, 'thu':21, 'fri':11, 'sat':15, 'san':12}
my_dictionary_farenheit = {}
for day in my_dictionary_tempr.keys():
    print(day, '=' ,my_dictionary_tempr[day])
    my_dictionary_farenheit[day] = round((9/5)*my_dictionary_tempr[day] + 32)
    print(my_dictionary_farenheit)

