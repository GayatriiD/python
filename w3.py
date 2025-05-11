import tkinter as tk

class SimpleCalculator:
    def __init__(self, master):
        self.master = master
        master.title("Simple Calculator")

        self.result_var = tk.StringVar()

        # Entry field for displaying the result
        self.result_entry = tk.Entry(master, textvariable=self.result_var, font=('Arial', 24), bd=10, insertwidth=2, width=14, borderwidth=4)
        self.result_entry.grid(row=0, column=0, columnspan=4)

        # Buttons for digits and operations
        self.create_buttons()

    def create_buttons(self):
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
        ]

        for (text, row, col) in buttons:
            if text == '=':
                button = tk.Button(self.master, text=text, padx=20, pady=20, command=self.calculate)
            else:
                button = tk.Button(self.master, text=text, padx=20, pady=20, command=lambda t=text: self.append_to_expression(t))
            button.grid(row=row, column=col)

        clear_button = tk.Button(self.master, text='C', padx=20, pady=20, command=self.clear)
        clear_button.grid(row=5, column=0, columnspan=4)

    def append_to_expression(self, value):
        current_text = self.result_var.get()
        new_text = current_text + str(value)
        self.result_var.set(new_text)

    def calculate(self):
        expression = self.result_var.get()
        try:
            # Evaluate the expression
            result = eval(expression)
            # Format the output as "expression = result"
            output = f"{expression} = {result}"
            self.result_var.set(output)
        except Exception:
            self.result_var.set("Error")

    def clear(self):
        self.result_var.set("")

if __name__ == "__main__":
    root = tk.Tk()
    calculator = SimpleCalculator(root)
    root.mainloop()