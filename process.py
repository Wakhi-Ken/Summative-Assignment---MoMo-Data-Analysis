import json
import re

# Load the JSON data
with open('process.json', 'r') as file:
    data = json.load(file)

# Function to extract relevant fields from the body
def extract_fields(body):
    fields = {}
    
    # Extract RWF amounts using regex
    amounts = re.findall(r'RWF\s*([\d,]+(?:\.\d{1,2})?)|([\d,]+(?:\.\d{1,2})?)\s*RWF', body)
    amounts = [match[0] if match[0] else match[1] for match in amounts]

    if "You have received" in body and amounts:
        fields['amount'] = amounts[0] + " RWF"  # Amount received
        sender_start = body.find('from') + len('from ')
        sender_end = body.find(' (', sender_start)
        fields['sender'] = body[sender_start:sender_end]  # Sender name
        fields['new_balance'] = amounts[-1] + " RWF"  # New balance

    elif "Your payment of" in body and amounts:
        fields['amount'] = amounts[0] + " RWF"  # Amount paid
        recipient_start = body.find('to') + len('to ')
        recipient_end = body.find(' ', recipient_start)
        fields['recipient'] = body[recipient_start:recipient_end]  # Recipient name
        fields['new_balance'] = amounts[-1] + " RWF"  # New balance

    elif "transferred to" in body and amounts:
        fields['amount'] = amounts[0] + " RWF"  # Amount transferred
        recipient_start = body.find('to') + len('to ')
        recipient_end = body.find(' (', recipient_start)
        fields['recipient'] = body[recipient_start:recipient_end]  # Recipient name
        fields['new_balance'] = amounts[-1] + " RWF"  # New balance

    elif "A bank deposit of" in body and amounts:
        fields['amount'] = amounts[0] + " RWF"  # Amount deposited
        fields['new_balance'] = amounts[-1] + " RWF"  # New balance

    elif "transaction of" in body and amounts:
        fields['amount'] = amounts[0] + " RWF"  # Amount in transaction
        fields['new_balance'] = amounts[-1] + " RWF"  # New balance

    return fields

# Process each category and subcategory
for category, transactions in data.items():
    for transaction in transactions:
        body = transaction['body']
        extracted_fields = extract_fields(body)
        transaction.update(extracted_fields)

# Save the updated data back to a new JSON file
with open('updated_process.json', 'w') as file:
    json.dump(data, file, indent=4)

print("Fields extracted and appended successfully.")