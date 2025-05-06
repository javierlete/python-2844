from datetime import date, datetime, timedelta

hoy = date.today()

print(f"Hoy es: {hoy}")
print(f"Hoy es: {hoy.strftime('%d/%m/%Y')}")

inicio = date(2025, 4, 9)

dias = (hoy - inicio).days

print(f"Llevamos {dias} días en este curso")
