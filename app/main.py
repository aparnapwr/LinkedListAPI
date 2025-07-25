from fastapi import FastAPI
from typing import Optional

app=FastAPI()

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class SingleLinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        items = []
        temp=self.head
        while(temp):
            items.append(temp.data)
            temp = temp.next
        return items

    def insert(self,data):
        if(L.head is None):
            new_node = Node(data)
            L.head=new_node
        else:
            new_node = Node(data)
            temp = L.head
            while(temp.next):
                temp = temp.next
            temp.next = new_node
    
    def delete(self,pos):
        prev = L.head
        temp = L.head.next
        for i in range(pos-1):
            prev = prev.next
            temp = temp.next
        prev.next = temp.next
        temp.next = None
    


L = SingleLinkedList()

@app.post("/insert")
def insert_item(data: str):
    L.insert(data)
    return {"message": f"{data} has been added."}

@app.delete("/delete")
def delete_item(pos: int):
    L.delete(pos)
    return {"message": f"Element at {pos} has been removed."}

@app.get("/list")
def get_items():
    return {"items": L.display()}

@app.get("/")
def root():
    return {"message": "Linked List API is running"}
