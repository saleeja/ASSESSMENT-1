"""Write a Python program to implement a stack using a list.(push and pop)"""

# Initialize an empty stack
stack = []
# Function to push an item onto the stack
def push(item):
    stack.append(item)
    print(f"Pushed {item} onto the stack.")

# Function to pop an item from the stack
def pop():
    if not is_empty():
        popped_item = stack.pop()
        print(f"Popped {popped_item} from the stack.")
        return popped_item
    else:
        print("Stack is empty. Cannot pop from an empty stack.")
        return None

# Function to check if the stack is empty
def is_empty():
    return len(stack) == 0

# Function to get the size of the stack
def size():
    return len(stack)


while True:
    print("\nChoose an operation:")
    print("1. Push")
    print("2. Pop")
    print("3. Check if empty")
    print("4. Get size")
    print("5. show current list")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")
# Perform the chosen operation based on user inpu
    if choice == '1':
        item = input("Enter the item to push onto the stack: ")
        push(item)
    elif choice == '2':
        pop()
    elif choice == '3':
        if is_empty():
            print("The stack is empty.")
        else:
            print("The stack is not empty.")
    elif choice == '4':
        print("Stack size:", size())
    elif  choice=='5':
        print("Current stack:", stack)
    elif choice == '6':
        print("Exiting. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 6.")

