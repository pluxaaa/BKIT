def field(items, *args):

    assert len(args) > 0
    if len(args) == 1:
        for data in items:
            current = data.get(args[0])
            if current is not None:
                yield current
    else:
        for elem in items:
            data = dict()
            for arg in args:
                current = elem.get(arg)
                if current is not None:
                    data[arg] = current
            if len(data) != 0:
                yield data


# goods = [
#    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
#    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
# ]
# print(list(field(goods, 'title'))) # 'Ковер', 'Диван для отдыха'
# print(list(field(goods, 'title', 'price'))) # {'title': 'Ковер', 'price': 2000}, {'title': 'Диван для отдыха', 'price': 5300}