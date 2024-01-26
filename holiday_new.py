''' 
user inputs will be taken for- city they wish to fly to,number of nights they want to stay at the hotel and 
and number of days they wish to rent a car for.
 '''
while True:
        
        city_flight = input("Please enter the city you wish to fly to(select from -London,Tokyo,Newyork or Barcelona) :").capitalize()   
        if  city_flight == "London":
            print(f"You have chosen: {city_flight} as your destination.")
            break 
        elif  city_flight == "Tokyo":
            print(f"You have chosen: {city_flight} as your destination.")
            break 
        elif  city_flight == "Barcelona":
            print(f"You have chosen: {city_flight} as your destination.")
            break 
        elif  city_flight == "Newyork":
            print(f"You have chosen: {city_flight} as your destination.") 
            break 
             
        elif not city_flight.isalpha():
            print("You have entered a number.Please enter the city you wish to fly to!")
            continue
        else:
            print(f"Invalid input.Please try again!")
            continue
                   
        
while True:
    try: 
        num_nights = int(input("Please enter the number of nights you wish to stay at the hotel :"))
        if num_nights >0:
                print(f"You have selected {num_nights} nights.")
                break      

        else:
            print("Invalid input.Please enter a valid number.")
            continue
    except ValueError:
        print("Invalid input.Please enter a valid number greater than zero.")
while True:
        try: 
            rental_days = int(input("Please enter the number of days you wish to rent a car for :"))
            if rental_days > 0:
                print(F"You wish to rent a car for {rental_days} days.")
                break
            else:
                print("Invalid input.Please enter a valid number.")
                continue
        except  ValueError:
            print("Invalid input.Please enter a valid number greater than zero.")
            continue

# this function will return the total hotel cost of the user based on their input.    
def hotel_cost(num_nights):
    price_per_night = 500                         # chosen price per night charged at hotel
    total_cost =  num_nights * price_per_night    # chosen daily car rental cost
    return total_cost

# this variable will store the output of the hotel_cost funtion.
total_hotel_cost = hotel_cost(num_nights)         


# this function will return the total fare cost of the user based on their input.
def plane_cost(city_flight):
    
    fare_cost = city_flight
    if city_flight == "London":
        fare_cost = 2000
           
        print(f"The flight to {city_flight} will cost you £{fare_cost}.")
        
                
    elif city_flight == "Tokyo":
        fare_cost = 4500
            
        print(f"The flight to {city_flight} will cost you £{fare_cost}.")
        

    elif city_flight == "Newyork":
        fare_cost = 3700
        
        print(f"The flight to {city_flight} will cost you £{fare_cost}.")
            

    elif city_flight == "Barcelona":
        fare_cost = 4200

        print(f"The flight to {city_flight} will cost you £{fare_cost}.")
            

    else:

        print("Invalid character! Please enter the city you wish to fly.")

    return fare_cost

# this variable will store the output of the plane_cost funtion.
total_fare_cost = plane_cost(city_flight)   

# this function will return the total rental cost of the user based on their input.
def car_rental(rental_days):
    daily_rental_cost = 50
    car_rental_cost = rental_days * daily_rental_cost
    return car_rental_cost

# this variable will store the output of the car_rental funtion.
total_car_rental_cost = car_rental(rental_days)






# this function will return the total holiday cost of the user by calling other variables.
def holiday_cost():
    final_cost = total_hotel_cost + total_fare_cost + total_car_rental_cost
    
    print(f"""
            
            Dear Customer,\n
            Your total holiday cost to {city_flight} will be £{final_cost}.This itinerary includes the following :\n
            Your flight to {city_flight} will cost you : £{total_fare_cost}.\n
            Your selected {num_nights} days at the hotel will cost you £{total_hotel_cost}.\n
            Your selected {rental_days} days of car rental will cost you £{total_car_rental_cost}.\n
            """)
    

final_cost = holiday_cost()


