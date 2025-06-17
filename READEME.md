# 🚗 Python OOP Car System

This project is a powerful demonstration of Object-Oriented Programming (OOP) concepts implemented using **pure Python**. It simulates a real-world car manufacturing system, including classic cars, electric cars, batteries, and engines, while applying **encapsulation, inheritance, abstraction, and polymorphism**.

---

## 🧠 Key Features

### ✅ 1. Encapsulation
- Private attributes like `__model` and `__brand` are secured using name mangling.
- Safe access is provided via getters and setters.

### ✅ 2. Abstraction
- Complex details (e.g., battery or brand internals) are abstracted through method calls.
- Static and property methods keep access clean and safe.

### ✅ 3. Inheritance
- **Single Inheritance**: `ElectricCar` inherits from `Car`.
- **Multiple Inheritance**: `ElectricCarTwo` inherits from `Battery`, `Engine`, and `Car`.

### ✅ 4. Polymorphism
- Method overriding: `full_info()` and `fuel_type()` behave differently based on object type.

---

## 📂 Project Structure

```bash
├── main.py          
├── README.md 

```
## 💻 How to Run
python3 main.py

## ✍️ Author
👨‍💻 Wahaj Ali
COO @ Hashkoders
🔗 LinkedIn
🧠 Python | FastAPI | AI | Streamlit | Full Stack Web & Mobile Solutions
💬 Helping businesses scale with automation, AI integration, and real-world SaaS tools.

## Future Enhancements
 Add support for hybrid cars (petrol + electric)

 Abstract base class with abc module

 Add @property.setter for writable protected access

 Unit testing with pytest

 Connect with FastAPI backend and Streamlit frontend

 Track battery health as a dynamic attribute


