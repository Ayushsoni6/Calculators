
while True:
    print("Please select operation -\n" \
            "1. Add\n" \
            "2. Subtract\n" \
            "3. Division\n" \
            "4. Multiplacation\n" \
            "0. Exit\n")

    Option = int(input("select operation- 1, 2, 3, 4, 0 :"))

    if Option == 0:
      break

    number_1 = int(input("Enter first number:  "))
    number_2 = int(input("Enter second number: "))

    if Option == 1:
      sum = int(number_1) + int(number_2)
      print("Total is= ", sum)

    if Option == 2:
      sum = int(number_1) - int(number_2)
      print("Total is= ", sum)

    if Option == 3:
      sum = int(number_1) / int(number_2)
      print("Total is= ", sum)

    if Option == 4:
      sum = int(number_1) * int(number_2)
      print("Total is= ", sum)
