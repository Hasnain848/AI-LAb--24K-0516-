class Vehicle:
  def __init__(self,vehicle_id, brand, rent_per_day):
    self.vehicle_id = vehicle_id  
    self.brand = brand
    self.rent_per_day = rent_per_day
  def display_info(self):
    print(f"Vehicle ID: {self.vehicle_id}")
    print(f"Brand: {self.brand}")
    print(f"Rent per day: {self.rent_per_day}")
  def Calculate_rent(self,days):
    return self.rent_per_day * days

v1=Vehicle("V001","Toyota",50)
v1.display_info()
days=3
total_rent=v1.Calculate_rent(days)
print(f"Total rent for {days} days: {total_rent}")
print("======================================")
v2=Vehicle("V002","Honda",60)
v2.display_info()
days=2
total_rent= v2.Calculate_rent(days)
print(f"Total rent for {days} days: {total_rent}")



