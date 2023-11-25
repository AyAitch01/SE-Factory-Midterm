def printlist():
    print("***Welcome***")
    print('''1. Open Tab
2. Close Tab
3. Switch Tab
4. Display All Tabs
5. Open Nested Tab
6. Sort All Tabs
7. Save Tabs
8. Import Tabs
9. Exit''')

printlist()

choice = 0
while(choice != 9):
    printlist()
    choice = int(input("Choose from the above menu "))

print("Thank You!")
