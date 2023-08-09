
while True: # for loop
    print("Please select operation -\n" \
      "1. Add\n" \
      "2. Subtract\n" \
      "3. Division\n" \
      "4. Multiplication\n" \
      "5. Square\n" \
      "6. Square root\n" \
      "0. Exit\n")  #assigned different operation as a numbers

    Option = int(input("select operation- 1, 2, 3, 4, 0 :")) #user will be asked to apply which option + - * /

    if Option >= 7:
       print("inter from number 0, 1, 2, 3, 4 only")

    if Option == 0: #0 will exit the cide from loop
      break

    number_1 = int(input("Enter first number:  ")) #user will be asked to eneter 1st number 
    number_2 = int(input("Enter second number: ")) #user will be asked to eneter 2nd number 

    if Option == 1: #if user select option 1 
      sum = int(number_1) + int(number_2)  # math part 
      print("Total is= ", sum) #Output

    if Option == 2: #if user select option 2 
      sum = int(number_1) - int(number_2) # math part 
      print("Total is= ", sum)  #Output


    if Option == 3:   #if user select option 3
      #sum = int(number_1) / int(number_2) # math part 
      #print("Total is= ", sum)  #Output
        if number_2 == 0:
          print("N/A")
        else:
          sum = int(number_1) / int(number_2) # math part 
          print("Total is= ", sum)  #Output

    if Option == 4: #if user select option 4
      sum = int(number_1) * int(number_2) # math part 
      print("Total is= ", sum)  #Output

    if Option == 5:
       sum = int(number_1) * int(number_1)
       print("will only pick number 1 not number2")
       print("Total is= ", sum)
       
    if Option == 6:
       sum = int(number_1) ** 0.5
       print("will only pick number 1 not number2")
       print("Total is= ", sum)
