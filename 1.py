def read_input():
    with open("1.txt", "r") as f:
        input_data = f.read().split("\n")
    return input_data

def part1(calories_list):
    highest_calories_carried = 0
    current_calories_carried = 0

    for item in calories_list:
        if item == '':
            #print(current_calories_carried, highest_calories_carried)
            if(current_calories_carried > highest_calories_carried):
                highest_calories_carried = current_calories_carried
            current_calories_carried = 0
        else:
            current_calories_carried += int(item)
            
    #print("Svaret:", highest_calories_carried)
    return

def part2(calories_list):
    highest_calories_carried = []
    current_calories_carried = 0

    for item in calories_list:
        if item == '':
            print(current_calories_carried, highest_calories_carried)
            if(len(highest_calories_carried) < 3):
                highest_calories_carried.append(current_calories_carried)
                current_calories_carried = 0
            else:
                minimum_calories_value_index = highest_calories_carried.index(min(highest_calories_carried))
                if(current_calories_carried > highest_calories_carried[minimum_calories_value_index]):
                    if(len(highest_calories_carried) == 3):

                        highest_calories_carried.pop(minimum_calories_value_index)
                    highest_calories_carried.append(current_calories_carried)
                current_calories_carried = 0
        else:
            current_calories_carried += int(item)
            
    print("Svaret, del 2:", sum(highest_calories_carried, 0))
    return




if __name__ == "__main__":
    calories_list = read_input()
    part1(calories_list)
    part2(calories_list)