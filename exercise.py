import json

with open("sample-data.json") as f:
    data = json.load(f)

print("Interface Status")
print("=" * 80)
print(f"{'DN':<50} {'Description':<20} {'Speed':<10} {'MTU':<5}")
print("-" * 80)

# Вставляем ограничение здесь:
for item in data["imdata"][:3]:  
    attributes = item["l1PhysIf"]["attributes"]
    dn = attributes["dn"]
    descr = attributes.get("descr", "")
    speed = attributes.get("speed", "inherit")
    mtu = attributes["mtu"]
    print(f"{dn:<50} {descr:<20} {speed:<10} {mtu:<5}")

    from datetime import datetime, timedelta

five_days_ago = datetime.now() - timedelta(days=5)
print("Five days ago:", five_days_ago)

from datetime import date, timedelta

today = date.today()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)

print("Yesterday:", yesterday)
print("Today:", today)
print("Tomorrow:", tomorrow)

from datetime import datetime

now = datetime.now()
no_microseconds = now.replace(microsecond=0)
print("Without microseconds:", no_microseconds)


from datetime import datetime

d1 = datetime(2023, 6, 1, 12, 0, 0)
d2 = datetime(2023, 6, 1, 12, 2, 30)

diff_seconds = int((d2 - d1).total_seconds())
print("Difference in seconds:", diff_seconds)


def squares_up_to(n):
    for i in range(n+1):
        yield i * i

for num in squares_up_to(5):
    print(num)


def even_numbers(n):
    for i in range(0, n+1, 2):
        yield i

n = int(input("Enter a number: "))
print(", ".join(str(x) for x in even_numbers(n)))


def divisible_by_3_and_4(n):
    for i in range(n+1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

for x in divisible_by_3_and_4(50):
    print(x)


def squares(a, b):
    for i in range(a, b+1):
        yield i * i

for val in squares(2, 6):
    print(val)


def countdown(n):
    for i in range(n, -1, -1):
        yield i

for num in countdown(5):
    print(num)