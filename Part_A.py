# Staff Information and Requisition Management

def staff_info():
    global date
    global staff_id
    global staff_name
    global requisition_id
    # This function is used to enter the date
    date = input("Enter the date: ")
    # This function is used to enter the staff_id
    staff_id = input("Enter the staff_ID: ")
    # This function is used to enter the staff_name
    staff_name = input("Enter the staff_name: ")
    requisition_id = 1 + 10000
    # This function is used to print the date
    print("Date:", date)
    # This function is used to print the staff_id
    print("Staff ID:", staff_id)
    # This function is used to print the staff_name
    print("Staff Name:", staff_name)
    # This function is used to print the requisition_id
    print("Requisition ID:", requisition_id)
    # This function is used to return 
    return {
        "date": date,
        "staff_id": staff_id,
        "staff_name": staff_name,
        "requisition_id": requisition_id
    }

staff_info()

# Call the function
def requisitions_total():
    global requisition_item_total
    # This function is used to enter the price of coffee
    coffee = input("Enter the price of coffee $: ")
    # This function is used to enter the price of paper
    paper = input("Enter the price of paper $: ")
    # This function is used to enter the price of pen
    pen = input("Enter the price of pen $: ")
    # Total amount
    requisition_item_total = int(coffee) + int(paper) + int(pen)
    # Prints the total value of requisition item
    print("The total value of requisition item is $", requisition_item_total)
    # Return the value
    return requisition_item_total

requisitions_total()

# Call the function
def requisitions_approval():
    global approval_reference_number
    if requisition_item_total < 500:
        print("Status: Approved")
    else:
        print("Status: Pending")
    approval_reference_number = str(staff_id) + str(requisition_id)[2:]
    print("Approval Reference Number:", approval_reference_number)

requisitions_approval()

def display_requisitions():
    print("Date:", date)
    print("Requisition ID:", requisition_id)
    print("Staff ID:", staff_id)
    print("Staff Name:", staff_name)
    print("Total: $", requisition_item_total)
    if requisition_item_total < 500:
        print("Status: Approved")
    else:
        print("Status: Pending")
    print("Approval Reference Number:", approval_reference_number)

display_requisitions()
