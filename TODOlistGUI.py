from tkinter import *
from tkinter import messagebox

def addtask():
    task=entry.get()
    if task:
        listbox.insert(END,task)
        entry.delete(0,END)
    else:
        messagebox.showwarning("Warning","Please enter a task")

def removetask():
    selectedtaskindex=listbox.curselection()
    if selectedtaskindex:
        listbox.delete(selectedtaskindex)
        messagebox.showwarning('Warning',"Task deleted")
    else:
        messagebox.showwarning("Warning","Please select a task to remove")

def clearlist():
    listbox.delete(0,END)
    messagebox.showwarning('Warning',"List cleared")

root=Tk()
root.title("To-Do List")

entry=Entry(root, ipadx=5)

add_button=Button(root, text="Add Task", command=addtask)

remove_button=Button(root, text="Delete Task", command=removetask)

clear_button=Button(root, text='Clear List', command=clearlist)
listbox=Listbox(root)

entry.pack()
add_button.pack()

remove_button.pack()
clear_button.pack()
listbox.pack()

root.mainloop()
