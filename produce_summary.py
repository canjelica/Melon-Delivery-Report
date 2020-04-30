def produce_melon_count_sales_by_day():
    """Creates report of how many melons sold for total amount by day.

    Looks at daily sales logs and creates report of the number, type of melon, and total amount sold"""  
    
    print("Day 1")
    the_file = open("um-deliveries-20140519.txt") #this opens daily sales log
    for line in the_file:       #iterates over each line in opened saily sales log, tokenizes each item by delimitor"
        line = line.rstrip()
        words = line.split('|')

        melon = words[0]        #saves each item from tokenized file to variable by index
        count = words[1]
        amount = words[2]

        print("Delivered {} {}s for total of ${}".format(count, melon, amount)) #prints the number of type of melons and amount sold
    the_file.close()

    print("Day 2")
    the_file = open("um-deliveries-20140520.txt")
    for line in the_file:
        line = line.rstrip()
        words = line.split('|')

        melon = words[0]
        count = words[1]
        amount = words[2]

        print("Delivered {} {}s for total of ${}".format(
            count, melon, amount))
    the_file.close()


    print("Day 3")
    the_file = open("um-deliveries-20140521.txt")
    for line in the_file:
        line = line.rstrip()
        words = line.split('|')

        melon = words[0]
        count = words[1]
        amount = words[2]

        print("Delivered {} {}s for total of ${}".format(
            count, melon, amount))
    the_file.close()

produce_melon_count_sales_by_day()