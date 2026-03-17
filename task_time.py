"""Time"""
N = int(input("Enter timer time: "))
HOURS = int(N/60)
MINUTES = N % 60
if N >= 0:
    HH = f"{HOURS:02d}"
    MM = f"{MINUTES:02d}"
    print(HH, ":", MM)
    DIGITS_SUM = sum(int(DIGIT) for DIGIT in (HH + MM))
    print("Sum of digits: ", DIGITS_SUM)
else:
    print("Enter correct timer time")
