one = ['  #','  #','  #','  #','  #']
two = ['###','  #','###','#  ','###']
three = ['###','  #','###','  #','###']
four = ['# #','# #','###','  #','  #']
five = ['###','#  ','###','  #','###']
six = ['#  ','#  ','###','# #','###']
seven = ['###','  #','  #','  #','  #']
eight = ['###','# #','###','# #','###']
nine = ['###', '# #', '###', '  #', '  #']
zero = ['###','# #','# #','# #','###']

array = [zero,one,two,three,four,five,six,seven,eight,nine]

def led_display(num):
    
    str_num = str(num)

    if str_num.isdigit() == False:
        return print("Please enter digits only")

    processor = [num for num in str_num]

    i = 0

    while i < 5:
        for num in processor:
            t = int(num)
            print(array[t][i], end = '  ')
        print('')
        i += 1

led_display(7598656447)