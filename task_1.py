class ListNode:
    '''ListNode'''
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

class LinkedList:
    '''LinkedList'''
    def __init__(self):
        self.head = None

    def append(self, value):
        '''Додавання нового значення'''
        if not self.head:
            self.head = ListNode(value)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = ListNode(value)

    def print_list(self):
        '''Відображення'''
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")


def reverse_linked_list(head):
    '''Реверсування однозв'язного списку'''
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev


def merge_sort(head):
    '''Сортування злиттям'''
    if not head or not head.next:
        return head

    # Розділити список на дві половини
    middle = get_middle(head)
    next_to_middle = middle.next
    middle.next = None

    left = merge_sort(head)
    right = merge_sort(next_to_middle)

    # Злиття двох відсортованих списків
    sorted_list = merge_lists(left, right)
    return sorted_list

def get_middle(head):
    '''
        Розділяє список на дві частини 
        (дозволяє рекурсивно сортувати кожну половину окремо, а потім об'єднати їх у відсортований список)
    '''
    if not head:
        return head

    slow = head #рухається по одному елементу за один крок
    fast = head #рухається по два елементи за один крок

    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    return slow

def merge_lists(l1, l2):
    '''Об'єднання двох однозв'язних списків'''
    dummy = ListNode()
    tail = dummy

    while l1 and l2:
        if l1.value < l2.value:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next

    tail.next = l1 if l1 else l2

    return dummy.next


if __name__ == "__main__":
    # Створення та виведення початкового списку
    ll = LinkedList()
    ll.append(3)
    ll.append(1)
    ll.append(4)
    ll.append(2)
    print("Початковий список:")
    ll.print_list()

    # Реверсування списку
    ll.head = reverse_linked_list(ll.head)
    print("Реверсований список:")
    ll.print_list()

    # Сортування списку
    ll.head = merge_sort(ll.head)
    print("Відсортований список:")
    ll.print_list()

    # Створення другого відсортованого списку
    ll2 = LinkedList()
    ll2.append(1)
    ll2.append(3)
    ll2.append(5)
    ll2.append(7)
    print("Другий відсортований список:")
    ll2.print_list()

    # Об'єднання двох відсортованих списків
    merged_head = merge_lists(ll.head, ll2.head)
    merged_list = LinkedList()
    merged_list.head = merged_head
    print("Об'єднаний відсортований список:")
    merged_list.print_list()
