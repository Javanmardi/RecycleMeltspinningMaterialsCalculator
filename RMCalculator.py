import tkinter as tk
from tkinter import ttk
import webbrowser

class MeltSpinningCalculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Recycling Meltspinning Calculator")
        self.geometry("440x330")
        self.resizable(False, False)

        # Labels for components
        self.components = [
            "Oil (%)", "PSU (kg)", "Popcorn SPC (kg)", "SKPC (kg)",
            "Flake", "Chips (kg)", "Master batch",
            "Waste (%)", "Bunker mass (kg)"
        ]

        # Dictionaries to hold entry and result widgets
        self.entries = {}
        self.results = {}

        # Build UI
        row_index = 0
        for comp in self.components:
            if comp == "Flake":
                # --- Flake Row 1 ---
                tk.Label(self, text="Flake 1 (kg)", width=15, anchor="w").grid(row=row_index, column=0, padx=5, pady=3)

                self.flake_entry = tk.Entry(self, width=10)
                self.flake_entry.grid(row=row_index, column=1, padx=5, pady=3)

                self.flake_result1 = tk.Entry(self, width=15, state="readonly", justify="center")
                self.flake_result1.grid(row=row_index, column=2, padx=5, pady=3)

                # Mix checkbox + entry
                self.mix_var = tk.IntVar(value=0)
                mix_check = tk.Checkbutton(self, text="Mix", variable=self.mix_var, command=self.toggle_flake2)
                mix_check.grid(row=row_index, column=3, padx=5)

                self.mix_entry = tk.Entry(self, state="disabled", width=5)
                self.mix_entry.grid(row=row_index, column=4, padx=5, pady=3)

                tk.Label(self, text='%', width=5, anchor="w").grid(row=row_index, column=5, padx=5, pady=3)
                row_index += 1

                # --- Flake Row 2 ---
                tk.Label(self, text="Flake 2 (kg)", width=15, anchor="w").grid(row=row_index, column=0, padx=5, pady=3)

                self.flake2_entry = tk.Entry(self, width=10, state="disabled")
                self.flake2_entry.grid(row=row_index, column=1, padx=5, pady=3)

                self.flake_result2 = tk.Entry(self, width=15, state="readonly", justify="center")
                self.flake_result2.grid(row=row_index, column=2, padx=5, pady=3)
                row_index += 1

            else:
                tk.Label(self, text=comp, width=15, anchor="w").grid(row=row_index, column=0, padx=5, pady=3)
                entry = tk.Entry(self, width=10)
                entry.grid(row=row_index, column=1, padx=5, pady=3)
                self.entries[comp] = entry

                # Results column (skip for Bunker mass)
                if comp != "Bunker mass (kg)":
                    result = tk.Entry(self, width=15, state="readonly", justify="center")
                    result.grid(row=row_index, column=2, padx=5, pady=3)
                    self.results[comp] = result
                else:
                    self.results[comp] = None  # no results box for Bunker

                # Special case: Master batch radio buttons
                if comp == "Master batch":
                    self.masterbatch_mode = tk.StringVar(value="kg")
                    tk.Radiobutton(self, text="kg", variable=self.masterbatch_mode, value="kg").grid(row=row_index, column=3, padx=5)
                    tk.Radiobutton(self, text="%", variable=self.masterbatch_mode, value="%").grid(row=row_index, column=4, padx=5)

                row_index += 1

        # Buttons
        calc_btn = ttk.Button(self, text="Calculate", command=self.calculate)
        calc_btn.grid(row=row_index, column=1, pady=10)

        reset_btn = ttk.Button(self, text="Reset", command=self.reset)
        reset_btn.grid(row=row_index, column=2, pady=10)

        # Menu bar (added once here, not inside toggle_flake2)
        self.add_menu()

    def toggle_flake2(self):
        # Enable/disable Flake2 and Mix entry depending on checkbox
        if self.mix_var.get() == 1:
            self.mix_entry.config(state="normal")
            self.flake2_entry.config(state="normal")
        else:
            self.mix_entry.delete(0, tk.END)
            self.mix_entry.config(state="disabled")
            self.flake2_entry.delete(0, tk.END)
            self.flake2_entry.config(state="disabled")

    def add_menu(self):
        # Menu bar
        menu_bar = tk.Menu(self)
        about_menu = tk.Menu(menu_bar, tearoff=0)
        about_menu.add_command(label="About", command=lambda: self.show_about())
        menu_bar.add_cascade(label="Help", menu=about_menu)
        self.config(menu=menu_bar)

    def show_about(self):
        # About window
        about_window = tk.Toplevel(self)
        about_window.title("About")
        about_window.geometry("300x200")
        about_window.resizable(False, False)

        ttk.Label(
            about_window,
            text="Recycling Meltspinning Calculator",
            font=("Segoe UI", 10, "bold")
        ).pack(pady=(10, 5))

        ttk.Label(about_window, text="Created by Behrouz Javanmardi").pack()

        def open_email():
            webbrowser.open("mailto:behrouz@javanmardi.org")

        email_label = tk.Label(
            about_window,
            text="behrouz@javanmardi.org",
            font=("Consolas", 9),
            fg="blue",
            cursor="hand2"
        )
        email_label.pack()
        email_label.bind("<Button-1>", lambda e: open_email())

        ttk.Label(about_window, text="License: MIT").pack()
        ttk.Label(about_window, text="Version: 1.5.1").pack(pady=(0, 10))

        ttk.Label(about_window, text="GitHub:").pack()

        def open_github():
            webbrowser.open("https://github.com/Javanmardi/RMCalculator")

        link_button = ttk.Button(about_window, text="Visit GitHub", command=open_github)
        link_button.pack(pady=5)

    def calculate(self):
        try:
            # Read values (default to 0 if empty)
            oil = float(self.entries["Oil (%)"].get() or 0)
            psu = float(self.entries["PSU (kg)"].get() or 0)
            spc = float(self.entries["Popcorn SPC (kg)"].get() or 0)
            skpc = float(self.entries["SKPC (kg)"].get() or 0)
            flake = float(self.flake_entry.get() or 0)  # FIX: use self.flake_entry
            chips = float(self.entries["Chips (kg)"].get() or 0)
            masterbatch = float(self.entries["Master batch"].get() or 0)
            waste = float(self.entries["Waste (%)"].get() or 0)
            bunker = float(self.entries["Bunker mass (kg)"].get() or 1)  # avoid div by zero

            # Oil percent is fixed
            oil_percent = oil

            # Other percents
            psu_percent = psu * (100 + waste) / bunker
            spc_percent = spc * (100 + waste) / bunker
            skpc_percent = skpc * (100 + waste) / bunker

            # Master batch logic
            if self.masterbatch_mode.get() == "kg":
                masterbatch_percent = masterbatch * (100 + waste) / bunker
            else:  # percent mode
                masterbatch_percent = masterbatch

            # Decide chips/flake based on total
            total = oil_percent + psu_percent + spc_percent + skpc_percent + masterbatch_percent

            if total < 300:
                chips_percent = chips * (100 + waste) / bunker
                flake_percent = (100 + waste) - (
                    oil_percent + psu_percent + spc_percent + skpc_percent + masterbatch_percent + chips_percent
                )
            else:
                flake_percent = flake * (100 + waste) / bunker
                chips_percent = (100 + waste) - (
                    oil_percent + psu_percent + spc_percent + skpc_percent + masterbatch_percent + flake_percent
                )

            # Flake mix logic
            if self.mix_var.get() == 1:
                mix_val = float(self.mix_entry.get() or 0)
                if 1 <= mix_val <= 99:
                    flake_percent1 = flake_percent * mix_val / 100
                    flake_percent2 = flake_percent * (100 - mix_val) / 100
                else:
                    flake_percent1 = flake_percent
                    flake_percent2 = 0
            else:
                flake_percent1 = flake_percent
                flake_percent2 = 0

            if total == 0:
                flake_percent1 = 0
                bunker = 0

            # Update results
            values = {
                "Oil (%)": oil_percent,
                "PSU (kg)": psu_percent,
                "Popcorn SPC (kg)": spc_percent,
                "SKPC (kg)": skpc_percent,
                "Chips (kg)": chips_percent,
                "Master batch": masterbatch_percent,
                "Waste (%)": waste,
                "Bunker mass (kg)": bunker
            }

            # Loop through dictionary and update result boxes
            for comp, val in values.items():
                if self.results[comp] is not None:  # skip Bunker mass since it has no result box
                    self.results[comp].config(state="normal")
                    self.results[comp].delete(0, tk.END)
                    self.results[comp].insert(0, f"{val:.2f}")
                    self.results[comp].config(state="readonly")

            # Flake results (two rows)
            self.flake_result1.config(state="normal")
            self.flake_result1.delete(0, tk.END)
            self.flake_result1.insert(0, f"{flake_percent1:.2f}")
            self.flake_result1.config(state="readonly")

            self.flake_result2.config(state="normal")
            self.flake_result2.delete(0, tk.END)
            self.flake_result2.insert(0, f"{flake_percent2:.2f}")
            self.flake_result2.config(state="readonly")

        except Exception as e:
            print("Error:", e)

    def reset(self):
        # Clear all entry and result boxes
        for comp in self.components:
            # Clear entry if it exists
            entry_widget = self.entries.get(comp)
            if entry_widget is not None:
                entry_widget.delete(0, tk.END)

            # Clear result if it exists and not None (skip Bunker mass)
            result_widget = self.results.get(comp)
            if result_widget is not None:
                result_widget.config(state="normal")
                result_widget.delete(0, tk.END)
                result_widget.config(state="readonly")

        # Clear flake results
        self.flake_entry.delete(0, tk.END)
        self.flake_result1.config(state="normal")
        self.flake_result1.delete(0, tk.END)
        self.flake_result1.config(state="readonly")

        self.flake2_entry.delete(0, tk.END)
        self.flake2_entry.config(state="disabled")
        self.flake_result2.config(state="normal")
        self.flake_result2.delete(0, tk.END)
        self.flake_result2.config(state="readonly")

        # Reset mix checkbox and entry
        self.mix_var.set(0)
        self.mix_entry.delete(0, tk.END)
        self.mix_entry.config(state="disabled")

        # Reset Master batch radio buttons to default (kg)
        if hasattr(self, "masterbatch_mode"):
            self.masterbatch_mode.set("kg")

if __name__ == "__main__":
    app = MeltSpinningCalculator()

    app.mainloop()

