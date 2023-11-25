import tkinter as tk
from PIL import Image, ImageTk
import csv
from tkinter import messagebox, Button
from tkinter import ttk
from datetime import datetime
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import Scrollbar
from Hash_ADT import HashTable
from Priority_Queue_ADT import PriorityQueue
from List_ADT import ArrayList
from Linked_list_ADT import LinkedList


def login():
    """Validate the username and password entered by the user and open the home page if login is successful."""
    global username_entry, password_entry, result_label

    # Get the username and password entered by the user
    username = username_entry.get()
    password = password_entry.get()

    # Open the users CSV file and check if the entered username and password match any user
    with open("users.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["Username"] == username and row["Password"] == password:
                result_label.config(text="Login Successful", fg="green")
                # Open the home page
                home_page()
                return

    # Display an error message if the username or password is invalid
    result_label.config(text="Invalid username or password", fg="red")



def register_page():
    """Display the register page for new user registration."""

    # Set the main Tkinter window
    root = tk.Tk()
    root.title("Register Page")  # Set the title of the window

    # Open the window in full-screen mode
    root.attributes("-fullscreen", True)

    # Set the background color
    root.configure(bg="lightblue")

    # Create a frame to hold the register widgets
    frame = tk.Frame(root, padx=20, pady=20, bg="lightblue")
    frame.pack(expand=True)

    # Create the heading label
    heading_label = tk.Label(
        frame,
        text="New User Registration ",
        font=("Arial", 18, "bold"),
        bg="lightblue",
        fg="blue",
    )
    heading_label.pack(pady=10)

    # Create labels and entry fields
    username_label = tk.Label(
        frame, text="Username:", font=("Arial", 12), bg="lightblue"
    )
    username_label.pack()

    username_entry = tk.Entry(frame, font=("Arial", 12), width=30)
    username_entry.pack(pady=5)

    password_label = tk.Label(
        frame, text="Password:", font=("Arial", 12), bg="lightblue"
    )
    password_label.pack()

    password_entry = tk.Entry(frame, show="*", font=("Arial", 12), width=30)
    password_entry.pack(pady=5)

    confirm_password_label = tk.Label(
        frame, text="Confirm Password:", font=("Arial", 12), bg="lightblue"
    )
    confirm_password_label.pack()

    confirm_password_entry = tk.Entry(frame, show="*", font=("Arial", 12), width=30)
    confirm_password_entry.pack(pady=5)


    # Function to handle registration
    def register_user():
        """Registers a user based on the entered username and password."""
        username = username_entry.get()
        password = password_entry.get()
        confirm_password = confirm_password_entry.get()

        # Check if passwords match
        if password != confirm_password:
            result_label.config(text="Passwords do not match", fg="red")
            return

        # Check if username meets the criteria
        if len(username) != 6 or not username.islower() or not username.isalnum():
            result_label.config(
                text="Username must be 6 lowercase alphanumeric characters", fg="red"
            )
            return

        # Check if password meets the criteria
        if (
            len(password) < 8
            or not any(char.isupper() for char in password)
            or not any(char.islower() for char in password)
            or not any(char.isdigit() for char in password)
            or not any(char in "!@#$%^&*()" for char in password)
        ):
            result_label.config(
                text="Password must be at least 8 characters long "
                "and contain at least one uppercase letter, one lowercase letter, "
                "one digit, and one special character",
                fg="red",
            )
            return

        # Check if user already exists
        with open("users.csv", "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row["Username"] == username:
                    result_label.config(text="Username already exists", fg="red")
                    return

        # Register the user
        with open("users.csv", "a", newline="") as file:
            fieldnames = ["Username", "Password"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writerow({"Username": username, "Password": password})

        result_label.config(text="Registration Successful", fg="green")

    # Create the main window
    root = tk.Tk()

    # Create a frame to hold the registration form elements
    frame = tk.Frame(root)
    frame.pack(padx=20, pady=20)

    # Create the username label and entry field
    username_label = tk.Label(frame, text="Username:", font=("Arial", 12))
    username_label.pack()
    username_entry = tk.Entry(frame, font=("Arial", 12))
    username_entry.pack(pady=5)

    # Create the password label and entry field
    password_label = tk.Label(frame, text="Password:", font=("Arial", 12))
    password_label.pack()
    password_entry = tk.Entry(frame, show="*", font=("Arial", 12))
    password_entry.pack(pady=5)

    # Create the confirm password label and entry field
    confirm_password_label = tk.Label(frame, text="Confirm Password:", font=("Arial", 12))
    confirm_password_label.pack()
    confirm_password_entry = tk.Entry(frame, show="*", font=("Arial", 12))
    confirm_password_entry.pack(pady=5)

    # Function to handle the registration process

    # Create a register button
    register_button = tk.Button(
        frame, text="Register", command=register_user, font=("Arial", 12), width=10
    )
    register_button.pack(pady=10)

    # Create a back button to close the register page window
    back_button = tk.Button(
        frame, text="Back", command=root.destroy, font=("Arial", 12), width=10
    )
    back_button.pack()

    # Create a label for displaying the registration result
    result_label = tk.Label(
        frame, text="", fg="green", font=("Arial", 12), bg="lightblue"
    )
    result_label.pack()

    # Create a text widget to display the registration conditions
    conditions_text = """
    Registration Conditions:
    - Username must be 6 lowercase alphanumeric characters.
    - Password must be at least 8 characters long.
    - Password must contain at least one uppercase letter, one lowercase letter,
    one digit, and one special character (!@#$%^&*()).
    """
    conditions_widget = tk.Text(
        frame, height=7, width=60, font=("Arial", 12), bg="grey"
    )
    conditions_widget.insert(tk.END, conditions_text)
    conditions_widget.configure(state="disabled")
    conditions_widget.pack()

    # Run the register page event loop
    root.mainloop()



opened_pages = []


def create_login_page():
    """Create and display the login page window."""

    global username_entry, password_entry, result_label, opened_pages

    # Create the main login page window
    window = tk.Tk()
    window.title("Login Page")

    # Open the window in full-screen mode
    window.attributes("-fullscreen", True)

    # Load and set the background image
    background_image = ImageTk.PhotoImage(Image.open("Login_image.jpg"))
    background_label = tk.Label(window, image=background_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    # Create a frame to hold the login widgets
    frame = tk.Frame(window, padx=20, pady=20)
    frame.pack(expand=True)

    # Create the heading label
    heading_label = tk.Label(
        frame, text="Medical Pharmacy system", font=("Arial", 18, "bold"), fg="blue"
    )
    heading_label.pack(pady=10)

    # Create labels and entry fields
    username_label = tk.Label(frame, text="Username:", font=("Arial", 12))
    username_label.pack()

    username_entry = tk.Entry(frame, font=("Arial", 12), width=30, highlightthickness=0)
    username_entry.pack(pady=5)

    password_label = tk.Label(frame, text="Password:", font=("Arial", 12))
    password_label.pack()

    password_entry = tk.Entry(
        frame, show="*", font=("Arial", 12), width=30, highlightthickness=0
    )
    password_entry.pack(pady=5)

    # Create login button
    login_button = tk.Button(
        frame, text="Login", command=login, font=("Arial", 12), width=10
    )
    login_button.pack(pady=10)

    # Create a register button to open the register page
    register_button = tk.Button(
        frame, text="Register", command=register_page, font=("Arial", 12), width=10
    )
    register_button.pack()

    # Create a label for displaying the login result
    result_label = tk.Label(frame, text="", fg="red", font=("Arial", 12))
    result_label.pack()

    def close_all_pages():
        """Close all opened pages and the login page."""

        # Close all opened pages
        for page in opened_pages:
            page.destroy()

        # Close the login page
        window.destroy()

    # Create a close button to close all opened pages
    close_button = tk.Button(
        window, text="Close All", command=close_all_pages, font=("Arial", 12), width=10
    )
    close_button.pack()

    # Run the main window event loop
    window.mainloop()



def home_page():
    """Create and display the home page window."""

    global home_window

    def back_to_login():
        """Close the home page and return to the login page."""

        # Close the home page
        home_window.destroy()

    # Create the home page window
    home_window = tk.Tk()
    home_window.title("Home Page")

    # Open the window in full-screen mode
    home_window.attributes("-fullscreen", True)

    # Set the background color
    home_window.configure(bg="lightblue")

    # Create a frame to hold the home page content
    frame = tk.Frame(home_window, padx=20, pady=20, bg="lightblue")
    frame.pack(expand=True)

    # Create the heading label
    heading_label = tk.Label(
        frame,
        text="Welcome to the Home Page!",
        font=("Arial", 18, "bold"),
        bg="lightblue",
        fg="blue",
    )
    heading_label.pack(pady=10)

    # Create a billing button
    billing_button = tk.Button(
        frame, text="Billing", command=billing_page, font=("Arial", 12), width=20
    )
    billing_button.pack(pady=5)

    # Create a display stock button
    stock_button = tk.Button(
        frame, text="Display Stock", command=display_stock, font=("Arial", 12), width=20
    )
    stock_button.pack(pady=5)

    # Create a soon to expire medicines button
    soon_expire_button = tk.Button(
        frame,
        text="Soon to Expire Medicines",
        command=soon_to_expire_page,
        font=("Arial", 12),
        width=20,
    )
    soon_expire_button.pack(pady=5)

    # Create an expired medicines button
    expired_button = tk.Button(
        frame,
        text="Expired Medicines",
        command=expired_medicines_page,
        font=("Arial", 12),
        width=20,
    )
    expired_button.pack(pady=5)

    # Create a soon to out of stock button
    soon_out_of_stock_button = tk.Button(
        frame,
        text="Soon to Out of Stock",
        command=soon_to_out_of_stock_page,
        font=("Arial", 12),
        width=20,
    )
    soon_out_of_stock_button.pack(pady=5)

    # Create an out of stock button
    out_of_stock_button = tk.Button(
        frame,
        text="Out of Stock",
        command=out_of_stock_page,
        font=("Arial", 12),
        width=20,
    )
    out_of_stock_button.pack(pady=5)

    # Create a day-wise sales report button
    day_sales_button = tk.Button(
        frame,
        text="Daily-wise Sales Report",
        command=day_sales_page,
        font=("Arial", 12),
        width=20,
    )
    day_sales_button.pack(pady=5)

    # Create a month-wise sales report button
    month_sales_button = tk.Button(
        frame,
        text="Month-wise Sales Report",
        command=monthly_sales_page,
        font=("Arial", 12),
        width=20,
    )
    month_sales_button.pack(pady=5)

    # Create an annual sales report button
    annual_sales_button = tk.Button(
        frame,
        text="Annual Sales Report",
        command=yearly_sales_page,
        font=("Arial", 12),
        width=20,
    )
    annual_sales_button.pack(pady=5)

    # Create a back button to return to the login page
    back_button = tk.Button(
        frame, text="Back", command=back_to_login, font=("Arial", 12), width=10
    )
    back_button.pack()

    # Run the home page event loop
    home_window.mainloop()


def billing_page():
    """
    Create and display the billing page window.
    """
    def add_medicine():
        """Add a medicine to the selected medicines list."""
        medicine_id = medicine_id_entry.get()
        quantity = quantity_entry.get()

        # Check if the medicine ID and quantity are provided
        if medicine_id == "" or quantity == "":
            messagebox.showwarning(
                "Warning", "Please provide medicine ID and quantity."
            )
            return

        # Check if the medicine ID is valid
        medicine_info = load_medicine_info()
        if not validate_medicine_id(medicine_id, medicine_info):
            messagebox.showwarning("Warning", "Invalid medicine ID.")
            return

        # Check if the quantity is valid and available
        if not validate_quantity(quantity, medicine_id, medicine_info):
            messagebox.showwarning("Warning", "Invalid quantity or out of stock.")
            return

        # Add the medicine to the linked list
        medicine_name = medicine_info[medicine_id]["Medicine Name"]
        selected_medicines.add((medicine_id, medicine_name, int(quantity)))

        # Clear the entry fields
        medicine_id_entry.delete(0, tk.END)
        quantity_entry.delete(0, tk.END)

        messagebox.showinfo("Success", "Medicine added to the list.")

    def validate_medicine_id(medicine_id, medicine_info):
        """Validate the provided medicine ID."""
        # Check if the medicine ID exists in the medicine_info dictionary
        return medicine_id in medicine_info

    def validate_quantity(quantity, medicine_id, medicine_info):
        """Validate the provided quantity for the medicine ID."""
        # Check if the quantity is valid and available for the given medicine ID
        if not quantity.isdigit() or int(quantity) <= 0:
            return False

        available_quantity = int(medicine_info[medicine_id]["Quantity"])
        return int(quantity) <= available_quantity

    def load_medicine_info():
        """Load the medicine information from the CSV file."""
        medicine_info = {}
        with open("medicines_list.csv", "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                medicine_id = row["Medicine ID"]
                medicine_info[medicine_id] = row
        return medicine_info


    def save_stock(stock):
        """
        Save the stock of medicines to a CSV file.

        Args:
            stock (dict): The dictionary representing the stock of medicines.

        """
        fieldnames = [
            "Medicine ID",
            "Medicine Name",
            "Quantity",
            "Price",
            "Expiry Date",
        ]
        with open("medicines_list.csv", "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(stock.values())


    def load_stock():
        """
        Load the stock of medicines from a CSV file.

        Returns:
            dict: The dictionary representing the stock of medicines.

        """
        stock = {}
        with open("medicines_list.csv", "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                medicine_id = row["Medicine ID"]
                stock[medicine_id] = row
        return stock


    def update_stock_quantity(medicine_id, quantity):
        """
        Update the quantity of a medicine in the stock.

        Args:
            medicine_id (str): The ID of the medicine to update.
            quantity (int): The quantity to subtract from the current stock.

        """
        # Load the current stock from the CSV file
        stock = load_stock()

        # Update the quantity for the specified medicine
        if medicine_id in stock:
            current_quantity = int(stock[medicine_id]["Quantity"])
            updated_quantity = current_quantity - quantity
            stock[medicine_id]["Quantity"] = str(updated_quantity)

        # Save the updated stock back to the CSV file
        save_stock(stock)


    def print_bill(medicines):
        customer_name = customer_name_entry.get()
        contact_number = contact_number_entry.get()

        # Check if customer details are provided
        if customer_name == "" or contact_number == "":
            messagebox.showwarning("Warning", "Please provide customer details.")
            return

        # Check if any medicines are selected
        if medicines.is_empty():
            messagebox.showwarning("Warning", "Please select at least one medicine.")
            return

        # Calculate the total bill amount
        total_amount = calculate_total_amount(medicines)

        # Create the bill
        bill_text = (
            f"Customer Name: {customer_name}\nContact Number: {contact_number}\n\n"
        )
        bill_text += "Selected Medicines:\n"
        current = medicines.get_head()
        index = 1
        while current:
            medicine_id, medicine_name, quantity = current.data
            bill_text += f"{index}. Medicine ID: {medicine_id}, Medicine Name: {medicine_name}, Quantity: {quantity}\n"
            current = current.next
            index += 1
        bill_text += f"\nTotal Amount: {total_amount}"

        # Display the bill in a message box
        messagebox.showinfo("Bill", bill_text)

        # Write the sales details to the sales_tracking.csv file
        sale_date = datetime.now().strftime("%Y-%m-%d")
        medicine_info = load_medicine_info()
        sales_data = []
        current = medicines.get_head()
        while current:
            medicine_id, medicine_name, quantity = current.data
            sales_data.append(
                [
                    sale_date,
                    customer_name,
                    contact_number,
                    medicine_id,
                    medicine_name,
                    quantity,
                    medicine_info[medicine_id]["Price"],
                ]
            )
            current = current.next

        with open("sales_tracking.csv", "a", newline="") as file:
            writer = csv.writer(file)
            for sale in sales_data:
                writer.writerow(sale)
        current = medicines.get_head()
        while current:
            medicine_id, medicine_name, quantity = current.data
            update_stock_quantity(medicine_id, quantity)
            current = current.next

        # Update the displayed stock
        display_stock()
        # Clear the customer details and selected medicines
        customer_name_entry.delete(0, tk.END)
        contact_number_entry.delete(0, tk.END)
        medicines.clear()

    def calculate_total_amount(medicines):
        total_amount = 0
        current = medicines.get_head()
        while current:
            medicine_id, medicine_name, quantity = current.data
            medicine_info = load_medicine_info()
            medicine_price = float(medicine_info[medicine_id]["Price"])
            total_amount += medicine_price * quantity
            current = current.next
        return total_amount

    def display_stock():
        stock = load_stock()
        stock_tree.delete(*stock_tree.get_children())  # Clear existing data
        for medicine_id, data in stock.items():
            medicine_name = data["Medicine Name"]
            quantity = data["Quantity"]
            stock_tree.insert("", "end", values=(medicine_id, medicine_name, quantity))

    billing_window = tk.Tk()
    billing_window.title("Billing Page")

    # Open the window in full-screen mode
    billing_window.attributes("-fullscreen", True)

    # Set the background color
    billing_window.configure(bg="lightblue")

    # Create a frame to hold the billing page content
    frame = tk.Frame(billing_window, padx=20, pady=20, bg="lightblue")
    frame.pack(expand=True)

    # Create the heading label
    heading_label = tk.Label(
        frame,
        text="Billing Page",
        font=("Arial", 18, "bold"),
        bg="lightblue",
        fg="blue",
    )
    heading_label.pack(pady=10)

    # Create labels and entry fields for customer details
    customer_name_label = tk.Label(
        frame, text="Customer Name:", font=("Arial", 12), bg="lightblue"
    )
    customer_name_label.pack()

    customer_name_entry = tk.Entry(frame, font=("Arial", 12), width=30)
    customer_name_entry.pack(pady=5)

    contact_number_label = tk.Label(
        frame, text="Contact Number:", font=("Arial", 12), bg="lightblue"
    )
    contact_number_label.pack()

    contact_number_entry = tk.Entry(frame, font=("Arial", 12), width=30)
    contact_number_entry.pack(pady=5)

    # Create labels and entry fields for selecting medicines
    medicine_id_label = tk.Label(
        frame, text="Medicine ID:", font=("Arial", 12), bg="lightblue"
    )
    medicine_id_label.pack()

    medicine_id_entry = tk.Entry(frame, font=("Arial", 12), width=30)
    medicine_id_entry.pack(pady=5)

    quantity_label = tk.Label(
        frame, text="Quantity:", font=("Arial", 12), bg="lightblue"
    )
    quantity_label.pack()

    quantity_entry = tk.Entry(frame, font=("Arial", 12), width=30)
    quantity_entry.pack(pady=5)

    # Create a linked list to store selected medicines
    selected_medicines = LinkedList()

    # Create an "Add Medicine" button
    add_medicine_button = tk.Button(
        frame, text="Add Medicine", command=add_medicine, font=("Arial", 12), width=15
    )
    add_medicine_button.pack(pady=10)

    # Create a "Print Bill" button
    print_bill_button = tk.Button(
        frame,
        text="Print Bill",
        command=lambda: print_bill(selected_medicines),
        font=("Arial", 12),
        width=15,
    )
    print_bill_button.pack(pady=10)

    # Create a "Back" button to return to the home page
    back_button = tk.Button(
        frame, text="Back", command=billing_window.destroy, font=("Arial", 12), width=15
    )
    back_button.pack()

    # Create a Frame to hold the stock Treeview and Scrollbar
    stock_frame = tk.Frame(frame, bg="lightblue")
    stock_frame.pack(pady=10)

    # Create a Treeview widget to display the stock
    stock_tree = ttk.Treeview(
        stock_frame,
        columns=("Medicine ID", "Medicine Name", "Quantity"),
        show="headings",
    )
    stock_tree.heading("Medicine ID", text="Medicine ID")
    stock_tree.heading("Medicine Name", text="Medicine Name")
    stock_tree.heading("Quantity", text="Quantity")
    stock_tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # Create a Scrollbar widget and associate it with the Treeview
    scrollbar = ttk.Scrollbar(stock_frame, orient=tk.VERTICAL, command=stock_tree.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    stock_tree.configure(yscrollcommand=scrollbar.set)

    # Display the initial stock
    display_stock()

    # Run the billing page event loop
    billing_window.mainloop()


def display_stock():
    global tree, stock_window, medicine_table

    def back_to_home():
        # Close the stock page
        stock_window.destroy()

        # Create a new window for displaying stock

    stock_window = tk.Toplevel()
    stock_window.title("Stock")

    # Create a frame to hold the treeview and scrollbar
    tree_frame = ttk.Frame(stock_window)
    tree_frame.pack(fill="both", expand=True)

    # Create the 'tree' widget
    tree = ttk.Treeview(
        tree_frame,
        columns=("Medicine ID", "Medicine Name", "Quantity", "Price", "Expiry Date"),
        height=10,
    )
    tree.heading("Medicine ID", text="Medicine ID")
    tree.heading("Medicine Name", text="Medicine Name")
    tree.heading("Quantity", text="Quantity")
    tree.heading("Price", text="Price")
    tree.heading("Expiry Date", text="Expiry Date")

    # Create a vertical scrollbar
    scrollbar = ttk.Scrollbar(tree_frame, orient="vertical", command=tree.yview)

    # Configure the 'tree' widget to use the scrollbar
    tree.configure(yscrollcommand=scrollbar.set)

    # Place the 'tree' widget and scrollbar in the frame
    tree.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    # Open the window in full-screen mode
    stock_window.attributes("-fullscreen", True)

    # Set the background color
    stock_window.configure(bg="lightblue")

    # Read the medicines list from CSV
    with open("medicines_list.csv", "r") as file:
        reader = csv.DictReader(file)
        medicines = list(reader)

    # Check if the CSV file contains the expected column headers
    expected_headers = [
        "Medicine ID",
        "Medicine Name",
        "Quantity",
        "Price",
        "Expiry Date",
    ]
    csv_headers = reader.fieldnames
    if not set(expected_headers).issubset(csv_headers):
        raise ValueError("Invalid CSV file headers")

    # Create a hash table for storing medicines by ID
    medicine_table = HashTable(len(medicines))

    # Insert medicines data into the hash table and the treeview
    for medicine in medicines:
        medicine_id = medicine["Medicine ID"]
        medicine_table.insert(medicine_id, medicine)
        tree.insert(
            "",
            "end",
            values=(
                medicine["Medicine ID"],
                medicine["Medicine Name"],
                medicine["Quantity"],
                medicine["Price"],
                medicine["Expiry Date"],
            ),
        )

    # Configure the tree table width
    tree.column("#0", width=0, stretch=tk.NO)  # Hide the first column
    tree.column("Medicine ID", width=100)
    tree.column("Medicine Name", width=200)
    tree.column("Quantity", width=100)
    tree.column("Price", width=100)
    tree.column("Expiry Date", width=100)

    # Configure the scrollbar to adjust to the tree table size
    tree.update_idletasks()
    scrollbar.configure(command=tree.yview)

    # Center the tree and scrollbar in the window
    tree_frame.pack_configure(padx=150, pady=150)
    tree_frame.pack_propagate(False)  # Disable automatic resizing of the frame

    def search_medicine():
        search_query = search_entry.get()
        if not search_query:
            messagebox.showwarning("Warning", "Please enter a search query.")
            return

        results = []  # List to store matching medicines

        # Open and read the CSV file
        with open("medicines_list.csv", "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row["Medicine Name"].lower().startswith(search_query.lower()):
                    results.append(row)

        if results:
            result_message = "Matching medicines found:\n\n"
            for result in results:
                result_message += (
                    f"Medicine ID: {result['Medicine ID']}\n"
                    f"Medicine Name: {result['Medicine Name']}\n"
                    f"Quantity: {result['Quantity']}\n"
                    f"Price: {result['Price']}\n"
                    f"Expiry Date: {result['Expiry Date']}\n\n"
                )
            messagebox.showinfo("Search Result", result_message)
        else:
            messagebox.showinfo("Search Result", "No matching medicines found.")

    # Create a search box and button
    search_frame = ttk.Frame(stock_window)
    search_frame.pack(pady=10)

    search_label = ttk.Label(search_frame, text="Search Medicine:", font=("Arial", 12))
    search_label.grid(row=0, column=0)

    search_entry = ttk.Entry(search_frame, font=("Arial", 12), width=30)
    search_entry.grid(row=0, column=1)

    search_button = ttk.Button(search_frame, text="Search", command=search_medicine)
    search_button.grid(row=0, column=2)

    def add_new_medicine():
        # Create a new window for adding a new medicine
        add_window = tk.Toplevel(stock_window)
        add_window.title("Add New Medicine")
        add_window.configure(background="lightblue")

        # Set the window dimensions and position it in the center of the screen
        window_width = 300
        window_height = 250
        screen_width = add_window.winfo_screenwidth()
        screen_height = add_window.winfo_screenheight()
        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)
        add_window.geometry(f"{window_width}x{window_height}+{x}+{y}")

        # Create labels and entry fields for medicine details
        medicine_id_label = tk.Label(
            add_window, text="Medicine ID:", font=("Arial", 12)
        )
        medicine_id_label.pack()

        medicine_id_entry = tk.Entry(add_window, font=("Arial", 12), width=30)
        medicine_id_entry.pack(pady=5)

        medicine_name_label = tk.Label(
            add_window, text="Medicine Name:", font=("Arial", 12)
        )
        medicine_name_label.pack()

        medicine_name_entry = tk.Entry(add_window, font=("Arial", 12), width=30)
        medicine_name_entry.pack(pady=5)

        quantity_label = tk.Label(add_window, text="Quantity:", font=("Arial", 12))
        quantity_label.pack()

        quantity_entry = tk.Entry(add_window, font=("Arial", 12), width=30)
        quantity_entry.pack(pady=5)

        price_label = tk.Label(add_window, text="Price:", font=("Arial", 12))
        price_label.pack()

        price_entry = tk.Entry(add_window, font=("Arial", 12), width=30)
        price_entry.pack(pady=5)

        expiry_label = tk.Label(add_window, text="Expiry Date:", font=("Arial", 12))
        expiry_label.pack()

        expiry_entry = tk.Entry(add_window, font=("Arial", 12), width=30)
        expiry_entry.pack(pady=5)

        def add_medicine():
            global stock_window, medicine_table
            new_medicine_id = medicine_id_entry.get()
            new_medicine_name = medicine_name_entry.get()
            new_quantity = quantity_entry.get()
            new_price = price_entry.get()
            new_expiry = expiry_entry.get()

            # Check if any field is empty
            if (
                new_medicine_id == ""
                or new_medicine_name == ""
                or new_quantity == ""
                or new_price == ""
                or new_expiry == ""
            ):
                messagebox.showwarning("Warning", "Please fill in all the fields.")
                return

            # Append the new medicine to the CSV file
            with open("medicines_list.csv", "a", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(
                    [
                        new_medicine_id,
                        new_medicine_name,
                        new_quantity,
                        new_price,
                        new_expiry,
                    ]
                )

            messagebox.showinfo("Success", "New medicine added.")
            stock_window.destroy()
            add_window.destroy()

            display_stock()

        # Create a button to add the new medicine
        add_button = tk.Button(
            add_window,
            text="Add Medicine",
            command=add_medicine,
            font=("Arial", 12),
            width=15,
        )
        add_button.pack(pady=10)

    def delete_medicine():
        global tree, stock_window

        selected_item = tree.selection()
        if not selected_item:
            messagebox.showwarning("Warning", "Please select a medicine to delete.")
            return

        confirmation = messagebox.askyesno(
            "Confirmation", "Are you sure you want to delete the selected medicine?"
        )
        if confirmation:
            # Delete the selected medicine from the CSV file
            selected_medicine_id = tree.set(selected_item, "Medicine ID")
            with open("medicines_list.csv", "r") as file:
                reader = csv.reader(file)
                rows = list(reader)

            with open("medicines_list.csv", "w", newline="") as file:
                writer = csv.writer(file)
                for row in rows:
                    if row[0] != selected_medicine_id:
                        writer.writerow(row)

            messagebox.showinfo("Success", "Medicine deleted.")
            stock_window.destroy()

            display_stock()

    def increase_quantity():
        global tree

        selected_item = tree.selection()
        if not selected_item:
            messagebox.showwarning(
                "Warning", "Please select a medicine to increase the quantity."
            )
            return

        # Get the selected medicine details
        selected_medicine_id = tree.set(selected_item, "Medicine ID")
        selected_medicine_name = tree.set(selected_item, "Medicine Name")
        current_quantity = tree.set(selected_item, "Quantity")

        # Create a new window to enter the quantity to increase
        increase_window = tk.Toplevel(stock_window)
        increase_window.title("Increase Quantity")
        increase_window.configure(background="lightblue")

        # Set the window dimensions and position it in the center of the screen
        window_width = 300
        window_height = 200
        screen_width = increase_window.winfo_screenwidth()
        screen_height = increase_window.winfo_screenheight()
        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)
        increase_window.geometry(f"{window_width}x{window_height}+{x}+{y}")

        # Create a label and entry field for the new quantity
        quantity_label = tk.Label(
            increase_window, text="New Quantity:", font=("Arial", 12)
        )
        quantity_label.pack()

        quantity_entry = tk.Entry(increase_window, font=("Arial", 12), width=30)
        quantity_entry.pack(pady=5)

        def increase_quantity():
            new_quantity = quantity_entry.get()

            # Check if the new quantity is valid
            if not new_quantity.isdigit() or int(new_quantity) <= 0:
                messagebox.showwarning("Warning", "Invalid quantity.")
                return

            # Update the quantity in the CSV file
            with open("medicines_list.csv", "r") as file:
                reader = csv.reader(file)
                rows = list(reader)

            with open("medicines_list.csv", "w", newline="") as file:
                writer = csv.writer(file)
                for row in rows:
                    if row[0] == selected_medicine_id:
                        row[2] = new_quantity
                    writer.writerow(row)

            messagebox.showinfo("Success", "Quantity increased.")
            increase_window.destroy()
            display_stock()

        # Create a button to increase the quantity
        increase_button = tk.Button(
            increase_window,
            text="Increase Quantity",
            command=increase_quantity,
            font=("Arial", 12),
            width=15,
        )
        increase_button.pack(pady=10)

    def update_stock():
        global tree

        # Prompt for confirmation before updating the stock
        confirmation = messagebox.askyesno(
            "Confirmation", "Are you sure you want to update the stock?"
        )
        if confirmation:
            # Read the updated stock from the treeview
            updated_stock = []
            for child in tree.get_children():
                medicine_id = tree.item(child)["values"][0]
                medicine_name = tree.item(child)["values"][1]
                quantity = tree.item(child)["values"][2]
                price = tree.item(child)["values"][3]
                expiry_date = tree.item(child)["values"][4]
                updated_stock.append(
                    {
                        "Medicine ID": medicine_id,
                        "Medicine Name": medicine_name,
                        "Quantity": quantity,
                        "Price": price,
                        "Expiry Date": expiry_date,
                    }
                )

            # Write the updated stock back to the CSV file
            with open("medicines_list.csv", "w", newline="") as file:
                writer = csv.DictWriter(file, fieldnames=expected_headers)
                writer.writeheader()
                writer.writerows(updated_stock)

            messagebox.showinfo("Success", "Stock updated successfully.")

    # Create buttons for modifying the stock
    add_medicine_button = tk.Button(
        stock_window,
        text="Add New Medicine",
        command=add_new_medicine,
        font=("Arial", 12),
        width=20,
    )
    add_medicine_button.pack(pady=5)

    delete_medicine_button = tk.Button(
        stock_window,
        text="Delete Medicine",
        command=delete_medicine,
        font=("Arial", 12),
        width=20,
    )
    delete_medicine_button.pack(pady=5)

    increase_quantity_button = tk.Button(
        stock_window,
        text="Increase Quantity",
        command=increase_quantity,
        font=("Arial", 12),
        width=20,
    )
    increase_quantity_button.pack(pady=5)

    update_stock_button = tk.Button(
        stock_window,
        text="Update Stock",
        command=update_stock,
        font=("Arial", 12),
        width=20,
    )
    update_stock_button.pack(pady=5)

    # Create a back button to return to the login page
    back_button = tk.Button(
        stock_window, text="Back", command=back_to_home, font=("Arial", 12), width=10
    )
    back_button.pack()

    stock_window.mainloop()


def out_of_stock_page():
    def show_notification():
        messagebox.showinfo(
            "Notification", "A medicine has been added to the Out of Stock page."
        )

    def delete_medicine():
        selected_item = tree.selection()
        if selected_item:
            tree.delete(selected_item)
            messagebox.showinfo("Notification", "Medicine deleted successfully.")
        else:
            messagebox.showwarning("Warning", "Please select a medicine to delete.")

    # Create the out of stock page window
    out_of_stock_window = tk.Toplevel()
    out_of_stock_window.title("Out of Stock Page")

    # Open the window in full-screen mode
    out_of_stock_window.attributes("-fullscreen", True)

    # Set the background color
    out_of_stock_window.configure(bg="lightblue")

    # Read the medicines list from CSV
    with open("medicines_list.csv", "r") as file:
        reader = csv.DictReader(file)
        medicines = list(reader)

    # Create a priority queue for out of stock medicines
    priority_queue = PriorityQueue()

    # Check if there are any out of stock medicines and add them to the priority queue
    for medicine in medicines:
        if int(medicine["Quantity"]) == 0:
            priority_queue.insert(
                medicine, 0
            )  # Priority is set to 0 for all out of stock medicines

    # Display a notification if a medicine is added to the out of stock page
    if not priority_queue.is_empty():
        show_notification()

    # Create a label to display the out of stock medicines
    heading_label = tk.Label(
        out_of_stock_window,
        text="Out of Stock Medicines",
        font=("Arial", 14),
        bg="lightblue",
    )
    heading_label.pack(pady=10)

    # Create a frame to hold the treeview and scrollbar
    tree_frame = ttk.Frame(out_of_stock_window)
    tree_frame.pack(fill="both", expand=True)

    # Create a treeview to display the out of stock medicines
    tree = ttk.Treeview(tree_frame)
    tree["columns"] = (
        "Medicine ID",
        "Medicine Name",
        "Quantity",
        "Price",
        "Expiry Date",
        "Action",
    )

    # Define column headings
    tree.heading("Medicine ID", text="Medicine ID")
    tree.heading("Medicine Name", text="Medicine Name")
    tree.heading("Quantity", text="Quantity")
    tree.heading("Price", text="Price")
    tree.heading("Expiry Date", text="Expiry Date")
    tree.heading("Action", text="Action")

    # Create a vertical scrollbar
    scrollbar = Scrollbar(tree_frame, orient="vertical", command=tree.yview)

    # Configure the 'tree' widget to use the scrollbar
    tree.configure(yscrollcommand=scrollbar.set)

    # Place the 'tree' widget and scrollbar in the frame
    tree.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    # Insert out of stock medicines data into the treeview
    while not priority_queue.is_empty():
        medicine = priority_queue.remove()
        tree.insert(
            "",
            "end",
            values=(
                medicine["Medicine ID"],
                medicine["Medicine Name"],
                medicine["Quantity"],
                medicine["Price"],
                medicine["Expiry Date"],
                "Delete",
            ),
        )

    # Create a delete button
    delete_button = Button(
        out_of_stock_window, text="Delete", command=delete_medicine, font=("Arial", 12)
    )
    delete_button.pack(pady=10)

    # Create a back button
    back_button = tk.Button(
        out_of_stock_window,
        text="Back",
        command=out_of_stock_window.destroy,
        font=("Arial", 12),
    )
    back_button.pack(pady=10)

    # Run the out of stock page event loop
    out_of_stock_window.mainloop()


def soon_to_out_of_stock_page():
    def show_notification():
        messagebox.showinfo(
            "Notification",
            "A medicine has been added to the Soon to Out of Stock page.",
        )

    def delete_medicine():
        selected_item = tree.selection()
        if selected_item:
            tree.delete(selected_item)
            messagebox.showinfo("Notification", "Medicine deleted successfully.")
        else:
            messagebox.showwarning("Warning", "Please select a medicine to delete.")

    # Create the soon to out of stock page window
    soon_to_out_of_stock_window = tk.Toplevel()
    soon_to_out_of_stock_window.title("Soon to Out of Stock Page")

    # Open the window in full-screen mode
    soon_to_out_of_stock_window.attributes("-fullscreen", True)

    # Set the background color
    soon_to_out_of_stock_window.configure(bg="lightblue")

    # Read the medicines list from CSV
    with open("medicines_list.csv", "r") as file:
        reader = csv.DictReader(file)
        medicines = list(reader)

    # Create a priority queue for soon to out of stock medicines
    priority_queue = PriorityQueue()

    # Check if there are any soon to out of stock medicines and add them to the priority queue
    for medicine in medicines:
        quantity = int(medicine["Quantity"])
        if 0 < quantity <= 30:
            priority_queue.insert(
                medicine, quantity
            )  # Priority is set to the quantity for soon to out of stock medicines

    # Display a notification if a medicine is added to the soon to out of stock page
    if not priority_queue.is_empty():
        show_notification()

    # Create a label to display the soon to out of stock medicines
    heading_label = tk.Label(
        soon_to_out_of_stock_window,
        text="Soon to Out of Stock Medicines",
        font=("Arial", 14),
        bg="lightblue",
    )
    heading_label.pack(pady=10)

    # Create a frame to hold the treeview and scrollbar
    tree_frame = ttk.Frame(soon_to_out_of_stock_window)
    tree_frame.pack(fill="both", expand=True)

    # Create a treeview to display the soon to out of stock medicines
    tree = ttk.Treeview(tree_frame)
    tree["columns"] = (
        "Medicine ID",
        "Medicine Name",
        "Quantity",
        "Price",
        "Expiry Date",
        "Action",
    )

    # Define column headings
    tree.heading("Medicine ID", text="Medicine ID")
    tree.heading("Medicine Name", text="Medicine Name")
    tree.heading("Quantity", text="Quantity")
    tree.heading("Price", text="Price")
    tree.heading("Expiry Date", text="Expiry Date")
    tree.heading("Action", text="Action")

    # Create a vertical scrollbar
    scrollbar = Scrollbar(tree_frame, orient="vertical", command=tree.yview)

    # Configure the 'tree' widget to use the scrollbar
    tree.configure(yscrollcommand=scrollbar.set)

    # Place the 'tree' widget and scrollbar in the frame
    tree.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    # Insert soon to out of stock medicines data into the treeview
    while not priority_queue.is_empty():
        medicine = priority_queue.remove()
        tree.insert(
            "",
            "end",
            values=(
                medicine["Medicine ID"],
                medicine["Medicine Name"],
                medicine["Quantity"],
                medicine["Price"],
                medicine["Expiry Date"],
                "Delete",
            ),
        )

    # Create a delete button
    delete_button = Button(
        soon_to_out_of_stock_window,
        text="Delete",
        command=delete_medicine,
        font=("Arial", 12),
    )
    delete_button.pack(pady=10)

    # Create a back button
    back_button = tk.Button(
        soon_to_out_of_stock_window,
        text="Back",
        command=soon_to_out_of_stock_window.destroy,
        font=("Arial", 12),
    )
    back_button.pack(pady=10)

    # Run the soon to out of stock page event loop
    soon_to_out_of_stock_window.mainloop()


def soon_to_expire_page():
    def show_notification():
        messagebox.showinfo(
            "Notification", "A medicine has been added to the Soon to Expire page."
        )

    def delete_medicine():
        selected_item = tree.selection()
        if selected_item:
            tree.delete(selected_item)
            messagebox.showinfo("Notification", "Medicine deleted successfully.")
        else:
            messagebox.showwarning("Warning", "Please select a medicine to delete.")

    # Create the soon to expire page window
    soon_to_expire_window = tk.Toplevel()
    soon_to_expire_window.title("Soon to Expire Medicines")

    # Open the window in full-screen mode
    soon_to_expire_window.attributes("-fullscreen", True)

    # Set the background color
    soon_to_expire_window.configure(bg="lightblue")

    # Read the medicines list from CSV
    with open("medicines_list.csv", "r") as file:
        reader = csv.DictReader(file)
        medicines = list(reader)

    # Check if there are any soon to expire medicines
    soon_to_expire_medicines = []
    current_date = datetime.now()

    # Create a priority queue for soon to expire medicines
    priority_queue = PriorityQueue()

    for medicine in medicines:
        expiry_date = datetime.strptime(medicine["Expiry Date"], "%Y-%m-%d")
        days_until_expiry = (expiry_date - current_date).days
        if 0 < days_until_expiry <= 30:
            priority_queue.insert(medicine, days_until_expiry)
            soon_to_expire_medicines.append(medicine)

    # Display a notification if a medicine is added to the soon to expire page
    if soon_to_expire_medicines:
        show_notification()

    # Create a label to display the soon to expire medicines
    heading_label = tk.Label(
        soon_to_expire_window,
        text="Soon to Expire Medicines",
        font=("Arial", 14),
        bg="lightblue",
    )
    heading_label.pack(pady=10)

    # Create a frame to hold the treeview and scrollbar
    tree_frame = ttk.Frame(soon_to_expire_window)
    tree_frame.pack(fill="both", expand=True)

    # Create a treeview to display the soon to expire medicines
    tree = ttk.Treeview(tree_frame)
    tree["columns"] = (
        "Medicine ID",
        "Medicine Name",
        "Quantity",
        "Price",
        "Expiry Date",
        "Action",
    )

    # Define column headings
    tree.heading("Medicine ID", text="Medicine ID")
    tree.heading("Medicine Name", text="Medicine Name")
    tree.heading("Quantity", text="Quantity")
    tree.heading("Price", text="Price")
    tree.heading("Expiry Date", text="Expiry Date")
    tree.heading("Action", text="Action")

    # Create a vertical scrollbar
    scrollbar = Scrollbar(tree_frame, orient="vertical", command=tree.yview)

    # Configure the 'tree' widget to use the scrollbar
    tree.configure(yscrollcommand=scrollbar.set)

    # Place the 'tree' widget and scrollbar in the frame
    tree.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    # Insert soon to expire medicines data into the treeview
    while not priority_queue.is_empty():
        medicine = priority_queue.remove()
        tree.insert(
            "",
            "end",
            values=(
                medicine["Medicine ID"],
                medicine["Medicine Name"],
                medicine["Quantity"],
                medicine["Price"],
                medicine["Expiry Date"],
                "Delete",
            ),
        )

    # Create a delete button
    delete_button = Button(
        soon_to_expire_window,
        text="Delete",
        command=delete_medicine,
        font=("Arial", 12),
    )
    delete_button.pack(pady=10)

    # Create a back button
    back_button = tk.Button(
        soon_to_expire_window,
        text="Back",
        command=soon_to_expire_window.destroy,
        font=("Arial", 12),
    )
    back_button.pack(pady=10)

    # Run the soon to expire page event loop
    soon_to_expire_window.mainloop()


def expired_medicines_page():
    def show_notification():
        messagebox.showinfo(
            "Notification", "A medicine has been added to the Expired Medicines page."
        )

    def delete_medicine():
        selected_item = tree.selection()
        if selected_item:
            tree.delete(selected_item)
            messagebox.showinfo("Notification", "Medicine deleted successfully.")
        else:
            messagebox.showwarning("Warning", "Please select a medicine to delete.")

    # Create the expired medicines page window
    expired_medicines_window = tk.Toplevel()
    expired_medicines_window.title("Expired Medicines")

    # Open the window in full-screen mode
    expired_medicines_window.attributes("-fullscreen", True)

    # Set the background color
    expired_medicines_window.configure(bg="lightblue")

    # Read the medicines list from CSV
    with open("medicines_list.csv", "r") as file:
        reader = csv.DictReader(file)
        medicines = list(reader)

    # Check if there are any expired medicines
    expired_medicines = []
    current_date = datetime.now()

    # Create a priority queue for expired medicines
    priority_queue = PriorityQueue()

    for medicine in medicines:
        expiry_date = datetime.strptime(medicine["Expiry Date"], "%Y-%m-%d")
        if expiry_date < current_date:
            priority_queue.insert(medicine, expiry_date)
            expired_medicines.append(medicine)

    # Display a notification if a medicine is added to the expired medicines page
    if expired_medicines:
        show_notification()

    # Create a label to display the expired medicines
    heading_label = tk.Label(
        expired_medicines_window,
        text="Expired Medicines",
        font=("Arial", 14),
        bg="lightblue",
    )
    heading_label.pack(pady=10)

    # Create a frame to hold the treeview and scrollbar
    tree_frame = ttk.Frame(expired_medicines_window)
    tree_frame.pack(fill="both", expand=True)

    # Create a treeview to display the expired medicines
    tree = ttk.Treeview(tree_frame)
    tree["columns"] = (
        "Medicine ID",
        "Medicine Name",
        "Quantity",
        "Price",
        "Expiry Date",
        "Action",
    )

    # Define column headings
    tree.heading("Medicine ID", text="Medicine ID")
    tree.heading("Medicine Name", text="Medicine Name")
    tree.heading("Quantity", text="Quantity")
    tree.heading("Price", text="Price")
    tree.heading("Expiry Date", text="Expiry Date")
    tree.heading("Action", text="Action")

    # Create a vertical scrollbar
    scrollbar = Scrollbar(tree_frame, orient="vertical", command=tree.yview)

    # Configure the 'tree' widget to use the scrollbar
    tree.configure(yscrollcommand=scrollbar.set)

    # Place the 'tree' widget and scrollbar in the frame
    tree.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    # Insert expired medicines data into the treeview
    while not priority_queue.is_empty():
        medicine = priority_queue.remove()
        tree.insert(
            "",
            "end",
            values=(
                medicine["Medicine ID"],
                medicine["Medicine Name"],
                medicine["Quantity"],
                medicine["Price"],
                medicine["Expiry Date"],
                "Delete",
            ),
        )

    # Create a delete button
    delete_button = Button(
        expired_medicines_window,
        text="Delete",
        command=delete_medicine,
        font=("Arial", 12),
    )
    delete_button.pack(pady=10)

    # Create a back button
    back_button = tk.Button(
        expired_medicines_window,
        text="Back",
        command=expired_medicines_window.destroy,
        font=("Arial", 12),
    )
    back_button.pack(pady=10)

    # Run the expired medicines page event loop
    expired_medicines_window.mainloop()


def day_sales_page():
    def calculate_day_sales():
        # Load the sales data from the CSV file
        sales_data = load_sales_data()
        medicine_info = load_medicine_info()

        # Calculate the total sales for each day
        day_sales = {}
        for sale in sales_data:
            sale_date = sale["sale_date"]
            medicine_id = sale[" medicine_id"]
            quantity = int(sale[" quantity"])
            price = float(sale["price"])

            sale_amount = quantity * price

            if sale_date in day_sales:
                day_sales[sale_date]["total_sales"] += sale_amount
            else:
                day_sales[sale_date] = {"total_sales": sale_amount, "medicines": {}}

            if medicine_id in day_sales[sale_date]["medicines"]:
                day_sales[sale_date]["medicines"][medicine_id]["quantity"] += quantity
            else:
                medicine_name = medicine_info[medicine_id]["Medicine Name"]
                medicine_price = price
                day_sales[sale_date]["medicines"][medicine_id] = {
                    "medicine_name": medicine_name,
                    "quantity": quantity,
                    "price": medicine_price,
                }

        # Display the day-wise sales report
        display_sales_report(day_sales)

    def load_sales_data():
        sales_data = []
        with open("sales_tracking.csv", "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                sales_data.append(row)
        return sales_data

    def load_medicine_info():
        medicine_info = {}
        with open("medicines_list.csv", "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                medicine_id = row["Medicine ID"]
                medicine_info[medicine_id] = row
        return medicine_info

    def display_sales_report(day_sales):
        # Create a new window for the day sales report
        report_window = tk.Toplevel()
        report_window.title("Daily Sales Report")

        # Create a frame to hold the report content
        frame = tk.Frame(report_window, padx=20, pady=20)
        frame.pack()

        # Create the heading label
        heading_label = tk.Label(
            frame, text="Daily Sales Report", font=("Arial", 18, "bold")
        )
        heading_label.pack(pady=10)

        # Create a table-like display for the day-wise sales report
        for date, sales in day_sales.items():
            date_label = tk.Label(frame, text=date, font=("Arial", 12, "bold"))
            date_label.pack(anchor="w")

            total_sales_label = tk.Label(
                frame,
                text=f"Total Sales: ₹{sales['total_sales']:.2f}",
                font=("Arial", 12),
            )
            total_sales_label.pack(anchor="w")

            medicines_label = tk.Label(
                frame, text="Medicine Info:", font=("Arial", 12, "bold")
            )
            medicines_label.pack(anchor="w")

            for medicine_id, medicine_data in sales["medicines"].items():
                medicine_name = medicine_data["medicine_name"]
                quantity = medicine_data["quantity"]
                price = medicine_data["price"]
                medicine_info_label = tk.Label(
                    frame,
                    text=f"Medicine ID: {medicine_id}, Medicine Name: {medicine_name}, Quantity: {quantity}, Price: ₹{price:.2f}",
                    font=("Arial", 12),
                )
                medicine_info_label.pack(anchor="w")

            separator = tk.Frame(frame, height=1, bg="gray", pady=5)
            separator.pack(fill="x")

        # Create a button to show the sales graph
        show_graph_button = tk.Button(
            frame,
            text="Show Graph",
            command=lambda: show_sales_graph(day_sales),
            font=("Arial", 12),
            width=20,
        )
        show_graph_button.pack(pady=5)

    def show_sales_graph(day_sales):
        # Extract the dates and total sales from day_sales
        dates = list(day_sales.keys())
        total_sales = [sales["total_sales"] for sales in day_sales.values()]

        # Create a new window for the sales graph
        graph_window = tk.Toplevel()
        graph_window.title("Daily Sales Graph")

        # Create a Figure object
        fig = Figure(figsize=(6, 4), dpi=100)

        # Add a subplot to the Figure
        ax = fig.add_subplot(111)

        # Plot the sales data
        ax.plot(dates, total_sales, marker="o")

        # Set labels and title
        ax.set_xlabel("Date")
        ax.set_ylabel("Total Sales")
        ax.set_title("Daily Sales")

        # Create a Tkinter canvas
        canvas = FigureCanvasTkAgg(fig, master=graph_window)
        canvas.draw()

        # Add the canvas to the Tkinter window
        canvas.get_tk_widget().pack()

    # Create the day sales page window
    day_sales_window = tk.Tk()
    day_sales_window.title("Daily Sales Page")

    # Open the window in full-screen mode
    day_sales_window.attributes("-fullscreen", True)

    # Set the background color
    day_sales_window.configure(bg="lightblue")

    # Create a frame to hold the day sales page content
    frame = tk.Frame(day_sales_window, padx=20, pady=20, bg="lightblue")
    frame.pack(expand=True)

    # Create the heading label
    heading_label = tk.Label(
        frame,
        text="Daily Sales Page",
        font=("Arial", 18, "bold"),
        bg="lightblue",
        fg="blue",
    )
    heading_label.pack(pady=10)

    # Create a button to calculate and display the day sales report
    calculate_button = tk.Button(
        frame,
        text="Calculate Daily Sales",
        command=calculate_day_sales,
        font=("Arial", 12),
        width=20,
    )
    calculate_button.pack(pady=5)

    # Create a "Back" button to return to the home page
    back_button = tk.Button(
        frame,
        text="Back",
        command=day_sales_window.destroy,
        font=("Arial", 12),
        width=20,
    )
    back_button.pack(pady=5)

    # Run the day sales page event loop
    day_sales_window.mainloop()


def monthly_sales_page():
    def calculate_monthly_sales():
        # Load the sales data from the CSV file
        sales_data = load_sales_data()
        medicine_info = load_medicine_info()

        # Calculate the total sales for each month
        monthly_sales = {}
        for sale in sales_data:
            sale_date = sale["sale_date"]
            month = sale_date.split("-")[1]
            medicine_id = sale[" medicine_id"]
            quantity = int(sale[" quantity"])
            price = float(sale["price"])

            sale_amount = quantity * price

            if month in monthly_sales:
                monthly_sales[month]["total_sales"] += sale_amount
            else:
                monthly_sales[month] = {"total_sales": sale_amount, "medicines": {}}

            if medicine_id in monthly_sales[month]["medicines"]:
                monthly_sales[month]["medicines"][medicine_id]["quantity"] += quantity
            else:
                medicine_name = medicine_info[medicine_id]["Medicine Name"]
                medicine_price = price
                monthly_sales[month]["medicines"][medicine_id] = {
                    "medicine_name": medicine_name,
                    "quantity": quantity,
                    "price": medicine_price,
                }

        # Display the monthly sales report
        display_sales_report(monthly_sales)

    def load_sales_data():
        sales_data = []
        with open("sales_tracking.csv", "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                sales_data.append(row)
        return sales_data

    def load_medicine_info():
        medicine_info = {}
        with open("medicines_list.csv", "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                medicine_id = row["Medicine ID"]
                medicine_info[medicine_id] = row
        return medicine_info

    def display_sales_report(monthly_sales):
        # Create a new window for the monthly sales report
        report_window = tk.Toplevel()
        report_window.title("Monthly Sales Report")

        # Create a frame to hold the report content
        frame = tk.Frame(report_window, padx=20, pady=20)
        frame.pack()

        # Create the heading label
        heading_label = tk.Label(
            frame, text="Monthly Sales Report", font=("Arial", 18, "bold")
        )
        heading_label.pack(pady=10)

        # Create a table-like display for the monthly sales report
        for month, sales in monthly_sales.items():
            month_label = tk.Label(
                frame, text=f"Month: {month}", font=("Arial", 12, "bold")
            )
            month_label.pack(anchor="w")

            total_sales_label = tk.Label(
                frame,
                text=f"Total Sales: ₹{sales['total_sales']:.2f}",
                font=("Arial", 12),
            )
            total_sales_label.pack(anchor="w")

            medicines_label = tk.Label(
                frame, text="Medicine Info:", font=("Arial", 12, "bold")
            )
            medicines_label.pack(anchor="w")

            for medicine_id, medicine_data in sales["medicines"].items():
                medicine_name = medicine_data["medicine_name"]
                quantity = medicine_data["quantity"]
                price = medicine_data["price"]
                medicine_info_label = tk.Label(
                    frame,
                    text=f"Medicine ID: {medicine_id}, Medicine Name: {medicine_name}, Quantity: {quantity}, Price: ₹{price:.2f}",
                    font=("Arial", 12),
                )
                medicine_info_label.pack(anchor="w")

            separator = tk.Frame(frame, height=1, bg="gray", pady=5)
            separator.pack(fill="x")

        # Create a button to show the sales graph
        show_graph_button = tk.Button(
            frame,
            text="Show Graph",
            command=lambda: show_sales_graph(monthly_sales),
            font=("Arial", 12),
            width=20,
        )
        show_graph_button.pack(pady=5)

    def show_sales_graph(monthly_sales):
        # Extract the months and total sales from monthly_sales
        months = list(monthly_sales.keys())
        total_sales = [sales["total_sales"] for sales in monthly_sales.values()]

        # Create a new window for the sales graph
        graph_window = tk.Toplevel()
        graph_window.title("Monthly Sales Graph")

        # Create a Figure object
        fig = Figure(figsize=(6, 4), dpi=100)

        # Add a subplot to the Figure
        ax = fig.add_subplot(111)

        # Plot the sales data
        ax.plot(months, total_sales, marker="o")

        # Set labels and title
        ax.set_xlabel("Month")
        ax.set_ylabel("Total Sales")
        ax.set_title("Monthly Sales")

        # Create a Tkinter canvas
        canvas = FigureCanvasTkAgg(fig, master=graph_window)
        canvas.draw()

        # Add the canvas to the Tkinter window
        canvas.get_tk_widget().pack()

    # Create the monthly sales page window
    monthly_sales_window = tk.Tk()
    monthly_sales_window.title("Monthly Sales Page")

    # Open the window in full-screen mode
    monthly_sales_window.attributes("-fullscreen", True)

    # Set the background color
    monthly_sales_window.configure(bg="lightblue")

    # Create a frame to hold the monthly sales page content
    frame = tk.Frame(monthly_sales_window, padx=20, pady=20, bg="lightblue")
    frame.pack(expand=True)

    # Create the heading label
    heading_label = tk.Label(
        frame,
        text="Monthly Sales Page",
        font=("Arial", 18, "bold"),
        bg="lightblue",
        fg="blue",
    )
    heading_label.pack(pady=10)

    # Create a button to calculate and display the monthly sales report
    calculate_button = tk.Button(
        frame,
        text="Calculate Monthly Sales",
        command=calculate_monthly_sales,
        font=("Arial", 12),
        width=20,
    )
    calculate_button.pack(pady=5)

    # Create a "Back" button to return to the home page
    back_button = tk.Button(
        frame,
        text="Back",
        command=monthly_sales_window.destroy,
        font=("Arial", 12),
        width=20,
    )
    back_button.pack(pady=5)

    # Run the monthly sales page event loop
    monthly_sales_window.mainloop()


def yearly_sales_page():
    def calculate_yearly_sales():
        # Load the sales data from the CSV file
        sales_data = load_sales_data()
        medicine_info = load_medicine_info()

        # Calculate the total sales for each year
        yearly_sales = {}
        for sale in sales_data:
            sale_date = sale["sale_date"]
            year = sale_date.split("-")[0]
            medicine_id = sale[" medicine_id"]
            quantity = int(sale[" quantity"])
            price = float(sale["price"])

            sale_amount = quantity * price

            if year in yearly_sales:
                yearly_sales[year]["total_sales"] += sale_amount
            else:
                yearly_sales[year] = {"total_sales": sale_amount, "medicines": {}}

            if medicine_id in yearly_sales[year]["medicines"]:
                yearly_sales[year]["medicines"][medicine_id]["quantity"] += quantity
            else:
                medicine_name = medicine_info[medicine_id]["Medicine Name"]
                medicine_price = price
                yearly_sales[year]["medicines"][medicine_id] = {
                    "medicine_name": medicine_name,
                    "quantity": quantity,
                    "price": medicine_price,
                }

        # Display the yearly sales report
        display_sales_report(yearly_sales)

    def load_sales_data():
        sales_data = []
        with open("sales_tracking.csv", "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                sales_data.append(row)
        return sales_data

    def load_medicine_info():
        medicine_info = {}
        with open("medicines_list.csv", "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                medicine_id = row["Medicine ID"]
                medicine_info[medicine_id] = row
        return medicine_info

    def display_sales_report(yearly_sales):
        # Create a new window for the yearly sales report
        report_window = tk.Toplevel()
        report_window.title("Yearly Sales Report")

        # Create a frame to hold the report content
        frame = tk.Frame(report_window, padx=20, pady=20)
        frame.pack()

        # Create the heading label
        heading_label = tk.Label(
            frame, text="Yearly Sales Report", font=("Arial", 18, "bold")
        )
        heading_label.pack(pady=10)

        # Create a table-like display for the yearly sales report
        for year, sales in yearly_sales.items():
            year_label = tk.Label(
                frame, text=f"Year: {year}", font=("Arial", 12, "bold")
            )
            year_label.pack(anchor="w")

            total_sales_label = tk.Label(
                frame,
                text=f"Total Sales: ₹{sales['total_sales']:.2f}",
                font=("Arial", 12),
            )
            total_sales_label.pack(anchor="w")

            medicines_label = tk.Label(
                frame, text="Medicine Info:", font=("Arial", 12, "bold")
            )
            medicines_label.pack(anchor="w")

            for medicine_id, medicine_data in sales["medicines"].items():
                medicine_name = medicine_data["medicine_name"]
                quantity = medicine_data["quantity"]
                price = medicine_data["price"]
                medicine_info_label = tk.Label(
                    frame,
                    text=f"Medicine ID: {medicine_id}, Medicine Name: {medicine_name}, Quantity: {quantity}, Price: ₹{price:.2f}",
                    font=("Arial", 12),
                )
                medicine_info_label.pack(anchor="w")

            separator = tk.Frame(frame, height=1, bg="gray", pady=5)
            separator.pack(fill="x")

        # Create a button to show the sales graph
        show_graph_button = tk.Button(
            frame,
            text="Show Graph",
            command=lambda: show_sales_graph(yearly_sales),
            font=("Arial", 12),
            width=20,
        )
        show_graph_button.pack(pady=5)

    def show_sales_graph(yearly_sales):
        # Extract the years and total sales from yearly_sales
        years = list(yearly_sales.keys())
        total_sales = [sales["total_sales"] for sales in yearly_sales.values()]

        # Create a new window for the sales graph
        graph_window = tk.Toplevel()
        graph_window.title("Yearly Sales Graph")

        # Create a Figure object
        fig = Figure(figsize=(6, 4), dpi=100)

        # Add a subplot to the Figure
        ax = fig.add_subplot(111)

        # Plot the sales data
        ax.bar(years, total_sales)

        # Set labels and title
        ax.set_xlabel("Year")
        ax.set_ylabel("Total Sales")
        ax.set_title("Yearly Sales")

        # Create a Tkinter canvas
        canvas = FigureCanvasTkAgg(fig, master=graph_window)
        canvas.draw()

        # Add the canvas to the Tkinter window
        canvas.get_tk_widget().pack()

    # Create the yearly sales page window
    yearly_sales_window = tk.Tk()
    yearly_sales_window.title("Yearly Sales Page")

    # Open the window in full-screen mode
    yearly_sales_window.attributes("-fullscreen", True)

    # Set the background color
    yearly_sales_window.configure(bg="lightblue")

    # Create a frame to hold the yearly sales page content
    frame = tk.Frame(yearly_sales_window, padx=20, pady=20, bg="lightblue")
    frame.pack(expand=True)

    # Create the heading label
    heading_label = tk.Label(
        frame,
        text="Yearly Sales Page",
        font=("Arial", 18, "bold"),
        bg="lightblue",
        fg="blue",
    )
    heading_label.pack(pady=10)

    # Create a button to calculate and display the yearly sales report
    calculate_button = tk.Button(
        frame,
        text="Calculate Yearly Sales",
        command=calculate_yearly_sales,
        font=("Arial", 12),
        width=20,
    )
    calculate_button.pack(pady=5)

    # Create a "Back" button to return to the home page
    back_button = tk.Button(
        frame,
        text="Back",
        command=yearly_sales_window.destroy,
        font=("Arial", 12),
        width=20,
    )
    back_button.pack(pady=5)

    # Run the yearly sales page event loop
    yearly_sales_window.mainloop()


# Create the login page
create_login_page()
