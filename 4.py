usd_rate = 4369
eur_rate = 4600
gbp_rate = 5500
jpy_rate = 28

cantidad_cop = float(input("Ingresa el valor en pesos colombianos"))

usd_valor = cantidad_cop / usd_rate
eur_valor = cantidad_cop / eur_rate
gbp_valor = cantidad_cop / gbp_rate
jpy_valor = cantidad_cop / jpy_rate
 
print("\la cantidad en otras monedas es")
print("La cantidad serían", usd_valor, "dólares")
print("La cantidad serían", eur_valor, "euros")
print("La cantidad serían", gbp_valor, "Libras britanicas")
print("La cantidad serían", jpy_valor, "Yenes")



