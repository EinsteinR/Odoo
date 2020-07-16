from box_sort import pack
from math import ceil

print(f'{"Lp.":6} | {"mały":6}|{"średni":6} | {"duży":6}| {"zbiorczy"} ')
print(('-'*7+'+')*5)
for lp, boxes in enumerate([pack(i) for i in range(1, 101)], 1):
    print(f'{lp:6} |{boxes["box_s"]:6} |{boxes["box_m"]: 6} |'
          f'{boxes["box_l"]:6} |{( ceil(sum(boxes.values()) / 3.0) if sum(boxes.values()) > 1 else " "):6} |')

