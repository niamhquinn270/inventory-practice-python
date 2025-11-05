# Inventory Management System

This Python console application allows users to manage a basic inventory. It supports adding items, selling items, and viewing current stock levels through a simple menu interface.

## Features

- Add items to inventory
- Sell items with stock validation
- Display current inventory with formatted output
- Input handling and error messages for invalid operations

## How It Works

- Inventory is stored in a global dictionary (`inventory = {}`)
- Item names are normalized to lowercase for consistency
- Menu options guide the user through available actions
- Input is validated to prevent selling unavailable stock

## How to Run

```bash
python inventory.py


## Example Interaction


Inventory Management System
1. Add Item to Inventory
2. Sell Item
3. Display Inventory
4. Exit
Enter your choice: 1
Enter the item name: apples
Enter the quantity to add: 10
Added 10 of apples to inventory.

## Author

Created by Niamh Quinn (me) as part of my Python learning journey. Focused on clean logic, user interaction, and practical functionality.
