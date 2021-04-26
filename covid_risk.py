age = input("Are you a cigarette addict older than 75 years old? (True or False): ")
chronic = input("Do you have a severe chronic disease? (True or False): ")
immune = input("Is your immune system too weak? (True or False): ")

if age == "True" or chronic == "True" or immune == "True":
    risk = True
    print(f"covid risk: {risk}")

else:
    risk = False
    print(f"covid risk: {risk}")