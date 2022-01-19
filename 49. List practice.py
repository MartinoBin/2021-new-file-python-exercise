print('Welcome!')

input1=input('Your first grade:')
input2=input('Your second grade:')
input3=input('Your third grade:')
input4=input('Your fourth grade:')

list_grade=[input1,input2,input3,input4]
print('Your grades are:',list_grade)

print('Your grades from higher to lower is:',sorted(list_grade,reverse=True))

print('The lowest two grades would be dropped.')
print('Removed grades:',list_grade.pop(0))
print('Removed grades:',list_grade.pop(0))
print('Your remaining grades are:',list_grade)

print('Nice job.', 'your highest grade is', sorted(list_grade[-1])) 
