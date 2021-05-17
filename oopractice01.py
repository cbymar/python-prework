
# closures
# https://www.springboard.com/workshops/data-engineering-career-track/learn#/curriculum/23972
def outerFunction(text):
    def innerFunction():
        print(text)
    innerFunction()

outerFunction("Hello")

def pop(list):
    def get_last_item(my_list):
        return my_list[len(list) - 1]
    list.remove(get_last_item(list))
    return list

a = [1, 2, 3, 4, 7]
print(pop(a))
###############
# https://www.springboard.com/workshops/data-engineering-career-track/learn#/curriculum/23972
# Instance method -- modify both object instance state and class state.
# Class method cannot modify obj instance state, only class state
# static method cannot modify either obj instance or class state
