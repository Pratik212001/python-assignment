# avg per total

maths=float(input('Enter the marks of maths'))
science=float(input('Enter the marks of science'))
hindi=float(input('Enter the marks of hindi'))
sanskrit=float(input('Enter the marks of sanskrit'))
english=float(input('Enter the marks of english'))

total=maths+hindi+science+sanskrit+english

average=(maths+hindi+science+sanskrit+english)/5

percentage=(total/500)*100

print("total marks are",total)

print("average is",average)

print("percentage is",percentage)