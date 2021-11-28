from SkipList import SkipList


def main():
    skip_list = SkipList()
    skip_list.add(2)
    print(skip_list.print_levels())
    skip_list.add(5)
    skip_list.add(20)
    skip_list.add(15)

    print("Looking up 20: ", skip_list.search(20))
    print("Looking up 100: ", skip_list.search(100))
    skip_list.add(100)
    skip_list.add(27)
    skip_list.add(45)
    skip_list.add(78)
    skip_list.add(86)
    print(skip_list.print_levels())
    print("Looking up 20: ", skip_list.search(20))
    print("Deleting 20")
    skip_list.remove(20)
    print("Looking up 20: ", skip_list.search(20))
    print("Looking up 100: ", skip_list.search(100))
    print("Deleting 100")
    skip_list.remove(100)
    print("Looking up 100: ", skip_list.search(100))
    print("\n", skip_list.print_levels())


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
