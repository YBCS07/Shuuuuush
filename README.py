# Shuuuuush

import tkinter as tk
from tkinter import messagebox, ttk
import json  # For saving and loading favorite foods

# User class to handle user data
class User:
    def __init__(self, full_name, username, password):
        self.full_name = full_name
        self.username = username
        self.password = password

# Function to save user data to a text file
def save_user(user):
    with open("users.txt", "a") as file:
        file.write(f"{user.username},{user.password}\n")

def is_valid_username(username):
    return 3 <= len(username) <= 20

def is_valid_password(password):
    return 8 <= len(password) <= 20

# Class for the main application
class MainApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("User Login and Registration")

        self.tab_control = ttk.Notebook(self.root)
        self.login_tab = ttk.Frame(self.tab_control)
        self.registration_tab = ttk.Frame(self.tab_control)

        self.tab_control.add(self.login_tab, text="Login")
        self.tab_control.add(self.registration_tab, text="User Registration")
        self.tab_control.pack(expand=1, fill="both")

        self.create_login_tab()
        self.create_registration_tab()

        self.root.mainloop()

    def create_login_tab(self):
        tk.Label(self.login_tab, text="Username:").grid(row=0, column=0)
        self.username_entry = tk.Entry(self.login_tab)
        self.username_entry.grid(row=0, column=1)

        tk.Label(self.login_tab, text="Password:").grid(row=1, column=0)
        self.password_entry = tk.Entry(self.login_tab, show="*")
        self.password_entry.grid(row=1, column=1)

        tk.Button(self.login_tab, text="Login", command=self.login).grid(row=2, column=1)

    def create_registration_tab(self):
        tk.Label(self.registration_tab, text="First Name:").grid(row=0, column=0)
        self.first_name_entry = tk.Entry(self.registration_tab)
        self.first_name_entry.grid(row=0, column=1)

        tk.Label(self.registration_tab, text="Last Name:").grid(row=1, column=0)
        self.last_name_entry = tk.Entry(self.registration_tab)
        self.last_name_entry.grid(row=1, column=1)

        tk.Label(self.registration_tab, text="Username:").grid(row=2, column=0)
        self.username_reg_entry = tk.Entry(self.registration_tab)
        self.username_reg_entry.grid(row=2, column=1)

        tk.Label(self.registration_tab, text="Password:").grid(row=3, column=0)
        self.password_reg_entry = tk.Entry(self.registration_tab, show="*")
        self.password_reg_entry.grid(row=3, column=1)

        tk.Button(self.registration_tab, text="Submit", command=self.submit_registration).grid(row=4, column=1)

    def submit_registration(self):
        first_name = self.first_name_entry.get()
        last_name = self.last_name_entry.get()
        username = self.username_reg_entry.get()
        password = self.password_reg_entry.get()

        if not is_valid_username(username):
            messagebox.showerror("Error", "Username must be 3-20 characters.")
            return
        if not is_valid_password(password):
            messagebox.showerror("Error", "Password must be 8-20 characters.")
            return

        full_name = f"{first_name} {last_name}"
        user = User(full_name, username, password)
        save_user(user)
        messagebox.showinfo("Success", "User registered successfully!")

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        try:
            with open("users.txt", "r") as file:
                users = {line.split(",")[0]: line.split(",")[1].strip() for line in file}
            if username in users and users[username] == password:
                messagebox.showinfo("Login Successful", "Welcome!")
                self.tab_control.destroy()
                self.show_main_app()
            else:
                messagebox.showerror("Error", "Invalid username or password.")
        except FileNotFoundError:
            messagebox.showerror("Error", "User data file not found.")

    def show_main_app(self):
        self.main_window = tk.Tk()
        self.main_window.title("Main Application")

        self.tab_control = ttk.Notebook(self.main_window)
        self.calorie_calculator_tab = ttk.Frame(self.tab_control)
        self.food_log_tab = ttk.Frame(self.tab_control)

        self.tab_control.add(self.calorie_calculator_tab, text="Calorie Calculator")
        self.tab_control.add(self.food_log_tab, text="Food Log")
        self.tab_control.pack(expand=1, fill="both")

        CalorieCalculatorGUI(self.calorie_calculator_tab)
        FoodLogGUI(self.food_log_tab)

        self.main_window.mainloop()

# Class for the calorie calculator GUI
class CalorieCalculatorGUI:
    def __init__(self, parent):
        self.calculator_window = parent
        self.create_gui()

    def create_gui(self):
        tk.Label(self.calculator_window, text="Age:").grid(row=0, column=0)
        self.age_entry = tk.Entry(self.calculator_window)
        self.age_entry.grid(row=0, column=1)

        tk.Label(self.calculator_window, text="Weight (kg):").grid(row=1, column=0)
        self.weight_entry = tk.Entry(self.calculator_window)
        self.weight_entry.grid(row=1, column=1)

        tk.Label(self.calculator_window, text="Height (cm):").grid(row=2, column=0)
        self.height_entry = tk.Entry(self.calculator_window)
        self.height_entry.grid(row=2, column=1)

        tk.Label(self.calculator_window, text="Gender:").grid(row=3, column=0)
        self.gender_var = tk.StringVar(value="male")
        tk.Radiobutton(self.calculator_window, text="Male", variable=self.gender_var, value="male").grid(row=3, column=1)
        tk.Radiobutton(self.calculator_window, text="Female", variable=self.gender_var, value="female").grid(row=3, column=2)

        tk.Label(self.calculator_window, text="Activity Level:").grid(row=4, column=0)
        self.activity_var = tk.StringVar(value="none")
        tk.OptionMenu(self.calculator_window, self.activity_var, "none", "little", "moderate", "heavy").grid(row=4, column=1)

        tk.Label(self.calculator_window, text="Goal:").grid(row=5, column=0)
        self.goal_var = tk.StringVar(value="maintain")
        tk.OptionMenu(self.calculator_window, self.goal_var, "maintain", "lose", "gain").grid(row=5, column=1)

        tk.Label(self.calculator_window, text="Intensity:").grid(row=6, column=0)
        self.intensity_var = tk.StringVar(value="low")
        tk.OptionMenu(self.calculator_window, self.intensity_var, "low", "medium", "high").grid(row=6, column=1)

        tk.Button(self.calculator_window, text="Calculate", command=self.calculate_calories).grid(row=7, column=1)

        self.result_label = tk.Label(self.calculator_window, text="Your daily caloric needs will be displayed here.")
        self.result_label.grid(row=8, column=0, columnspan=2)

    def calculate_calories(self):
        try:
            age = int(self.age_entry.get())
            weight = int(self.weight_entry.get())
            height = int(self.height_entry.get())
            gender = self.gender_var.get()
            activity_level = self.activity_var.get()
            goal = self.goal_var.get()
            intensity = self.intensity_var.get()

            if gender == 'male':
                bmr = 66 + (6.23 * weight) + (12.7 * height) - (6.8 * age)
            else:
                bmr = 655 + (4.35 * weight) + (4.7 * height) - (4.7 * age)

            activity_factors = {'none': 1.2, 'little': 1.375, 'moderate': 1.55, 'heavy': 1.725}
            calories = bmr * activity_factors[activity_level]

            if goal == 'maintain':
                pass
            elif goal == 'lose':
                calories -= 500
            elif goal == 'gain':
                calories += 500

            if intensity == 'medium':
                calories += 250
            elif intensity == 'high':
                calories += 500

            self.result_label.config(text=f"Your daily caloric needs are: {calories:.2f} calories.")
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter valid numbers for age, weight, and height.")

# Class for the food log GUI
class FoodLogGUI:
    def __init__(self, parent):
        self.food_log_window = parent
        self.create_gui()

    def create_gui(self):
        tk.Label(self.food_log_window, text="Daily Calorie Goal:").grid(row=0, column=0)
        self.calorie_goal_entry = tk.Entry(self.food_log_window)
        self.calorie_goal_entry.grid(row=0, column=1)

        tk.Button(self.food_log_window, text="Set Goal", command=self.set_goal).grid(row=0, column=2)

        self.food_entries = []
        self.favorite_foods = {}
        self.daily_calories = 0

        tk.Label(self.food_log_window, text="Food Name:").grid(row=1, column=0)
        self.food_entry = tk.Entry(self.food_log_window)
        self.food_entry.grid(row=1, column=1)

        tk.Label(self.food_log_window, text="Calories:").grid(row=2, column=0)
        self.calories_entry = tk.Entry(self.food_log_window)
        self.calories_entry.grid(row=2, column=1)

        tk.Label(self.food_log_window, text="Grams:").grid(row=3, column=0)
        self.grams_entry = tk.Entry(self.food_log_window)
        self.grams_entry.grid(row=3, column=1)

        tk.Label(self.food_log_window, text="Meal Type:").grid(row=4, column=0)
        self.meal_var = tk.StringVar(value="breakfast")
        tk.OptionMenu(self.food_log_window, self.meal_var, "breakfast", "lunch", "dinner", "snack").grid(row=4, column=1)

        tk.Button(self.food_log_window, text="Add Item", command=self.add_item).grid(row=5, column=1)
        tk.Button(self.food_log_window, text="Delete Item", command=self.delete_item).grid(row=6, column=1)

        self.food_listbox = tk.Listbox(self.food_log_window, width=50)
        self.food_listbox.grid(row=7, column=0, columnspan=2)

        self.calories_label = tk.Label(self.food_log_window, text=f"Remaining Daily Calories: {self.daily_calories:.2f}")
        self.calories_label.grid(row=8, column=0, columnspan=2)

        tk.Label(self.food_log_window, text="Favorite Food:").grid(row=9, column=0)
        self.favorite_food_var = tk.StringVar(self.food_log_window)
        self.update_favorite_foods_dropdown()

        tk.Button(self.food_log_window, text="Add Favorite", command=self.add_favorite_food_to_library).grid(row=10, column=0)
        tk.Button(self.food_log_window, text="Add to Log from Favorite", command=self.add_from_favorite).grid(row=10, column=1)

    def set_goal(self):
        try:
            self.daily_calories = int(self.calorie_goal_entry.get())
            if self.daily_calories <= 0:
                raise ValueError
            self.calories_label.config(text=f"Remaining Daily Calories: {self.daily_calories:.2f}")
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid positive number for calorie goal.")

    def add_item(self):
        food_name = self.food_entry.get()
        try:
            calories = int(self.calories_entry.get())
            grams = int(self.grams_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers for calories and grams.")
            return

        meal_type = self.meal_var.get()
        self.food_entries.append((food_name, calories, grams, meal_type))
        self.daily_calories -= calories
        self.food_listbox.insert(tk.END, f"{meal_type}: {food_name} - {calories} kcal, {grams}g")
        self.update_calories_label()

    def delete_item(self):
        selected_index = self.food_listbox.curselection()
        if selected_index:
            deleted_entry = self.food_entries.pop(selected_index[0])
            self.daily_calories += deleted_entry[1]
            self.food_listbox.delete(selected_index)
            self.update_calories_label()

    def update_calories_label(self):
        self.calories_label.config(text=f"Remaining Daily Calories: {self.daily_calories:.2f}")

    def update_favorite_foods_dropdown(self):
        if hasattr(self, 'favorite_food_menu'):
            self.favorite_food_menu.destroy()

        favorite_foods = list(self.favorite_foods.keys())
        if favorite_foods:
            self.favorite_food_var.set(favorite_foods[0])
            self.favorite_food_menu = tk.OptionMenu(self.food_log_window, self.favorite_food_var, *favorite_foods)
        else:
            self.favorite_food_var.set("")
            self.favorite_food_menu = tk.OptionMenu(self.food_log_window, self.favorite_food_var, "")

        self.favorite_food_menu.grid(row=9, column=1)

    def add_favorite_food_to_library(self):
        food_name = self.food_entry.get()
        try:
            calories_per_100g = int(self.calories_entry.get())
            self.favorite_foods[food_name] = calories_per_100g
            self.update_favorite_foods_dropdown()
            messagebox.showinfo("Success", f"{food_name} added to favorite foods.")
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers for calories per 100g.")

    def add_from_favorite(self):
        food_name = self.favorite_food_var.get()
        if food_name:
            try:
                grams = int(self.grams_entry.get())
                calories_per_100g = self.favorite_foods[food_name]
                calories = (calories_per_100g * grams) / 100

                self.food_entries.append((food_name, calories, grams, "favorite"))
                self.food_listbox.insert(tk.END, f"favorite: {food_name} - {calories:.2f} kcal, {grams}g")
                self.daily_calories -= calories
                self.update_calories_label()

                messagebox.showinfo("Calories Calculated", f"{food_name} ({grams}g) adds {calories:.2f} calories.")
            except ValueError:
                messagebox.showerror("Error", "Please enter a valid number of grams.")
        else:
            messagebox.showerror("Error", "No favorite food selected.")

if __name__ == "__main__":
    MainApp()
