# Jordan Drabek - Lab 5 - 11/8/2024

# lab 1 - calculator

def grade_calc():

    num_scores = int(input("Enter the number of scores: "))
    scores_list = []

    for i in range(num_scores):
        score = float(input(f"Enter score number {i+1}: "))
        scores_list.append(score)

    print(scores_list)

    avg_score = sum(scores_list)/len(scores_list)

    if avg_score >= 90:
        grade = "A"
    elif avg_score >= 80:
        grade = "B"
    elif avg_score >= 70:
        grade = "C"
    elif avg_score >= 60:
        grade = "D"
    else:
        grade = "F"
    
    print(f"Average Score: {avg_score:.2f}, Grade: {grade}")

# lab 2 - Even and Odds number counter

def odd_even():
    numbers = input("Enter integers seperated by spaces: ").split()

    numbers = [int(num) for num in numbers]

    even_count = sum(1 for num in numbers if num % 2 == 0)
    odd_count = sum(1 for num in numbers if num % 2 != 0)

    print(f"Even numbers count: {even_count}, Odd numbers count: {odd_count}")

# lab 3 - Unique list merger

def unique_list():
    while True:
        list1 = input("Enter the first list of numbers separated by spaces: ").split()
        list2 = input("Enter the second list of numbers separated by spaces: ").split()

        list1 = [int(num) for num in list1]
        list2 = [int(num) for num in list2]

        merged_list = list(set(list1 + list2))

        print("Merged list without duplicates:", merged_list)
        
        repeat = input("Do you want to merge another pair of lists? (yes/no): ").lower()

        if repeat == "no" or repeat == "exit":
            break
        
# Main function to prompt the user which lab to run

if __name__ == "__main__": 
    
    while True: 
        
        print("\nSelect a lab to run:") 
        print("1. Grade Calculator") 
        print("2. Even and Odd Numbers Counter") 
        print("3. Unique List Merger") 
        
        choice = input("Enter your choice (1/2/3): ") 
        
        if choice == "1": grade_calc() 
        elif choice == "2": odd_even() 
        elif choice == "3": unique_list() 
        else: print("Invalid choice. Please select 1, 2, or 3")