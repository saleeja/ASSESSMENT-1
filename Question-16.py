"""Write a Python program to implement a stack using a list.(push and pop)"""


stack = []

def push(item):
    stack.append(item)
    print(f"Pushed {item} onto the stack.")

def pop():
    if not is_empty():
        popped_item = stack.pop()
        print(f"Popped {popped_item} from the stack.")
        return popped_item
    else:
        print("Stack is empty. Cannot pop from an empty stack.")
        return None

def is_empty():
    return len(stack) == 0


def size():
    return len(stack)


while True:
    print("\nChoose an operation:")
    print("1. Push")
    print("2. Pop")
    print("3. Check if empty")
    print("4. Get size")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        item = input("Enter the item to push onto the stack: ")
        push(item)
    elif choice == '2':
        pop()
    elif choice == '3':
        print("Is the stack empty?", is_empty())
    elif choice == '4':
        print("Stack size:", size())
    elif choice == '5':
        print("Exiting. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")

