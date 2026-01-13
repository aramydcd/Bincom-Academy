from model import Fibonacci
from model import To_Do as Todo_App


class Menu():
    def __init__(self):
        self.GeneralMenu()
    
    
    def GeneralMenu(self):
        print(f"\n{' General Menu '.center(80,"#")}")
        input_key = input("\nChoose from the menu below: Press\n1. Fibonacci\n2. To-Do App\n0. Exit\n>> ".title())
        if input_key == "1": self.FibonacciGeneralMenu()
        elif input_key == "2": self.TodoAppMenu()
        elif input_key == "0": self.exit_program()
        else: 
            print("Invalid Key")
            self.GeneralMenu()


    def FibonacciGeneralMenu(self):
        print(f"\n{' Fibonacci Menu '.center(80,"#")}")
        self.fibonacci_obj = Fibonacci()
        input_key = input("\nChoose from the menu below to use method of fibonacci class: Press\n1. Calculate Fibonacci of a number\n2. Generate the fibonacci series\n0. Back\n>> ".title())
        if input_key == "1": self.FibonacciMenu_1()
        elif input_key == "2": self.FibonacciMenu_2()
        elif input_key == "0": self.GeneralMenu()
        else: 
            print("Invalid Key")
            self.FibonacciGeneralMenu()

            
    def FibonacciMenu_1(self):
        print(f"\n{' Calculate Fibonacci Of  A Number '.center(50,"#")}")
        while True:
            try:
                number = int(input("\nEnter the number: "))
                break
            except ValueError:
                print("Note: Only numerical value")
        
        print(f"\n{'#'*10} Fibonacci of {number} = {self.fibonacci_obj.fibonacci_of_num(number)}")
                
        self.goAgain(self.FibonacciMenu_1, self.FibonacciGeneralMenu)
     
       
    def FibonacciMenu_2(self):
        print(f"\n{' Fibonacci Series Generator '.center(80,"#")}")
        while True:
            try:
                starting_number = int(input("\nEnter the starting number of the fibonacci series: "))
                limit = int(input("\nEnter the limit of the fibonacci number series: "))
                break
            except ValueError:
                print("Note: Only numerical value")
        
        self.fibonacci_obj = Fibonacci(limit=limit, start_num=starting_number)
                
        while True:
            generatorMethodOption = input("\nChoose from the menu below the method to use in generating the fibonacci series : Press\n1. List\n2. Yield\n3. Both List and Yield\n>> ".title())
            
            if generatorMethodOption == "1": 
                print(f"\n{'#'*10} Fibonacci Series Generator (List):{self.fibonacci_obj.fibonacci_series_generator_ls()}")
                break
            elif generatorMethodOption == "2": 
                print(f"\n{'#'*10} Fibonacci Series Generator (Yield): {list(self.fibonacci_obj.fibonacci_series_generator_yi())}")
                break
            elif generatorMethodOption == "3":
                print(f"\n{'#'*10} Fibonacci Series Generator (Yield): {list(self.fibonacci_obj.fibonacci_series_generator_yi())}")
                print(f"\n{'#'*10} Fibonacci Series Generator (List):{self.fibonacci_obj.fibonacci_series_generator_ls()}")
                break
            else: print("Invalid Key")
        
        self.goAgain(self.FibonacciMenu_2, self.FibonacciGeneralMenu)
        

    def TodoAppMenu(self):
        print(f"\n{' To-Do App Menu '.center(80,"#")}")
        self.User = Todo_App()
        
        while True:
            input_key = input("\nChoose from the menu below operation you can perform on To-Do Class: Press\n1. Add new task\n2. View task\n3. Edit task\n4. Delete task\n0. Back\n>> ".title())
            
            if input_key == "1": 
                self.TodoAppMenu_1()
                break
            elif input_key == "2": 
                self.TodoAppMenu_2()
                break
            elif input_key == "3": 
                self.TodoAppMenu_3()
                break
            elif input_key == "4": 
                self.TodoAppMenu_4()
                break
            elif input_key == "0": 
                self.GeneralMenu()
                break
            else: 
                print("Invalid Key")

        
    def TodoAppMenu_1(self):
        print(f"\n{' add new task '.center(80,"#")}")
        taskDescription = input("Enter Task: ")
        self.User.add_task(task=taskDescription)
        self.goAgain(self.TodoAppMenu_1, self.TodoAppMenu)
        
        
    def TodoAppMenu_2(self):
        print(f"\n{' View task '.center(80,"#")}")
        self.User.view_task()
        self.TodoAppMenu()
        
        
    def TodoAppMenu_3(self): 
        print(f"\n{' Edit task '.center(80,"#")}")
        try:
            IdOfTaskToEdit = int(input("Enter ID of task you want to edit: "))
            self.User.edit_task(IdOfTaskToEdit)
        except ValueError:
            print("Only numerical value")
        self.goAgain(self.TodoAppMenu_3, self.TodoAppMenu)
        
            
    def TodoAppMenu_4(self): 
        print(f"\n{' Delete Task '.center(80,"#")}")
        IdOfTaskToDelete = int(input("Enter ID of task you want to delete: "))
        self.User.delete_task(IdOfTaskToDelete)
        self.goAgain(self.TodoAppMenu_4, self.TodoAppMenu)
        
    
    def goAgain(self, yes, no):
        while True:
            again = input("\nDo you want to continue? Yes or No: ".title()).lower()
            
            if again == "yes": 
                yes() 
                break
            elif again == "no": 
                no()
                break
            else: print("Invalid Key")
        
    def exit_program(self):
        print("Exiting Program... Goodbye!")
        exit()
