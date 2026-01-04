import os
import re

def main():
    # TASK 1: Create a text file that has your full name, and write code to read it and extract first name, middle name and last name.
    my_name = "Abdulazeez Abdulakeem Aramide"
    # Step 1: Create a text file with your full name
    with open("my_name.txt", "w") as f:
        f.write(my_name)

    # Step 2: Read the file and extract names
    with open("my_name.txt", "r") as f:
        content = f.read().split()
        print(f"Extraction: First Name: {content[0]}, Middle Name: {content[1]}, Last Name: {content[2]}")


    # TASK 2: Using the library os, print your local file path on screen.
    current_path = os.path.abspath("my_name.txt")
    print(f"Local file path: {current_path}")
    

    # TASK 3:Extraction of baby name from file using regex not using built-in libraries, create a sort algorithm, implement binary search.
    # Step 1: Define a function to extract names from HTML content
    def extract_names(html_content):
        # Regex to find: <td>Rank</td><td>Boy Name</td><td>Girl Name</td>
        # Match: <td>1</td><td>Jacob</td><td>Emma</td>
        pattern = r'<td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>'
        matches = re.findall(pattern, html_content)
        
        # Step 2: Flatten the list to just names for sorting/searching tasks
        all_names = []
        for rank, boy, girl in matches:
            all_names.append(boy)
            all_names.append(girl)
        return all_names

    # Step 3: Load baby2008.html file and extract names
    try:
        with open("baby2008.html", "r") as file:
            html_data = file.read()
        baby_names = extract_names(html_data)
        print(f"Extracted {len(baby_names)} names using Regex.")
    except FileNotFoundError:
        print("Error: baby2008.html not found. Please place it in the folder.")
        baby_names = []


    # Step 4: Implement Bubble Sort algorithm
    def bubble_sort(arr: list) -> list:
        n = len(arr) # Get the length of the array
        for i in range(n): # Loop through all array elements
            for j in range(0, n - i - 1): # Last i elements are already sorted
                if arr[j].lower() > arr[j + 1].lower(): # Use .lower() for safe alphabetizing
                    # Swap elements
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr


    # Step 5: Sort the extracted names
    sorted_names = bubble_sort(baby_names)
    # print(f"First 10 sorted names: {sorted_names[:10]}")
    print("Sorting Complete.")


    # Step 6: Implement Binary Search algorithm
    def binary_search(arr, target):
        low = 0 # Starting index
        high = len(arr) - 1 # Ending index
        
        while low <= high:
            mid = (low + high) // 2 # Middle index
            if arr[mid] == target: 
                return mid
            elif arr[mid] < target:
                low = mid + 1 # Move to the right half
            else:
                high = mid - 1 # Move to the left half
        return -1 # Target not found

        
    # Step 7: Test the Search
    search_name = "Aiden"
    result_index = binary_search(sorted_names, search_name)

    if result_index != -1:
        print(f"Success: '{search_name}' was found at index {result_index} in the sorted list!")
    else:
        print(f"Result: '{search_name}' was not found.")


if __name__ == "__main__":
    main()