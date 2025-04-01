class maxHeap:
    def __init__(self):
        self.arr = []
    
    def insert(self, element):
        self.arr.append(element)
        self._heapify_up(len(self.arr) - 1)
    
    def delete(self, element):
        try:
            index = self.arr.index(element)
            self.arr[index] = self.arr[-1]
            self.arr.pop()
            
            if index < len(self.arr):  # Ensure the index is valid after pop
                parent_index = (index - 1) // 2
                if index > 0 and self.arr[index] > self.arr[parent_index]:  
                    self._heapify_up(index)  # Move up if larger than parent
                else:
                    self._heapify_down(index)  # Move down otherwise
        except ValueError:
            print("Element not found in the heap")

    
    def display(self):
        print(self.arr)
    
    def _heapify_up(self, index):
        parent_index = (index - 1) // 2
        if index > 0 and self.arr[index] > self.arr[parent_index]:
            self.arr[index], self.arr[parent_index] = self.arr[parent_index], self.arr[index]
            self._heapify_up(parent_index)
    
    def _heapify_down(self, index):
        largest = index
        left_child = 2 * index + 1
        right_child = 2 * index + 2
        
        if left_child < len(self.arr) and self.arr[left_child] > self.arr[largest]:
            largest = left_child
        
        if right_child < len(self.arr) and self.arr[right_child] > self.arr[largest]:
            largest = right_child
        
        if largest != index:
            self.arr[index], self.arr[largest] = self.arr[largest], self.arr[index]
            self._heapify_down(largest)


if __name__ == "__main__":
    heap = maxHeap()
    while True:
        choice = int(input('''What do you want to do  :  
 1          insert
 2          delete
 3          display
 4          exit
Your choice  :  '''))

        if choice == 1:
            heap.insert(int(input("Enter the element to insert  :   ")))
            heap.display()
        
        elif choice == 2:
            heap.delete(int(input("Enter the element to delete  :   ")))
            heap.display()

        elif choice == 3:
            heap.display()
        
        elif choice == 4:
            break

        else:
            print("invalid choice!")