def pack(n: int):
    if not isinstance(n, int):
        raise TypeError('invalid data type')
    if not 1 <= n <= 100:
        raise ValueError('value out of range')
    three_pack = n // 3 + 1 if n % 3 else n // 3
    layout = {
        'box_s': 1 if three_pack % 3 == 1 else 0,
        'box_m': 1 if three_pack % 3 == 2 else 0,
        'box_l': three_pack // 3}
    if layout['box_l'] == 1 and layout['box_s'] == 1:
        layout['box_s'] = layout['box_l'] = 0
        layout['box_m'] = 2
    elif layout['box_l'] == 1 and layout['box_m'] == 1:
        layout['box_m'] = 0
        layout['box_l'] += 1
    return layout

