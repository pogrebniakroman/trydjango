subject_list = []
list_score = []
subject = 0
for i in range(3):
    grocery_input = int(input('Enter score: '))
    subject_input = str(input('Enter subject: '))

    list_score.append(grocery_input)
    subject_list.append(subject_input)
    sum_score = sum(list_score)
    print(sum_score)
    print(subject_list)
    percentage = (sum_score/300)*100
    print('Percentage is: ', round(percentage))

subject = len(subject_list)
for i in range(subject):
    print(subject_list[i])



#percentage = (87+95+75/(100+100+100))*100''