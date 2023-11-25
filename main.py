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
tabs = [
    {"title":"" ,"URL":"" }
]
choice = 0
while choice != 9:
    printlist()
    choice = int(input("Choose from the above menu "))
    if choice == 1:
        open_tab()
    elif choice == 2:
        close_tab()
    elif choice == 3:
        switch_tab()
    elif choice == 4:
        display_all_tabs()
    elif choice == 5:
        open_nested_tab()
    elif choice == 6:
        sort_all_tabs()
    elif choice == 7:
        save_tabs()
    elif choice == 8:
        import_tabs()
    elif choice == 9:
        exit_program()
    else:
        print("Invalid choice")
print("Thank You!")

