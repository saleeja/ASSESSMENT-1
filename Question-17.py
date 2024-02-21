"""Write a Python program to implement a queue using a list.(enqueue and dequeue)"""

# Initialize an empty queue
queue = []
# Enqueue operation: Add an item to the end of the list
# Dequeue operation: Remove and return the item from the front of the list

# Function to enqueue an item into the queue
def enqueue(item):
    queue.append(item)
    print(f"Enqueued {item} into the queue.")

# Function to dequeue an item from the queue
def dequeue():
    if not is_empty():
        dequeued_item = queue.pop(0)
        print(f"Dequeued {dequeued_item} from the queue.")
        return dequeued_item
    else:
        print("Queue is empty. Cannot dequeue from an empty queue.")
        return None

# Function to check if the queue is empty
def is_empty():
    return len(queue) == 0

# Function to get the size of the queue
def size():
    return len(queue)

# user input
while True:
    print("\nChoose an operation:")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Check if empty")
    print("4. Get size")
    print("5. Show current queue")
    print("6. Exit")

    # Get user choice
    choice = input("Enter your choice (1-6): ")

    # Perform the chosen operation based on user input
    if choice == '1':
        item = input("Enter the item to enqueue into the queue: ")
        enqueue(item)
    elif choice == '2':
        dequeue()
    elif choice == '3':
        if is_empty():
            print("The queue is empty.")
        else:
            print("The queue is not empty.")
    elif choice == '4':
        print("Queue size:", size())
    elif choice == '5':
        print("Current queue:", queue)
    elif choice == '6':
        print("Exiting. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 6.")

