# В офис заказали небольшую партию из четырёх мониторов и трёх наушников.
# У монитора есть четыре характеристики: название производителя, матрица, разрешение и частота обновления экрана.
# Все четыре монитора отличаются только частотой.
#
# У наушников три характеристики: название производителя, чувствительность и наличие микрофона.
# Отличие только в наличии микрофона.
#
#
#
# Для внесения в базу программист начал писать такой код:
# monitor_name_1 = 'Samsung'
# monitor_matrix_1 = 'VA'
# monitor_res_1 = 'WQHD'
# monitor_freq_1 = 60
# monitor_name_2 = 'Samsung'
# monitor_matrix_2 = 'VA'
# monitor_res_2 = 'WQHD'
# monitor_freq_2 = 144
# monitor_name_3 = 'Samsung'
# monitor_matrix_3 = 'VA'
# monitor_res_3 = 'WQHD'
# monitor_freq_3 = 70
# monitor_name_4 = 'Samsung'
# monitor_matrix_4 = 'VA'
# monitor_res_4 = 'WQHD'
# monitor_freq_4 = 60
#
# headphones_name_1 = 'Sony'
# headphones_sensitivity_1 = 108
# headphones_micro_1 = False
# headphones_name_2 = 'Sony'
# headphones_sensitivity_2 = 108
# headphones_micro_2 = True
# headphones_name_3 = 'Sony'
# headphones_sensitivity_3 = 108
# headphones_micro_3 = True
#
# Поправьте программиста: перепишите код, используя классы и экземпляры классов.
class Monitors:
    name = 'Samsung'
    matrix = 'VA'
    resolution = 'WQHD'
    freq = 60


class Headphones:
    name = 'Sony'
    sensitivity = 108
    micro = True


monitor_1 = Monitors()
monitor_2 = Monitors()
monitor_3 = Monitors()
monitor_4 = Monitors()

monitor_2.freq = 144
monitor_3.freq = 70

headphone_1 = Headphones()
headphone_2 = Headphones()
headphone_3 = Headphones()

headphone_1.micro = False
print('\n', monitor_1.name, monitor_1.matrix, monitor_1.resolution, monitor_1.freq, '\n',
      monitor_2.name, monitor_2.matrix, monitor_2.resolution, monitor_2.freq, '\n',
      monitor_3.name, monitor_3.matrix, monitor_3.resolution, monitor_3.freq, '\n',
      monitor_4.name, monitor_4.matrix, monitor_4.resolution, monitor_4.freq, '\n',
      headphone_1.name, headphone_1.sensitivity, headphone_1.micro, '\n',
      headphone_2.name, headphone_2.sensitivity, headphone_2.micro, '\n',
      headphone_3.name, headphone_3.sensitivity, headphone_3.micro)
