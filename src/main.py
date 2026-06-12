from datetime import date
from utils import add, subtract, multiply, divide

print("Name: S. Mahmud Nabil")
print(f"Date: {date.today()}")

print(f"10 + 5 = {add(10, 5)}")
print(f"10 - 5 = {subtract(10, 5)}")
print(f"10 * 5 = {multiply(10, 5)}")

try:
    print(f"10 / 2 = {divide(10, 2)}")
    print(f"10 / 0 = {divide(10, 0)}")
except ValueError as e:
    print(f"Error: {e}")
