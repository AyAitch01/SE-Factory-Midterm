import requests
from bs4 import BeautifulSoup
import json


def printlist():
    print("    ***Welcome***   ")
    print('''    1. Open Tab
    2. Close Tab 
    3. Switch Tab
    4. Display All Tabs
    5. Open Nested Tab
    6. Sort All Tabs
    7. Save Tabs
    8. Import Tabs
    9. Exit''')


tabs = [

]


def open_tab():
    title = str(input("Enter tab title: "))
    URL = str(input("Enter tab URL: "))
    return title, URL


def close_tab():
    index = int(input("Enter the index of tab to close "))
    tabs.pop(index)


# I got these library from these urls: https://pypi.org/project/beautifulsoup4/
# https://www.tutlane.com/tutorial/python/python-requests-module#:~:text=To%20download%20and%20install%20the,the%20pip%20install%20requests%20command.&text=After%20completion%20of%20installing%20the,will%20be%20as%20shown%20below.
def displayContent(displayURL):
    result = requests.get("https://" + displayURL)
    if result.status_code == 200:
        soup = BeautifulSoup(result.content, 'lxml')
        print(soup.prettify())
    elif result.status_code == 404:
        print('Not Found')


def switch_tab():
    displayIndex = int(input("Enter index to switch: "))
    if len(tabs) == 0:
        print("No tabs")
    else:
        print(tabs)
        if 0 <= displayIndex < len(tabs):
            displayContent(tabs[displayIndex]["URL"])
        else:
            displayContent(tabs[len(tabs) - 1]["URL"])


def display_all_tabs():
    for n in range(len(tabs)):
        tab = tabs[n]["title"]
        print(str(int(n + 1)) + f" {tab}")
        if len(tabs[n]["nested_tabs"]) > 0:
            for m in range(len(tabs[n]["nested_tabs"])):
                tab2 = tabs[n]["nested_tabs"][m]
                print("\t" + str(int((n + 1))) + "." + str(int((m + 1))) + f" {tab2}")


def open_nested_tab():
    nestedIndex = int(input("Enter index of tab to add to it: "))
    nestedTitle = str(input("Enter tab title: "))
    nestedURL = str(input("Enter tab URL: "))
    nestedList = [{"title": nestedTitle, "URL": nestedURL}]
    tabs[nestedIndex]["nested_tabs"].append(nestedList)
    # print(tabs)


def sort_all_tabs():
    tabs.sort(key=lambda x: x['title'], reverse=False)


def save_tabs():
    url = str(input("enter file url to save tabs to it : "))
    with open(url, 'w') as json_file:
        json.dump(tabs, json_file, indent=2)


def import_tabs():
    url = str(input("enter file url to import tabs from it : "))
    with open(url, 'r') as json_file:
        saved_tabs = json.load(json_file)
        for s in saved_tabs:
            tabs.append(s)


choice = 0
while choice != 9:
    printlist()
    choice = int(input("Choose from the above menu "))
    if choice == 1:
        title, URL = open_tab()
        tabs.append({"title": title, "URL": URL, "nested_tabs": []})
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
    else:
        print("Invalid choice")
print("Thank You!")
