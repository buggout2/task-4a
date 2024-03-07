import pandas as pd

df = pd.read_csv("Task4a_data.csv")

gbp_rate = df["GBP - USD"][0]
usd_rate = df["USD - GBP"][0]


def convert_gbp_to_usd(amount_local, rate):
    """ Takes in amount in GBP and returns amount in USD """
    amount_usd = amount_local * rate
    return round(amount_usd, 2)


# Add function below to convert USD to GBP
def convert_usd_to_gbp(amount_local, rate):
    amount_gbp = amount_local * rate
    return round(amount_gbp, 2)


amount = float(input("Enter amount in GBP: "))
print(convert_usd_to_gbp(amount, gbp_rate))

amount = float(input("Enter amount in USD: "))
print(convert_gbp_to_usd(amount, usd_rate))


gbp_rate = df["GBP - JPY"] [0]
usd_rate = df["JPY - GBP"] [0]

def covert_gbp_to_jyp(amount_local,rate):
    """Takes in amount in GBP and return amount in JYP"""
    amount_jyp = amount_local * rate
    return round(amount_jyp,2)

def convert_jypto_gbp(amount_local, rate):
    amount_gbp = amount_local * rate
    return round(amount_gbp, 2)
amount = float(input("enter amount in GBP"))
print()
