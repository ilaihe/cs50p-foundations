while True:
    try:
        fraction = input("Fraction: ")
        x_int, y_int = fraction.split("/")
        
        x = int(x_int)
        y = int(y_int)
        if x > y or x < 0 or y <0:
            continue
        percentage = round((x / y) * 100)

        break
    except (ValueError, ZeroDivisionError):
        pass

if percentage <= 1:
    print("E")
elif percentage >= 99:
    print("F")
else:
    print(f"{percentage}%")


