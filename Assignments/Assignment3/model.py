from _init_ import setup_db


class Fibonacci():
    """
        A class to deal with every operations that involve Fibonacci
    """
    def __init__(self, limit=0, start_num=0):
        self.n = limit
        self.start_num = start_num
        
    def fibonacci_of_num(self, num):
        if num == 0:
            return num
        elif num == 1:
            return num
        else:
            fibonacci=self.fibonacci_of_num(num - 1) + self.fibonacci_of_num(num - 2)
            
        print(f"\n Calculating the fibonacci of {num} ...".title())
        return fibonacci

    # Implement a Fibonacci series generator.    
    def fibonacci_series_generator_ls(self): # Return a list of all the series/value at once
        series=[self.start_num, self.start_num + 1]
        fibo_num_limit= self.n
        
        while series[-1] + series[-2] <= fibo_num_limit:
            next_fibo_num = series[-1] + series[-2]
            series.append(next_fibo_num)    
        return series
            
    def fibonacci_series_generator_yi(self): # Memory efficient, uses a generator (yield)
        current_fibo_num = self.start_num
        next_fibo_num = self.start_num+1
        fibo_num_limit= self.n
        
        while current_fibo_num <= fibo_num_limit:
            yield current_fibo_num
            current_fibo_num, next_fibo_num = next_fibo_num, current_fibo_num + next_fibo_num


# Build a to-do list in python and use Postgres for persistent storage.
class To_Do():
    def __init__(self):
        self.conn = setup_db()
        self.database_setup()        
        
    # Create a Postgres database with tables.
    def database_setup(self):
        cur = self.conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS todo (
                id SERIAL PRIMARY KEY,
                task TEXT NOT NULL,
                status TEXT DEFAULT 'pending',
                last_edited TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
            );
        """)
        self.conn.commit()
        cur.close() 

    # Perform crud operations.
    def add_task(self, task): # (C)reate A New Task
        cur = self.conn.cursor()
        cur.execute("INSERT INTO todo (task) VALUES (%s)", (task,))
        self.conn.commit()
        print(f"Task added successfully.")
        cur.close()

    def view_task(self): # (R)ead Task
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM todo ORDER BY id ASC")
        rows = cur.fetchall()
        print(f"\n{' TASKS '.center(65,"#")}")
        print(f"|{'Task ID'.center(10, " ")} | {'Task'.center(35, " ")} | {'Status'.center(10, " ")} |".upper())
        for row in rows:
            print(f"| {str(row[0]).ljust(9, " ")} | {str(row[1]).ljust(35, " ")} | {str(row[2]).center(10, " ")} |".title())
        cur.close()
        print(f"\n{''.center(65,"#")}")
        

    def edit_task(self, task_id): # (U)pdate Task
        cur = self.conn.cursor()
        choice = input("Edit (T)ask or (S)tatus: ").lower()
        
        if choice == "t":
            updated_task = input("Enter new task: ")
            cur.execute("UPDATE todo SET task = %s WHERE id = %s", (updated_task, task_id))
        elif choice == "s":
            updated_status = input("Enter new status: ")
            cur.execute("UPDATE todo SET status = %s WHERE id = %s", (updated_status, task_id))
        
        self.conn.commit()
        cur.close()

    def delete_task(self, task_id): # (D)elete Task
        cur = self.conn.cursor()
        cur.execute("SELECT id FROM todo")
        all_id = cur.fetchall()
        # print(f"All ID: {all_id}")
        if task_id in all_id: 
            cur.execute("DELETE FROM todo WHERE id = %s", (task_id,))
            self.conn.commit()
            print(f"Task {task_id} deleted.")
            cur.close()
            self.view_task()
        else: print(f"No Task with ID Number {task_id}!")
        
        
class Scrape_Save_BabyNames():
    def __init__(self, html_file):
        self.html_file = html_file
        self.file_content = self.open_and_read_file()
        self.conn = setup_db()
        self.database_setup()      
        self.save_babynames_to_db()
          
    def database_setup(self):
        cur = self.conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS baby_names (
                id SERIAL PRIMARY KEY,
                name VARCHAR(100),
                gender VARCHAR(10),
                rank INTEGER
            );
        """)
        self.conn.commit()
        cur.close()
        
    def open_and_read_file(self):
        try:
            with open(self.html_file, "r") as file:
                print(f"{self.html_file} opened successfully!")
                return file.read()
        except FileNotFoundError:
            print(f"Error: {self.html_file} not found.")
            return ""
            
    def extract_baby_names(self):
        import re
        data_pattern = r'<td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>'
        matches = re.findall(data_pattern, self.file_content)
        return matches
    
    def save_babynames_to_db(self):
        extracted_data = self.extract_baby_names()
        cur = self.conn.cursor()
        
        for rank, boy, girl in extracted_data:
            # Insert Boy
            cur.execute("INSERT INTO baby_names (name, gender, rank) VALUES (%s, %s, %s)", (boy, "Male", rank))
            # Insert Girl
            cur.execute("INSERT INTO baby_names (name, gender, rank) VALUES (%s, %s, %s)", (girl, "Female", rank))
        
        self.conn.commit()
        print(f"Successfully saved {len(extracted_data) * 2} names to the database.")
        cur.close()
        self.conn.close()     
            
                