import tkinter as tk
from tkinter import messagebox
from re import search, IGNORECASE


class FlashMobCalc:
    def __init__(self, root):
        self.root = root
        self.root.title("Flash Mobs Calc")
        self.root.geometry("600x400")

        # Initialize minute counter
        self.minute_counter = 0

        # Location name lists
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
        # Instructions
        instructions = tk.Label(
            self.root, text="Enter: world, location, time left (in minutes)"
        )
        instructions.pack(pady=5)

        locations = tk.Label(
            self.root,
            text="Valid Locations: pp, mta, uzer, mena, edge, fh, wa, pw, seers",
        )
        locations.pack(pady=5)

        # Entry field
        self.entry = tk.Entry(self.root, width=40)
        self.entry.pack(pady=10)

        # Bind Enter key to add_entry
        self.entry.bind("<Return>", lambda event: self.add_entry())

        # Add button
        add_button = tk.Button(self.root, text="Add Entry", command=self.add_entry)
        add_button.pack(pady=5)

        # Timer display
        self.timer_label = tk.Label(self.root, text="Next update in: 60s")
        self.timer_label.pack(pady=5)

        # Display area
        self.display = tk.Text(self.root, height=15, width=50)
        self.display.pack(pady=10)

        # Start auto-refresh
        self.update_display()

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

    def add_entry(self):
        line = self.entry.get()
        result = search(r"(\d{1,3}\s*),(\s*[\w\s]+),(\s*\d{1,2})", line, IGNORECASE)

        if not result:
            messagebox.showerror("Error", "Invalid format! Use: world, location, time")
            return

        clean_location = self.get_clean_location(result.group(2))
        if not clean_location:
            messagebox.showerror("Error", "Invalid location!")
            return

        try:
            world = int(result.group(1).strip())
            time_left = int(result.group(3).strip())

            class Entry:
                def __init__(self, world, location, time_left):
                    self.world = world
                    self.location = location
                    self.time_left = time_left

            self.big_list.append(Entry(world, clean_location, time_left))
            self.entry.delete(0, tk.END)  # Clear entry field

        except ValueError:
            messagebox.showerror("Error", "Invalid world or time value!")

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
