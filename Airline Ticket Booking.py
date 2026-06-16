print("Select station from where you want to have your flight =")
print("1.Delhi-DEL\n 2.Banglore-BLR\n 3.Ahmedabad-AMD\n 4.Mumbai-BOM\n 5.Kolkata-CCU")

dep=int(input("Enter Departure city = "))

if dep>=1 and dep<=5:
    print("Select station where you want to reach: ")
    print("1.London-LHR\n 2.Berlin-BER\n 3.Ontario-ON")
else:
    print("Invalid choice")

des=int(input("Enter Destination city:"))

if des>=1 and des<=3:
    date=input("Enter Departure date = ")
    print("Departure date = ",date)

    print("Select number of passengers: ")
    adult=int(input("Enter number of adult passengers = "))
    teen=int(input("Enter number of teen passengers"))
    infant_seat=int(input("Enter number of infants on seat = "))
    infant_lap=int(input("Enter number of infants on lap = "))

    total_passengers=adult + teen + infant_seat + infant_lap
    print("Total passengers = ",total_passengers)

# Fare calculation
    fare_adult = 100000
    fare_teen = 80000
    fare_infant_seat = 50000
    fare_infant_lap = 10000

    total_fare = adult*fare_adult + teen*fare_teen + infant_seat*fare_infant_seat + infant_lap*fare_infant_lap

    print("Fare details:")
    print("Adult passenger fare = ",fare_adult)
    print("Teen passenger fare = ",fare_teen)
    print("Infant on seat fare = ",fare_infant_seat)
    print("Infant on lap fare = ",fare_infant_lap)
    print("Total fare = ",total_fare)

    standard_bag_allowed_weight=25
    bag=int(input("Enter bag weight = "))
    if bag>25:
        print("Your bag weight is = ",bag,"kg")
        print("Your bag fare is = ",(bag-25)*2000)
    else:
        print("Your baggage is allowed, no extra charges")
    
    Carry_bag=5
    baggage=int(input("Enter your baggage weight = "))
    if baggage>5:
        print("Your baggage weight is = ",baggage,"kg")
        print("Your baggage fare is = ",(baggage-5)*1000)
    else:
        print("Your baggage is allowed, no extra charges")
else:
    print("Invalid destination")