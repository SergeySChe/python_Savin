print('Hello World')

weather = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

weather_changes = []
for sign in weather:
    if sign.isdigit():
        weather_changes.extend(['"', f'{int(sign):02}', '"'])
    elif(sign.startswith('+') or sign.startswith('-')) and sign[1:].isdigit():
        weather_changes.extend(['"', f'{sign[0]}{int(sign[1:]):2}', '"'])
    else:
        weather_changes.append(sign)
out_weather = ' '.join(weather_changes)
print(out_weather)


