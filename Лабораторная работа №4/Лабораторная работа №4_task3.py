def delete(list_, index=None):
    if index is None:  # определение индекса: задан он пользователем или берется по умолчанию
        del list_[-1]  # если индекс не задан, удаление последнего элемента списка
    else:
        del list_[index]  # если же индекс задан пользоваталем, удаление элемента, согласно данному индексу
    return list_


print(delete([0, 1, 2], index=0))  # [1, 2]
print(delete([0, 1, 2], index=1))  # [0, 2]
print(delete([0, 1, 2]))  # [0, 1]
