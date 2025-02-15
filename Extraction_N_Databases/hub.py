import json
import re
import xml.etree.ElementTree as ET
from datetime import datetime

# Load and parse the XML file
tree = ET.parse('modified_sms.xml')
root = tree.getroot()

# Define keywords for categorization
keywords = {
    "Incoming_Money": ["received", "incoming money"],
    "Payments_to_Code_Holders": ["payment", "paid"],
    "Transfers_to_Mobile_Numbers": ["transfer", "sent to"],
    "Bank_Deposits": ["bank deposit", "deposited"],
    "Airtime_Bill_Payments": ["Amafaranga"],
    "Cash_Power_Bill_Payments": ["cash power", "electricity bill"],
    "Transactions_Initiated_by_Third Parties": ["transaction", "initiated by"],
    "Withdrawals_from_Agents": ["withdrawal", "agent"],
    "Bank_Transfers": ["bank transfer", "transferred"],
    "Internet_and_Voice_Bundle_Purchases": ["Umaze", "kugura ", "igura"],
    "Other": []
}

# Initialize categorized messages and log for unprocessed messages
categorized_sms = {key: [] for key in keywords.keys()}
unprocessed_messages = []

def normalize_date(timestamp):
    """Convert timestamp to a readable date format."""
    try:
        return datetime.fromtimestamp(int(timestamp) / 1000).strftime('%Y-%m-%d %H:%M:%S')
    except Exception:
        return None

# Iterate over each <sms> element
for sms in root.findall('sms'):
    # Extract relevant attributes
    body = sms.attrib.get('body')
    address = sms.attrib.get('address')
    date_sent = sms.attrib.get('date_sent')
    readable_date = sms.attrib.get('readable_date')
    contact_name = sms.attrib.get('contact_name')
    service_center = sms.attrib.get('service_center')

    # Validate extracted data
    if not body or not isinstance(body, str):
        unprocessed_messages.append(f"Missing or invalid body: {body}")
        continue

    if not date_sent:
        unprocessed_messages.append("Missing date_sent.")
        continue

    # Normalize date
    formatted_date = normalize_date(date_sent)

    # Categorization logic
    categorized = False
    for category, keys in keywords.items():
        if any(keyword in body.lower() for keyword in keys):
            categorized_sms[category].append({
                "contact_name": contact_name,
                "address": address,
                "date_sent": formatted_date,
                "readable_date": readable_date,
                "body": body,
                "service_center": service_center
            })
            categorized = True
            break  # Stop checking once categorized

    if not categorized:
        categorized_sms["Other"].append({
            "contact_name": contact_name,
            "address": address,
            "date_sent": formatted_date,
            "readable_date": readable_date,
            "body": body,
            "service_center": service_center
        })

# Store categorized messages in a single JSON file
with open('process.json', 'w') as json_file:
    json.dump(categorized_sms, json_file, indent=4)

# Log unprocessed messages
with open('unprocessed_messages.log', 'w') as log_file:
    for msg in unprocessed_messages:
        log_file.write(f"{msg}\n")

# print the final results for review
for category, messages in categorized_sms.items():
    print(f"{category}: {len(messages)} messages stored in process.json")

# Load the categorized messages from process.json
with open('process.json', 'r') as json_file:
    categorized_sms = json.load(json_file)

# Function to extract RWF amounts from the text using regex
def extract_rwf_amount(text):
    """Extract RWF amounts from the text using regex."""
    # Match patterns like "RWF 1000", "1000 RWF", "RWF1,000", etc.
    matches = re.findall(r'RWF\s*([\d,]+(?:\.\d{1,2})?)|([\d,]+(?:\.\d{1,2})?)\s*RWF', text)
    amounts = []
    for match in matches:
        # Extract the first non-empty match group
        amount = match[0] if match[0] else match[1]
        # Remove commas and convert to float
        amounts.append(float(amount.replace(',', '')))
    return amounts

# Initialize balances for each category
category_balances = {key: 0 for key in categorized_sms.keys()}

# Calculate balances for each category
for category, messages in categorized_sms.items():
    for message in messages:
        body = message.get('body', '')
        amounts = extract_rwf_amount(body)
        if amounts:
            # Sum the amounts for the category
            category_balances[category] += sum(amounts)

# Save the balances to balances.json
with open('balances.json', 'w') as balances_file:
    json.dump(category_balances, balances_file, indent=4)

# Print the final results for review
for category, balance in category_balances.items():
    print(f"{category}: Total RWF {balance:.2f}")