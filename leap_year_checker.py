year = int(input("What year would you like to check?\n"))

if year % 4 == 0:
  if year % 100 != 0:
    print(f"The year {year} is a leap year.")
  elif year % 100 == 0:
    if year % 400 == 0:
      print(f"The year {year} is a leap year.")
    else:
      print(f"The year {year} is NOT a leap year.")
  else:
    print(f"The year {year} is NOT a leap year.")
else:
  print(f"The year {year} is NOT a leap year.")