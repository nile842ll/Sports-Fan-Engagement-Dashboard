import pandas as pd
import matplotlib.pyplot as plt
from pytrends.request import TrendReq

TERMS = [
    "NFL",
    "Super Bowl",
    "Kansas City Chiefs",
    "San Francisco 49ers"
]

TIMEFRAME = "today 12-m"
GEO = "US"

pytrends = TrendReq(hl="en-US", tz=360)
pytrends.build_payload(TERMS, timeframe=TIMEFRAME, geo=GEO)

df = pytrends.interest_over_time()

if "isPartial" in df.columns:
    df = df.drop(columns=["isPartial"])

plt.figure()
for col in df.columns:
    plt.plot(df.index, df[col], label=col)

plt.title("Fan Engagement Proxy: Google Trends Interest Over Time")
plt.xlabel("Date")
plt.ylabel("Relative Interest (0–100)")
plt.legend()
plt.tight_layout()
plt.show()

print("Peak engagement by term:")
print(df.max().sort_values(ascending=False))
