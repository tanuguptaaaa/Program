
from apscheduler.schedulers.blocking import BlockingScheduler

# from todo import ToDo  # Import the ToDo class from todo.py
from to_dolist import ToDo


def fetch_pending_tasks():
    try:
        todo = ToDo()
        # Query for pending tasks
        query = "SELECT Task_id, Title, Description FROM Task WHERE Status = 'Pending'"
        todo.cursor.execute(query)
        tasks = todo.cursor.fetchall()

        if tasks:
            print("\nPending Tasks:")
            for task in tasks:
                print(f"ID: {task[0]}, Title: {task[1]}, Description: {task[2]}")
        else:
            print("No pending tasks.")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Close the cursor and connection
        if todo.cursor:
            todo.cursor.close()
        if todo.connection:
            todo.connection.close()


# Create a scheduler
scheduler = BlockingScheduler()

# Schedule the fetch_pending_tasks function to run every 10 seconds
scheduler.add_job(fetch_pending_tasks, 'interval', seconds=10)

# Start the scheduler
scheduler.start()
