def write_data():
    data = input("Enter data: ")
    with open("data.txt", "a") as f:
        f.write(data + "\n")
def read_data():
    try:
        with open("data.txt", "r") as f:
            print("\nFile Content:")
        print(f.read())
    except:
        print("No file found")
    while True:
        print("\n1.Write 2.Read 3.Exit")
        ch = input("Choice: ")
        if ch == '1':
            write_data()
        elif ch == '2':
            read_data()
        elif ch == '3':
            break
        else:
            print("Invalid choice")
