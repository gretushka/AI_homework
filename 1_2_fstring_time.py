def to_2_figures(input):
    if input < 1:
        return '00'
    elif input < 10:
        return '0' + str(input)
    return input


time_sec = int(input('Input time in seconds '))
print(
    f"In format hh:mm:ss it's {to_2_figures(time_sec // 3600)}:{to_2_figures(time_sec % 3600 // 60)}:{to_2_figures(time_sec % 60)}")
