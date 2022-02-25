import sqlite3

conn = sqlite3.connect("tasks.db")

cur = conn.cursor()


def insert_task(title, content):
    cur.execute("INSERT INTO tasks VALUES (null,?,?,0)", (title, content))
    print("The task was added successfully.")


def complete_task(id):

    cur.execute("update tasks set status = 1 where id = ?", id)
    cur.execute("delete from tasks where status = 1")
    print("The task was completed successfully, and after deleted.")


def delete_task(id):
    cur.execute("delete from tasks where id = ?", id)
    print("The task was deleted successfully.")


def show_tasks():
    count = 0
    d = dict()
    for task in cur.execute("SELECT * FROM tasks"):
        print("")
        d["id"] = task[0]
        d["title"] = task[1]
        d["content"] = task[2]
        d["status"] = task[3]
        print("id:", d["id"], "\n", "title:", d["title"], "\n",
              "content:", d["content"], "\n", "status:", d["status"])
        count += 1
    if count < 1:
        print("There aren't any task.")


# while True:
#     print("")
#     option = int(input(
#         "1. Insert task\n2. Show tasks\n3. Delete task\n4. Mark complete\n5. Quit\n: "))
#     print("")

#     if option == 1:
#         insert_task(input("Give the title: "), input("Give the content: "))
#     elif option == 2:
#         show_tasks()
#     elif option == 3:
#         delete_task(input("give the task id: "))
#     elif option == 4:
#         complete_task(input("give the task id: "))
#     elif option == 5:
#         conn.commit()
#         conn.close()
#         exit()
#     else:
#         print("This isnt an valid option")