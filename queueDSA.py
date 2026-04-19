#Queue
queue =[]
#enqueue : Adding Tasks to the back
queue.append("Finish lab")
queue.append("Update GitHub")
queue.append("Ignore the headache")

#Dequeue : Taking the first one out
current_task = queue.pop(0)
print(f"Working on : {current_task}")