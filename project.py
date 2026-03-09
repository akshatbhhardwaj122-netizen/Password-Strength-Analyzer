import customtkinter as CTk
import re
import math

# Appearance Settings
CTk.set_appearance_mode("dark")
CTk.set_default_color_theme("blue")

class StrengthAnalyzer(CTk.CTk):
    def __init__(self):
        super().__init__()

        self.title("ShieldPass Pro")
        self.geometry("450x450")
        
        # Grid layout
        self.grid_columnconfigure(0, weight=1)
        
        # Header
        self.label = CTk.CTkLabel(self, text="Password Analyzer", font=("Roboto", 24, "bold"))
        self.label.pack(pady=(30, 10))

        # Password Entry & Toggle
        self.entry_frame = CTk.CTkFrame(self, fg_color="transparent")
        self.entry_frame.pack(pady=10)

        self.password_entry = CTk.CTkEntry(self.entry_frame, placeholder_text="Enter password...", 
                                           width=300, height=45, show="*")
        self.password_entry.grid(row=0, column=0, padx=(0, 10))
        self.password_entry.bind("<KeyRelease>", self.update_ui)

        self.show_pass = CTk.CTkCheckBox(self, text="Show Password", command=self.toggle_visibility)
        self.show_pass.pack(pady=5)

        # Progress Bar
        self.meter = CTk.CTkProgressBar(self, width=350, height=12)
        self.meter.set(0)
        self.meter.pack(pady=20)

        # Feedback Labels
        self.status_label = CTk.CTkLabel(self, text="Enter a password to begin", font=("Roboto", 14))
        self.status_label.pack()

        self.entropy_label = CTk.CTkLabel(self, text="Entropy: 0 bits", font=("Roboto", 12), text_color="gray")
        self.entropy_label.pack(pady=5)

    def toggle_visibility(self):
        if self.show_pass.get() == 1:
            self.password_entry.configure(show="")
        else:
            self.password_entry.configure(show="*")

    def calculate_entropy(self, password):
        if not password: return 0
        pool = 0
        if re.search("[a-z]", password): pool += 26
        if re.search("[A-Z]", password): pool += 26
        if re.search("[0-9]", password): pool += 10
        if re.search(r"[^a-zA-Z0-9]", password): pool += 32
        
        # Formula: E = L * log2(R)
        entropy = len(password) * math.log2(pool) if pool > 0 else 0
        return round(entropy, 2)

    def update_ui(self, event=None):
        password = self.password_entry.get()
        entropy = self.calculate_entropy(password)
        
        # Update progress and colors based on entropy
        # < 40: Weak | 40-60: Fair | 60-80: Good | 80+: Strong
        progress_val = min(entropy / 100, 1.0)
        self.meter.set(progress_val)
        
        self.entropy_label.configure(text=f"Entropy: {entropy} bits")

        if entropy < 40:
            self.meter.configure(progress_color="#E74C3C") # Red
            self.status_label.configure(text="Strength: Weak", text_color="#E74C3C")
        elif entropy < 65:
            self.meter.configure(progress_color="#F1C40F") # Yellow
            self.status_label.configure(text="Strength: Fair", text_color="#F1C40F")
        elif entropy < 85:
            self.meter.configure(progress_color="#3498DB") # Blue
            self.status_label.configure(text="Strength: Good", text_color="#3498DB")
        else:
            self.meter.configure(progress_color="#2ECC71") # Green
            self.status_label.configure(text="Strength: Strong", text_color="#2ECC71")

if __name__ == "__main__":
    app = StrengthAnalyzer()
    app.mainloop()