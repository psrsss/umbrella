# Time converter
HOURS = int(input("Enter how many hours on your watch: "))
MINUTES = int(input("Enter how many minutes on your watch: "))
MM = f"{MINUTES:02d}"
if HOURS > 12:
    HOURS12 = HOURS % 12
    print("Time: ", HOURS12, ":", MM, "p.m.")
elif HOURS == 12:
    print("Time: ", HOURS, ":", MM, "p.m.")
else:
    print("Time: ", HOURS, ":", MM, "a.m.")
