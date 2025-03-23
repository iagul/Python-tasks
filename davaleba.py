kateti = int(input("pirveli katetis monacemi: "))
kateti2 = int(input("meore katetis monacemi: "))

hipotenuza = (kateti**2 + kateti2**2)

fartobi = 0.5 * kateti * kateti2

print(hipotenuza)
print(fartobi)

wamebi = int(input("sheiyvanet wami: "))

saati = wamebi // 3600
wami2 = wamebi % 3600
wutebi = wamebi // 60
wamebi1 = wamebi % 60

print(f"{wamebi} wami aris {saati} saati, {wutebi} wuti, {wamebi1} wami.")
