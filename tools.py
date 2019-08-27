import os
import random
class Strings:

    def strip(string,item):
        hold = string.strip(item)
        return hold

    def fomart(string,title):
        hold = "\n\n[STUDENT AI LEARNER]\n" +"____________________________\n" + str(title).upper() + "\n----------------------------\n" + str(string) + "\n-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_\n"
        return hold

    def split_to_list(self,char,lenght):
        string_hold = self
        list = string_hold.split(char,lenght)
        return list

class Lists:

    def strip_from_items(list,character):
        new_list = []
        for item in list:
            new_item = item.strip(character)
            new_list.append(new_item)
        return new_list

    def sort(list):
        return list.sort()

class Files:

    def delete_line_from_file(filename, string):
        file = open(filename, "r")
        temp = file.readlines()
        temp2 = temp
        print(temp[0])
        file.close()
        file = open(filename, "w")
        for item in temp2:
            if string in item:
                print("Updating...", string)
                temp.remove(item)
                print(string, "has been Updated")
                pass
            else:
                pass
        file.write("")
        for item in temp:
            file.writelines(item)

    def delete_file(filename):
        os.remove(filename)
        print("removed",filename)


def randomise(x,y):
    wild = random.randint(x,y)
    return wild

