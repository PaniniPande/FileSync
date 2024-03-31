import xmlrpc.client

# Function to display the menu options
def display_menu():
    print("\nWelcome to the Calculation Service!")
    print("Choose an option:")
    print("1. Add two numbers")
    print("2. Sort a list of numbers")
    print("0. Exit")
# Function to get two numbers from the user
def get_numbers():
    i = int(input("Enter the first number: "))
    j = int(input("Enter the second number: "))
    return i, j
# Function to get a list of numbers from the user
def get_list():
    arr = [int(x) for x in input("Enter a list of numbers separated by spaces: ").split()]
    return arr

def print_result(result):
    print(f"Result: {result}")
# Main block
if __name__ == "__main__":
     # Connect to the XML-RPC server
    with xmlrpc.client.ServerProxy("http://localhost:8000/RPC2") as proxy:
        while True:
            display_menu()
            choice = input("Enter your choice: ")

            if choice == "1":
                i, j = get_numbers()
                result = proxy.add(i, j)
                print_result(result)
            elif choice == "2":
                arr = get_list()
                result = proxy.sort_array(arr)
                print_result(result)
            elif choice == "0":
                print("Exiting...")
                break
            else:
                print("Invalid input. Please enter a valid choice.")
