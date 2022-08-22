import db_helper

def main():
    db_helper.createTable()

run = 1


while run:
    x = input("1.insert\n"
              "2.show data\n"
              "3.delete\n"
              "4.exit\n"
              "Enter Your Choice:"
              )
    if x == "1":
        data = str(input("Enter Your Task: "))
        db_helper.data_entry(data)
    elif x == "2":
        db_helper.data_print()
    elif x == "3":
        id = int(input("ENter ID: "))
        db_helper.delete_data(id)
    elif x== "4":
        run = 0
    else:
        print("enter valid number")

db_helper.close()

if __name__ == '__main__':main()

