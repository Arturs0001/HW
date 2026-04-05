def task1():
    f = open("data.txt", "w")
    for i in range(3):
        line = input("Enter line: ")
        f.write(line + "\n")
    f.close()
    print("Saved to data.txt")


def task2():
    try:
        f = open("log.txt", "r")
        text = f.read()
        f.close()
    except FileNotFoundError:
        print("log.txt not found")
        return

    words = text.split()
    stats = {}

    for word in words:
        word = word.lower()
        stats[word] = stats.get(word, 0) + 1

    def get_count(item):
        return item[1]

    sorted_words = sorted(stats.items(), key=get_count, reverse=True)

    f = open("word_stats.txt", "w")
    for word, count in sorted_words[:10]:
        f.write(word + ": " + str(count) + "\n")
    f.close()

    print("Saved to word_stats.txt")


def task3():
    try:
        f = open("orders.txt", "r")
        lines = f.readlines()
        f.close()
    except FileNotFoundError:
        lines = []

    print("2 Show orders")
    print("3 Search order")
    print("4 Update order")
    print("5 Delete order")
    print("0 Back")

    choice = input("> ")

    if choice == "1":
        f = open("orders.txt", "a")
        order_id = input("ID: ")
        name = input("Product: ")
        qty = input("Quantity: ")
        price = input("Price: ")
        f.write(order_id + "," + name + "," + qty + "," + price + "\n")
        f.close()
        print("Added")

    elif choice == "2":
        for line in lines:
            print(line.strip())

    elif choice == "3":
        order_id = input("Enter ID: ")
        for line in lines:
            if line.startswith(order_id + ","):
                print(line.strip())

    elif choice == "4":
        order_id = input("Enter ID: ")
        f = open("orders.txt", "w")
        for line in lines:
            if line.startswith(order_id + ","):
                name = line.split(",")[1]
                qty = input("New quantity: ")
                price = input("New price: ")
                f.write(order_id + "," + name + "," + qty + "," + price + "\n")
            else:
                f.write(line)
        f.close()
        print("Updated")

    elif choice == "5":
        order_id = input("Enter ID: ")
        f = open("orders.txt", "w")
        for line in lines:
            if not line.startswith(order_id + ","):
                f.write(line)
        f.close()
        print("Deleted")


while True:
    print("1. Task 1 (write file)")
    print("2. Task 2 (word stats)")
    print("3. Task 3 (orders)")
    print("0. Exit")

    choice = input("> ")

    if choice == "1":
        task1()
    elif choice == "2":
        task2()
    elif choice == "3":
        task3()
    elif choice == "0":
        break
    else:
        print("Invalid choice")