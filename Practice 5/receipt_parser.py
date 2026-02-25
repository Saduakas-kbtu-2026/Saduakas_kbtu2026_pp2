# receipt_parser.py
import re
import json

# Read the raw receipt text from file
with open("raw.txt", encoding="utf-8") as f:
    receipt_text = f.read()

#extracting prices
# Prices may have spaces for thousands: "1 200,00"
price_pattern = re.compile(r'\b\d{1,3}(?: \d{3})*(?:,\d{2})?\b')
prices = price_pattern.findall(receipt_text)

# Convert prices to floats (replace comma and remove spaces)
def price_to_float(price_str):
    return float(price_str.replace(" ", "").replace(",", "."))

prices_float = [price_to_float(p) for p in prices]

# Extract product names
# Product lines appear before quantity x price and after numbering "1." etc.
product_pattern = re.compile(r'\d+\.\s+(.+?)(?=\n\d+,\d+\sx)')
products = product_pattern.findall(receipt_text)

# Alternative: extract lines that appear before "x " pattern
# product_pattern2 = re.compile(r'\d+\.\s+(.+)\n\d+,\d+\s*x')
# products = product_pattern2.findall(receipt_text)

# Calculate total amount
# Usually the last big number after "ИТОГО:"
total_pattern = re.compile(r'ИТОГО:\s*([\d ]+,\d{2})')
total_match = total_pattern.search(receipt_text)
total = price_to_float(total_match.group(1)) if total_match else sum(prices_float)

# Extract date and time
datetime_pattern = re.compile(r'Время:\s*([\d\.]+)\s+([\d:]+)')
datetime_match = datetime_pattern.search(receipt_text)
date = datetime_match.group(1) if datetime_match else ""
time = datetime_match.group(2) if datetime_match else ""

#  Find payment method
payment_pattern = re.compile(r'(Банковская карта|Наличные):')
payment_match = payment_pattern.search(receipt_text)
payment_method = payment_match.group(1) if payment_match else "Unknown"

# prepare structured output
parsed_receipt = {
    "products": [{"name": p, "price": prices_float[i]} for i, p in enumerate(products)],
    "total": total,
    "date": date,
    "time": time,
    "payment_method": payment_method
}

print(json.dumps(parsed_receipt, ensure_ascii=False, indent=4))
