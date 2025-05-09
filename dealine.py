#import
import tkinter as tk
from datetime import datetime

def add_goal():
    goal = Your_goal.get()
    dead_line = Deadline.get()

    if not goal or not dead_line:
        box.insert(tk.END,"Please add your goal and deadline:")
        return
    try:
        deadline_date = datetime.strptime(dead_line,"%Y/%m/%d").date()
        today = datetime.today().date()
        days_left = (deadline_date - today).days
        
        if days_left >= 0:
            message = f"{goal} | {days_left} day(s) left (until {deadline_date}) "
        else:
            message = f"{goal} | Deadline Passed (on {deadline_date})"
        box.insert(tk.END,message)
    except:
        box.insert(tk.END,"❌ Invalid date! Please use the format yyyy/mm/dd")
    
    Your_goal.delete(0,tk.END)
    Deadline.delete(0,tk.END)
#gui
app = tk.Tk()
app.title("Deadline Planner by kid-one-bit")
app.geometry("450x450")
app.configure(bg="#FAF0E6")

#title
TitleLabel = tk.Label(app,text="Life Planner : Plan Your Priorities",font=("Fira Code",15,"bold"),bg="#FAF0E6",fg="#444")
TitleLabel.pack(pady=15)

#goal
GoalLabel = tk.Label(app,text="🎯 Your goal :",font=("Fira Code",13,"bold"),bg="#FAF0E6",fg="#444").pack()
Your_goal = tk.Entry(app,width=40,font=("Fira Code",12))
Your_goal.pack(pady=5,ipady=3)

#deadline
DeadlineLabel = tk.Label(app,text="⏳🔚🏁 Deadline (yyyy/mm/dd):",font=("Fira Code",13,"bold"),bg="#FAF0E6",fg="#444").pack()
Deadline = tk.Entry(app,width=40,font=("Fira Code",12))
Deadline.pack(pady=5,ipady=3)


#button
add_button = tk.Button(app,text="✙ Add ",font=("Fira Code",13,"bold"),bg="#FAF0E6",fg="#444",command=add_goal)
add_button.pack(pady=10)

#box
box = tk.Listbox(app,width=50,height=10,font=("Fira Code",10))
box.pack(pady=10)

app.mainloop()
