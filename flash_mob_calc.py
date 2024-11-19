import tkinter as tk
from tkinter import messagebox
from re import search, IGNORECASE


class FlashMobCalc:
    def __init__(self, root):
        self.root = root
        self.root.title("Flash Mobs Calc")
        self.root.geometry("600x400")

        # Set dark theme colors
        self.bg_color = "#1e1e1e"  # Dark background
        self.fg_color = "#ffffff"  # White text
        self.entry_bg = "#2d2d2d"  # Slightly lighter background for entries
        self.button_bg = "#404040"  # Button background
        self.button_fg = "#ffffff"  # Button text
        self.text_bg = "#2d2d2d"  # Text area background
        self.highlight_bg = "#3d3d3d"  # Highlight background

        # Configure root window background
        self.root.configure(bg=self.bg_color)

        # Initialize minute counter
        self.minute_counter = 0

        # Location name lists remain unchanged
        self.port_phas_names = [
            "pp",
            "port phas",
            "port",
            "phas",
            "phasmatas",
            "portphas",
        ]
        self.mage_training_names = [
            "mta",
            "mage training",
            "mage",
            "mage training arena",
            "mage arena",
        ]
        self.uzer_names = ["uzer", "uz", "uzr", "uze"]
        self.mena_names = ["mena", "menaphos", "men", "menap", "menaph", "menapho"]
        self.edge_names = ["edge", "edgeville", "ev", "edg", "edgevill", "edgev"]
        self.hills_names = ["fh", "hills", "feldip", "fell", "fel", "f hills"]
        self.west_ardougne_names = [
            "wa",
            "west",
            "ardougne",
            "west ardougne",
            "ardy",
            "doug",
        ]
        self.poison_waste_names = ["pw", "poison waste", "poison", "waste", "prif"]
        self.seers_village_names = [
            "seers",
            "sv",
            "village",
            "seer",
            "srs",
            "seers village",
            "vill",
        ]

        self.big_list = []

        self.setup_gui()

    def setup_gui(self):
        # Create main frame for input fields
        input_frame = tk.Frame(self.root, bg=self.bg_color)
        input_frame.pack(pady=10)

        # Instructions with dark theme
        instructions = tk.Label(
            self.root,
            text="Tab between fields, Enter to submit",
            bg=self.bg_color,
            fg=self.fg_color,
            font=("Arial", 10),
        )
        instructions.pack(pady=5)

        locations = tk.Label(
            self.root,
            text="Valid Locations: pp, mta, uzer, mena, edge, fh, wa, pw, seers",
            bg=self.bg_color,
            fg=self.fg_color,
            font=("Arial", 10),
        )
        locations.pack(pady=5)

        # World input
        world_frame = tk.Frame(input_frame, bg=self.bg_color)
        world_frame.pack(side=tk.LEFT, padx=5)
        tk.Label(world_frame, text="World:", bg=self.bg_color, fg=self.fg_color).pack()
        self.world_entry = tk.Entry(
            world_frame,
            width=10,
            bg=self.entry_bg,
            fg=self.fg_color,
            insertbackground=self.fg_color,  # Cursor color
            relief=tk.FLAT,
        )
        self.world_entry.pack()

        # Location input
        location_frame = tk.Frame(input_frame, bg=self.bg_color)
        location_frame.pack(side=tk.LEFT, padx=5)
        tk.Label(
            location_frame, text="Location:", bg=self.bg_color, fg=self.fg_color
        ).pack()
        self.location_entry = tk.Entry(
            location_frame,
            width=15,
            bg=self.entry_bg,
            fg=self.fg_color,
            insertbackground=self.fg_color,
            relief=tk.FLAT,
        )
        self.location_entry.pack()

        # Time input
        time_frame = tk.Frame(input_frame, bg=self.bg_color)
        time_frame.pack(side=tk.LEFT, padx=5)
        tk.Label(
            time_frame, text="Time (mins):", bg=self.bg_color, fg=self.fg_color
        ).pack()
        self.time_entry = tk.Entry(
            time_frame,
            width=10,
            bg=self.entry_bg,
            fg=self.fg_color,
            insertbackground=self.fg_color,
            relief=tk.FLAT,
        )
        self.time_entry.pack()

        # Submit button with hover effect
        self.submit_button = tk.Button(
            input_frame,
            text="Submit",
            command=self.add_entry,
            bg=self.button_bg,
            fg=self.button_fg,
            relief=tk.FLAT,
            activebackground=self.highlight_bg,
            activeforeground=self.button_fg,
            padx=15,
            pady=5,
        )
        self.submit_button.pack(side=tk.LEFT, padx=10)

        # Bind Enter key to submit button
        self.root.bind("<Return>", lambda event: self.add_entry())

        # Timer display
        self.timer_label = tk.Label(
            self.root,
            text="Next update in: 60s",
            bg=self.bg_color,
            fg=self.fg_color,
            font=("Arial", 10),
        )
        self.timer_label.pack(pady=5)

        # Display area with dark theme
        self.display = tk.Text(
            self.root,
            height=15,
            width=50,
            bg=self.text_bg,
            fg=self.fg_color,
            relief=tk.FLAT,
            insertbackground=self.fg_color,
            selectbackground=self.highlight_bg,
            selectforeground=self.fg_color,
            font=("Courier", 10),
        )
        self.display.pack(pady=10)

        # Set initial focus
        self.world_entry.focus_set()

        # Start auto-refresh
        self.update_display()

    # The rest of the methods remain unchanged
    def add_entry(self):
        try:
            world = int(self.world_entry.get().strip())
            location = self.location_entry.get().strip()
            time_left = int(self.time_entry.get().strip())

            clean_location = self.get_clean_location(location)
            if not clean_location:
                messagebox.showerror("Error", "Invalid location!")
                return

            class Entry:
                def __init__(self, world, location, time_left):
                    self.world = world
                    self.location = location
                    self.time_left = time_left

            self.big_list.append(Entry(world, clean_location, time_left))

            # Clear entries and reset focus
            self.world_entry.delete(0, tk.END)
            self.location_entry.delete(0, tk.END)
            self.time_entry.delete(0, tk.END)
            self.world_entry.focus_set()

        except ValueError:
            messagebox.showerror("Error", "Invalid world or time value!")

    def get_clean_location(self, location_str):
        location_str = location_str.strip().lower()
        if location_str in self.port_phas_names:
            return 10001
        if location_str in self.mage_training_names:
            return 20002
        if location_str in self.uzer_names:
            return 30003
        if location_str in self.mena_names:
            return 40004
        if location_str in self.edge_names:
            return 50005
        if location_str in self.hills_names:
            return 60006
        if location_str in self.west_ardougne_names:
            return 70007
        if location_str in self.poison_waste_names:
            return 80008
        if location_str in self.seers_village_names:
            return 90009
        return None

    def get_location_name(self, location_num):
        locations = {
            10001: "pp",
            20002: "mta",
            30003: "uzer",
            40004: "mena",
            50005: "edge",
            60006: "fh",
            70007: "wa",
            80008: "pw",
            90009: "seers",
        }
        return locations.get(location_num, "unknown")

    def update_display(self):
        # Sort the list
        self.big_list = sorted(self.big_list, key=lambda x: x.time_left)
        self.big_list = sorted(self.big_list, key=lambda x: x.location)

        # Update display
        self.display.delete(1.0, tk.END)
        self.display.insert(tk.END, "-" * 30 + "\n")

        for entry in self.big_list:
            location_name = self.get_location_name(entry.location)
            self.display.insert(
                tk.END, f"{entry.world}, {location_name}, {entry.time_left}\n"
            )

        # Remove entries with elapsed time
        self.big_list = [entry for entry in self.big_list if entry.time_left > 0]

        # Update minute counter and decrement time if a minute has passed
        self.minute_counter += 1
        if self.minute_counter >= 60:  # 60 seconds = 1 minute
            for entry in self.big_list:
                entry.time_left -= 1
            self.minute_counter = 0

        # Update timer display
        seconds_left = 60 - self.minute_counter
        self.timer_label.config(text=f"Next update in: {seconds_left}s")

        # Schedule next update (still update display every second)
        self.root.after(1000, self.update_display)


if __name__ == "__main__":
    root = tk.Tk()
    app = FlashMobCalc(root)
    root.mainloop()
