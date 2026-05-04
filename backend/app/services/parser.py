import pandas as pd

def parse_csv(file):
    df = pd.read_csv(file, encoding="utf-8")

    # Normalise column names (lowercase, remove spaces)
    df.columns = [col.strip().lower() for col in df.columns]

    transactions = []

    for _, row in df.iterrows():
        date = get_value(row, ["date", "transaction date"])
        description = get_value(row, ["description", "details", "merchant"])

        # Handle amount OR debit/credit format
        amount = None

        if "amount" in row:
            amount = safe_float(row.get("amount"))
        else:
            debit = safe_float(row.get("debit"))
            credit = safe_float(row.get("credit"))

            if debit:
                amount = -debit
            elif credit:
                amount = credit
            else:
                amount = 0

        transaction = {
            "date": str(date),
            "description": str(description),
            "amount": amount
        }

        transactions.append(transaction)

    return transactions

def get_value(row, possible_keys):
    
    for key in possible_keys:
        if key in row and pd.notna(row[key]):
            return row[key]
    return ""
        
def safe_float(value):
    try:
        return float(value)
    except:
        return 0