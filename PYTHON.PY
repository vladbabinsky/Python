distance_AB = int(input("Введіть відстань між пунктом А і пунктом В (в км): "))
distance_BC = int(input("Введіть відстань між пунктом В і пунктом С (в км): "))
weight = int(input("Введіть вагу вантажу (в кг): \n"))

fuel_capacity = 300

if weight <= 500:
    fuel_consumption_per_km = 1
elif weight <= 1000:
    fuel_consumption_per_km = 4
elif weight <= 1500:
    fuel_consumption_per_km = 7
elif weight <= 2000:
    fuel_consumption_per_km = 9
else:
    print("Літак не може підняти вантаж більше 2000 кг\n")
    exit()

fuel_required_AB = distance_AB * fuel_consumption_per_km
fuel_required_BC = distance_BC * fuel_consumption_per_km

if fuel_required_AB > fuel_capacity:
    print('Не достатньо палива, щоб долетіти в пункт B\n')
    additional_fuel_needed = fuel_required_AB - fuel_capacity
    print(f'Не достатньо палива, щоб долетіти в пункт B з точки A. Потрібно дозаправити {additional_fuel_needed} літрів')
    exit()
else:
    print('Літак може долетіти в пункт B з точки А\n')
    remaining_fuel_after_AB = fuel_capacity - fuel_required_AB
    print(f'Після прибуття в пункт B залишиться {remaining_fuel_after_AB} літрів палива\n')

if fuel_required_BC > fuel_capacity:
    additional_fuel_needed = fuel_required_BC - fuel_capacity
    print(f'Не достатньо палива, щоб долетіти в пункт C з точки B. Потрібно дозаправити {additional_fuel_needed} літрів в пункті B')
else:
    print('Літак може долетіти в пункт C з точки B без дозаправки')

print(f"Для подолання відстані між пунктом А і пунктом В необхідно {fuel_required_AB} літрів палива")
print(f"Для подолання відстані між пунктом В і пунктом С необхідно {fuel_required_BC} літрів палива")

total_fuel_required = fuel_required_AB + fuel_required_BC
print(f"Необхідна мінімальна кількість палива для польоту з пункту А в пункт С через пункт В: {total_fuel_required} літрів")
