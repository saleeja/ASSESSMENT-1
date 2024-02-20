"""Write a Python program to implement a queue using a list.(enqueue and dequeue)"""

# Initialize an empty list to represent the queue
queue = []

# Enqueue operation: Add an item to the end of the list (rear of the queue)
def enqueue(item):
    queue.append(item)

# Dequeue operation: Remove and return the item from the front of the list (front of the queue)
def dequeue():
    if not is_empty():
        return queue.pop(0)
    else:
        print("Queue is empty. Cannot dequeue.")
        return None

# Check if the queue is empty
def is_empty():
    return len(queue) == 0

# Get the size of the queue
def size():
    return len(queue)

# Example usage:
enqueue(1)
enqueue(2)
enqueue(3)

print("Queue:", queue)

item_removed = dequeue()
if item_removed is not None:
    print(f"Dequeued item: {item_removed}")
else:
    print("Queue is empty.")

print("Updated Queue:", queue)
