n = int(input())
invited_guests = set()
guests_who_came = set()
for _ in range(n):
    guests = input()
    invited_guests.add(guests)

data = input()
while data != "END":
    guests_who_came.add(data)
    data = input()
invites_guests_who_came = invited_guests.difference(guests_who_came)
vip_guests = []
regular_guests = []
for g in invites_guests_who_came:
    if g[0].isdigit():
        vip_guests.append(g)
    else:
        regular_guests.append(g)
number_of_guests_who_came = len(invites_guests_who_came)
vip_guests = sorted(vip_guests)
regular_guests = sorted(regular_guests)
print(number_of_guests_who_came)
if vip_guests:
    [print(g) for g in vip_guests]
if regular_guests:
    [print(g) for g in regular_guests]

