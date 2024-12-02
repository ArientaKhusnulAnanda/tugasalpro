#Modul 1 (OOP)
#Class: (contoh 1)
class Person:

    def __init__(aku, nama, umur):
        aku.nama = nama
        aku.umur = umur
    def info(aku):
        return f"{aku.nama} {aku.umur}"

orang_pertama = Person("Hai nama saya: Fabio Banyu Cyto", "\nUmur saya: 19 tahun") 

print(orang_pertama.info())

#Modul 2
#linkedlist
class node: #Representasi Node (menggunakan class)
    def __init__(self, data=None):
        self.data=data #Menyimpan data
        self.next=None  #Menyimpan referensi ke node berikutnya

#membuat class linkedlist
class linkedlist:   #Representasi Linkelist(menggunakan class)
    def __init__(self): 
        self.head = node()  #menyimpan referensi ke node pertama

#Menambahkan node diakhir linked list
    def append (self, data): #menambahkan node baru diurutan terakhir
        new_node = node(data)
        if self.head is None: #-> is empty metode mencari tahu apakah linked list kosong atau tidak
            self.head = new_node #Jika(if) list pertama kosong, maka akan terbentuk node baru
        else:
            last = self.head
            while last.next:        #Mencari kode terakhir
                last = last.next
            last.next = new_node    #Menambahkan node  di akhir

#Menampilkan elemen linked list
    def display(self):
        current = self.head
        if current is None:
            print("linkedlist is empty")
            return
        while current:
            print(current.data, end = " -> ")
            current = current.next
        print("None")

ll = linkedlist()
ll.append(10)
ll.append(20)
ll.append(30)
ll.append(40)

ll.display()

#Node       : Setiap elemen dari linked list, menyimpan data dan referensi ke node berikutnya.
#LinkedList : Struktur data yang memiliki referensi ke node pertama (head).
#append()   : Menambahkan node baru di akhir linked list.
#display()  : Menampilkan semua elemen dalam linked list secara berurutan.

#Double Linked List
class Node:
    def __init__(self, data=None):
        self.data = data
        self.prev = None
        self.next = None

class DoubleLinkedlist:
    def __init__(self):
        self.head = None

    def append (self, data):
        new_node1 = Node(data)
        if self.head is None:
            self.head = new_node1
        else:
            last1 = self.head
            while last1.next:
                last1 = last1.next
            last1.next = new_node1
            new_node1.prev = last1

    def display_forward(self):
        current = self.head
        while current:  # Selama ada node berikutnya
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def display_backward(self):
        current1 = self.head 
        if not current1 :
            print("Linked listg is empty")
            return
        
        while current1.next:
            current1 = current1.next

        
        while current1:
            print(current1.data, end="-> ")
            current1 = current1.prev
        print("None")

dll = DoubleLinkedlist()

dll.append(10)
dll.append(20)
dll.append(30)
dll.append(50)
dll.display_forward
dll.display_backward


#Circulation Linked list
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class CirculationLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.head.next = self.head
        else:
            current2 = self.head
            while current2.next != self.head:
                current2 = current2.next
            current2.next =new_node
            new_node.next = self.head


    def display(self):
        if not self.head:
            print("Circular Linked list is empty")
            return
        current3 = self.head

        while True:
            print(current3.data, end="->")
            current3 = current3.next
            if current3 == self.head:
                break
        print("(head)")

cll = CirculationLinkedList()
cll.append(10)
cll.append(20)
cll.append(30)

cll.display()