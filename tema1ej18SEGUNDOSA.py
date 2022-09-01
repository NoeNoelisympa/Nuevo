'''
segundos_user = int (input('Ingrese los segundos'))
segundos_a_horas = segundos_user // 60
segundos_a_minutos = segundos_user % 60
print(segundos_a_horas)
print(segundos_a_minutos)
'''


segundos_user = int (input('Ingrese los segundos'))
segundos_a_horas = (segundos_user / 60) / 60
segundos_a_minutos = segundos_user / 60
print('Total de horas {0}, minutos {1}'.format(segundos_a_horas, segundos_a_minutos))
'''

segundos_user = int (input('Ingrese los segundos'))
segundos_a_horas = segundos_user // 60
segundos_a_minutos = segundos_user % 60
segundos = segundos_a_horas - segundos_a_minutos
print(segundos_a_horas)
print(segundos_a_minutos)
