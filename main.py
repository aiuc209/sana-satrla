from datetime import datetime

def format_dates(dates):
    formatted_dates = []
    for date in dates:
        formatted_date = datetime.strptime(date, "%Y-%m-%d").strftime("%d-%B, %Y")
        formatted_dates.append(formatted_date)
    return formatted_dates

dates = ["2025-04-18", "2024-03-20", "2023-02-15"]
print(format_dates(dates))
