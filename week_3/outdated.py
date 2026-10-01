month = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:

    date_str = input("Date: ").strip()
    
    try:
        if "/" in date_str:
            month_, day_, year_ = date_str.split("/")
            m = int(month_)
            d = int(day_)
            y = int(year_)

            if 1 <= m <= 12 and 1 <= d <= 31:
                print(f"{y:04}-{m:02}-{d:02}")
                break

        elif "," in date_str:
            month_day, year = date_str.split(",")
            m_day, day = month_day.split()
            if m_day in month:
                 m = month.index(m_day) + 1
                 d = int(day)
                 y = int(year)

                 if 1 <= m <= 12 and 1 <= d <= 31:
                    print(f"{y:04}-{m:02}-{d:02}")
                    break
            else:
                 continue
            

    except ValueError:
            pass    
    