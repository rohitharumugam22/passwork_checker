import tkinter as tk
import re
def check_password():
    password = entry.get()
    strength = 0
    feedback = []
    
    # Length check
    if len(password) >= 8: 
        strength += 1
    else: 
        feedback.append("Password should be at least 8 characters")
    
    # Complexity checks
    if re.search(r"[A-Z]", password): strength += 1
    else: feedback.append("Add uppercase letters")
        
    if re.search(r"[a-z]", password): strength += 1
    else: feedback.append("Add lowercase letters")
        
    if re.search(r"[0-9]", password): strength += 1
    else: feedback.append("Add numbers")
        
    if re.search(r"[!@#$%^&*()_+=-]", password): strength += 1
    else: feedback.append("Add special characters")
    
    # Strength rating
    if strength < 2: result = "❌ Very Weak"
    elif strength < 4: result = "⚠️ Medium"
    else: result = "✅ Strong"
    
    feedback_label.config(text="\n".join(feedback))
    strength_label.config(text=result)

# Create GUI
root = tk.Tk()
root.title("Password Checker")

tk.Label(root, text="Enter Password:").pack()
entry = tk.Entry(root, show="*")
entry.pack()

tk.Button(root, text="Check Strength", command=check_password).pack()

strength_label = tk.Label(root, text="")
strength_label.pack()

feedback_label = tk.Label(root, text="", justify="left")
feedback_label.pack()

root.mainloop()