
# make node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
# make list
class LinkedList:
    def __init__(self):
        self.head = None
    # add nodes to list
    def append(self,data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    # print list
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end="->")
            current = current.next
        print("none")

# reverse list derection
def reverse_linked_list(linked_list):
    prev = None
    current = linked_list.head
    while current is not None:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    linked_list.head = prev

# find list middle point
def get_middle(head):
    if head is None:
        return head
    #  1 step forward
    slow = head
    # 2 steps forward
    fast = head
# when fast reach the end slow will be in the middle
    while fast.next is not None and fast.next.next is not None:
        slow = slow.next
        fast = fast.next.next
    return slow

# merge 
def sorted_merge(left, right):
    if left is None:
        return right
    if right is None:
        return left
    if left.data <= right.data:
        result = left
        result.next = sorted_merge(left.next, right)
    else:
        result = right
        result.next = sorted_merge(left, right.next)
    return result

# recursion sorted_merge
def merge_sort(head):
    if head is None or head.next is None:
        return head
    
    middle = get_middle(head)
    # beggining of right side
    next_to_middle = middle.next

    middle.next = None

    left = merge_sort(head)
    right = merge_sort(next_to_middle)

    sorted_list = sorted_merge(left, right)
    return sorted_list


# sort linked list
def sort_linked_list(linked_list):
    linked_list.head = merge_sort(linked_list.head)

# combine two sorted lists
def merge_sorted_lists(list1, list2):
    # additional node for beggining
    dummy = Node(0)
    tail = dummy

    a = list1.head
    b = list2.head

    while a is not None and b is not None:
        if a.data <= b.data:
            tail.next = a
            a = a.next
        else:
            tail.next = b
            b = b.next
        tail = tail.next

    if a is not None:
        tail.next = a
    if b is not None:
        tail.next = b
    
    merged_list = LinkedList()
    merged_list.head = dummy.next
    return merged_list

# testing code
if __name__ == "__main__":
    # creating elem and add them to list
    list1 = LinkedList()
    list1.append(3)
    list1.append(1)
    list1.append(4)

    print("Original list:")
    list1.print_list()

    # reversion
    reverse_linked_list(list1)
    print("Reversed list:")
    list1.print_list()

    # sorting list
    sort_linked_list(list1)
    print("Sorted list:")
    list1.print_list()

    # sorting two sorted lists
    sorted_list1 = LinkedList()
    sorted_list1.append(1)
    sorted_list1.append(3)
    sorted_list1.append(5)

    sorted_list2 = LinkedList()
    sorted_list2.append(2)
    sorted_list2.append(4)
    sorted_list2.append(6)

    # combine two sorted lists
    merged_list = merge_sorted_lists(sorted_list1, sorted_list2)
    print("Merged sorted list:")
    merged_list.print_list()

    # reverse merged list
    reverse_linked_list(merged_list)
    print("Reversed merged list:")
    merged_list.print_list()




    





