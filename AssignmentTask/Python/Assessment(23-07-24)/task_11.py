#Write a function that stores information about a car in a dictionary .
# The function should always receive a manufacturer and a model name.
# It should then accept an arbitary number of keyword arguments. 

def car(company, model, **kwargs):
    print("Company:",company)
    print("Model: ",model)
    for key, value in kwargs.items():
          print(f"{key.capitalize()}: {value}")

def main():
    car(company='Ford', model='2024', personname='Prasanth', color='Blue', price=4500000)
if __name__ == "__main__":
    main()
