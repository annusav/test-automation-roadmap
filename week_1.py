#Python Automation Testing Roadmap 
#Week 1 Mini-practice: Write a script to find duplicates in a list.


def finding_duplicates(list):
    seen = []
    duplicates = []
    for item in list:
        print(f"List item: '{item}'")
        if item in seen:
            duplicates.append(item)
            print(f"'{item}' added to list of duplicates.")
        else:
            seen.append(item)
            print(f"'{item}' seen for the first time.")
    print(f"Total number of duplicates on the original list: {len(duplicates)}")



my_list = ["some", "list", "stuff", "in", "a", "list"]
finding_duplicates(my_list)