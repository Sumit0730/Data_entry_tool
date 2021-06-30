# print("lets get start!!!!!!!!!!!!!!!!!")
# str = "hello world"
# print(str[0:8:2])
# tp=(1,2,3)
# print(type(tp))
# tpp=tuple((4,5,6))
# print(type(tpp))
# print(len(tpp))
# tup=("Apple")
# print(type(tup))
# tupp=("Apple",)
# print(type(tupp))
# l1=[1,4,5,8,6,7,9]
# l1.reverse()
# l1.sort()
# print(l1)
# l1.append(10)
# l1.insert(4,12)
# print(l1)
import tkinter as tk
# from tkinter import ttk
# from tkinter.messagebox import showinfo
#
# root = tk.Tk()
# root.geometry('300x200')
# root.resizable(False, False)
# root.title('Combobox Widget')
#
#
# def month_changed(event):
#     msg = f'You selected {month_cb.get()}!'
#     showinfo(title='Result', message=msg)
#
#
# # month of year
# months = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
#         'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')
#
# label = ttk.Label(text="Please select a month:")
# label.pack(fill='x', padx=5, pady=5)
#
# # create a combobox
# selected_month = tk.StringVar()
#
# month_cb = ttk.Combobox(root, textvariable=selected_month)
# month_cb['values'] = months
# month_cb['state'] = 'readonly'  # normal
# month_cb.pack(fill='x', padx=5, pady=5)
#
# month_cb.bind('<<ComboboxSelected>>', month_changed)
#
# root.mainloop()

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror


class TemperatureConverter:
    @staticmethod
    def fahrenheit_to_celsius(f, format=True):
        result = (f - 32) * 5/9
        if format:
            return f'{f} Fahrenheit = {result:.2f} Celsius'
        return result

    @staticmethod
    def celsius_to_fahrenheit(c, format=True):
        result = c * 9/5 + 32
        if format:
            return f'{c} Celsius = {result:.2f} Fahrenheit'
        return result


class ConverterFrame(ttk.Frame):
    def __init__(self, container, unit_from, converter):
        super().__init__(container)

        self.unit_from = unit_from
        self.converter = converter

        # field options
        options = {'padx': 5, 'pady': 0}

        # temperature label
        self.temperature_label = ttk.Label(self, text=self.unit_from)
        self.temperature_label.grid(column=0, row=0, sticky='w',  **options)

        # temperature entry
        self.temperature = tk.StringVar()
        self.temperature_entry = ttk.Entry(self, textvariable=self.temperature)
        self.temperature_entry.grid(column=1, row=0, sticky='w', **options)
        self.temperature_entry.focus()

        # button
        self.convert_button = ttk.Button(self, text='Convert')
        self.convert_button.grid(column=2, row=0, sticky='w', **options)
        self.convert_button.configure(command=self.convert)

        # result label
        self.result_label = ttk.Label(self)
        self.result_label.grid(row=1, columnspan=3, **options)

        # add padding to the frame and show it
        self.grid(column=0, row=0, padx=5, pady=5, sticky="nsew")

    def convert(self, event=None):
        """  Handle button click event
        """
        try:
            input_value = float(self.temperature.get())
            result = self.converter(input_value)
            self.result_label.config(text=result)
        except ValueError as error:
            showerror(title='Error', message=error)

    def reset(self):
        self.temperature_entry.delete(0, "end")
        self.result_label.text = ''


class ControlFrame(ttk.LabelFrame):
    def __init__(self, container):

        super().__init__(container)
        self['text'] = 'Options'

        # radio buttons
        self.selected_value = tk.IntVar()

        ttk.Radiobutton(
            self,
            text='F to C',
            value=0,
            variable=self.selected_value,
            command=self.change_frame).grid(column=0, row=0, padx=5, pady=5)

        ttk.Radiobutton(
            self,
            text='C to F',
            value=1,
            variable=self.selected_value,
            command=self.change_frame).grid(column=1, row=0, padx=5, pady=5)

        self.grid(column=0, row=1, padx=5, pady=5, sticky='ew')

        # initialize frames
        self.frames = {}
        self.frames[0] = ConverterFrame(
            container,
            'Fahrenheit',
            TemperatureConverter.fahrenheit_to_celsius)
        self.frames[1] = ConverterFrame(
            container,
            'Celsius',
            TemperatureConverter.celsius_to_fahrenheit)

        self.change_frame()

    def change_frame(self):
        frame = self.frames[self.selected_value.get()]
        frame.reset()
        frame.tkraise()


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Temperature Converter')
        self.geometry('300x120')
        self.resizable(False, False)
if __name__ == "__main__":
    app = App()
    ControlFrame(app)
    app.mainloop()