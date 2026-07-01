import tkinter as tk

class EmergencyOverlay:

    def show(self, score: float):
        self.root = tk.Tk()

        # MUST stay simple on macOS
        self.root.geometry("900x600")
        self.root.configure(bg="red")

        label = tk.Label(
            self.root,
            text="🚨 INTRUDER DETECTED 🚨",
            font=("Arial", 40, "bold"),
            fg="white",
            bg="red"
        )
        label.pack(expand=True)

        sub = tk.Label(
            self.root,
            text=f"Motion Score: {score:.0f}",
            font=("Arial", 20),
            fg="white",
            bg="red"
        )
        sub.pack()

        # force render safely
        self.root.update_idletasks()
        self.root.update()

        # stay visible 5 seconds
        self.root.after(5000, self.root.destroy)

        self.root.mainloop()
