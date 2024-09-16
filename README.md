 Project Overview\
 
This project is a simple staff requisition management system. It collects staff details, calculates requisition totals, and approves or holds requisitions based on the total cost.

 Features
- Staff Information Collection: Gathers staff ID, name, and requisition details.
- Requisition Total Calculation: Calculates the total cost of multiple items.
- Approval System: Approves requisitions below a set threshold and generates an approval reference number.
- Interactive Console: Accepts user input for real-time requisition processing.

 Code Structure
- Part_A.py: Main Python script containing all the functions for collecting data, calculating totals, and processing approvals.

 Attributes
- staff_id: Unique ID for the staff member.
- staff_name: Name of the staff member.
- requisition_item_total: Total value of the requisition.

 Methods
- `staff_info()`: Gathers staff details and generates a requisition ID.
- `requisitions_total()`: Calculates the total value of the requisition based on item prices.
- `requisitions_approval()`: Approves or holds the requisition based on the total cost.
- `display_requisitions()`: Displays the requisition summary and approval status.

 How to Run
1. Ensure Python is installed on your system.
2. Run the Part_A.py file in Visual Studio Code
3. Follow the prompts to input staff and requisition details.
