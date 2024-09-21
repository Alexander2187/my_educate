from true_math import divide as t_m
from fake_math import divide as s_m

print(f'Простое деление  --->    {s_m(14, 0)}')
print(f'Простое деление  --->    {s_m(14, 25)}')
print('--------------------------------------------------')
print(f'Настоящее деление -->    {t_m(42, 0)}')
print(f'Настоящее деление -->    {t_m(42, 4.2)}')
