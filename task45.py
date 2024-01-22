class PersistentNode:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node


class PersistentQueueInner:
    def __init__(self, front=None, rear=None):
        self.front = front
        self.rear = rear

    def enqueue(self, value):
        new_rear = PersistentNode(value)
        if not self.rear:
            # Empty queue case
            new_front = new_rear
        else:
            # Non-empty queue, link the new node to the rear
            self.rear.next = new_rear
            new_front = self.front
        return PersistentQueueInner(new_front, new_rear)

    def dequeue(self):
        if not self.front:
            raise IndexError("dequeue from an empty queue")
        new_front = self.front.next
        if not new_front:
            # Last element case
            new_rear = None
        else:
            new_rear = self.rear
        return PersistentQueueInner(new_front, new_rear)

    def peek(self):
        if not self.front:
            raise IndexError("peek from an empty queue")
        return self.front.value

    def is_empty(self):
        return self.front is None

    def __iter__(self):
        current = self.front
        while current:
            yield current.value
            current = current.next


if __name__ == "__main__":
    # Create a new empty queue
    q0 = PersistentQueueInner()

    # Enqueue elements
    q1 = q0.enqueue("apple")
    q2 = q1.enqueue("banana")
    q3 = q2.enqueue("cherry")

    # Dequeue elements
    q4 = q3.dequeue()  # Removes 'apple'
    q5 = q4.dequeue()  # Removes 'banana'

    # Check the contents of each queue version
    print("Contents of q0:")
    for val in q0:
        print(val)  # Empty, will not print anything

    print("Contents of q1:")
    for val in q1:
        print(val)  # Should print 'apple'

    print("Contents of q2:")
    for val in q2:
        print(val)  # Should print 'apple', 'banana'

    print("Contents of q3:")
    for val in q3:
        print(val)  # Should print 'apple', 'banana', 'cherry'

    print("Contents of q4:")
    for val in q4:
        print(val)  # Should print 'banana', 'cherry'

    print("Contents of q5:")
    for val in q5:
        print(val)  # Should print 'cherry'

    # Peeking elements (view the front without dequeuing)
    print("Front of q2:", q2.peek())  # Should print 'apple'
    print("Front of q4:", q4.peek())  # Should print 'banana'
    print("Front of q5:", q5.peek())  # Should print 'cherry'

    # Check if a queue is empty
    print("Is q0 empty?", q0.is_empty())  # Should print True
    print("Is q5 empty?", q5.is_empty())  # Should print False

    # Enqueuing more elements to a previous version
    q6 = q2.enqueue("date")
    print("Contents of q6:")
    for val in q6:
        print(val)  # Should print 'apple', 'banana', 'date'

    # The state of q2 remains unchanged
    print("Contents of q2 after q6 creation:")
    for val in q2:
        print(val)  # Should print 'apple', 'banana'