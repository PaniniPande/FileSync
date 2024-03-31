import aiohttp  
import asyncio  

# Function to display the menu options
async def display_menu():
    print("\nWelcome to the Calculation Service!")
    print("Choose an option:")
    print("1. Add two numbers")
    print("2. Sort a list of numbers")
    print("0. Exit")

# Function to get two numbers from the user
async def get_numbers():
    i = int(input("Enter the first number: "))
    j = int(input("Enter the second number: "))
    return i, j

# Function to get a list of numbers from the user
async def get_list():
    arr = [int(x) for x in input("Enter a list of numbers separated by spaces: ").split()]
    return arr

# Function to print the result
async def print_result(result):
    print(f"Result: {result}")

# Function to send an 'addition' request to the server
async def add_request(session, i, j):
    print("Sending 'addition' request to the server...")
    print("Waiting for 'addition' response...")
    async with session.post('http://localhost:8000/add', json={'i': i, 'j': j}) as response:
        result = await response.json()
        return result['result']

# Function to send a 'sort' request to the server
async def sort_array_request(session, arr):
    print("Sending 'sort' request to the server...")
    print("Waiting for 'sort' response...")
    async with session.post('http://localhost:8000/sort_array', json={'arr': arr}) as response:
        sorted_arr = await response.json()
        return sorted_arr['sorted_arr']

# Main asynchronous function
async def main():
    async with aiohttp.ClientSession() as session:
        while True:
            await display_menu()  # Display the menu
            choice = input("Enter your choice: ")

            if choice == "1":
                i, j = await get_numbers()  # Get two numbers from the user
                result = await add_request(session, i, j)  # Send 'addition' request to the server
                await print_result(result)  # Print the result
            elif choice == "2":
                arr = await get_list()  # Get a list of numbers from the user
                sorted_arr = await sort_array_request(session, arr)  # Send 'sort' request to the server
                await print_result(sorted_arr)  # Print the sorted array
            elif choice == "0":
                print("Exiting...")
                break  # Exit the loop and terminate the program
            else:
                print("Invalid input. Please enter a valid choice.")

if __name__ == "__main__":
    asyncio.run(main())  # Run the main asynchronous function
