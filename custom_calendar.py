def start_end_calender():
    year = [2018, 2019, 2020]
    month = ['0' + str(x + 1) for x in range(9) if len(str(x)) == 1]
    for z in range(10, 13):
        month.append(str(z))
    start_date, end_date = [], []

    for x in year:
        for j in month[:7]:
            start_date.append(str(x) + '-' + j + '-' + '01')
            if x == 2020:
                if int(j) % 2 == 0 and int(j) != 2 and int(j) != 11 and int(j) != 12:
                    end_date.append(str(x) + '-' + j + '-' + '30')
                elif int(j) == 2:
                    end_date.append(str(x) + '-' + j + '-' + '29')
                else:
                    end_date.append(str(x) + '-' + j + '-' + '31')
            else:
                if int(j) % 2 == 0 and int(j) != 2 and int(j) != 12:
                    end_date.append(str(x) + '-' + j + '-' + '30')
                elif int(j) == 2:
                    end_date.append(str(x) + '-' + j + '-' + '28')
                else:
                    end_date.append(str(x) + '-' + j + '-' + '31')
        for j in month[7:]:
            start_date.append(str(x) + '-' + j + '-' + '01')
            if x == 2020:
                if int(j) % 2 == 0 and int(j) != 11 and int(j) != 12:
                    end_date.append(str(x) + '-' + j + '-' + '31')

                elif int(j) != 11 and int(j) != 12:
                    end_date.append(str(x) + '-' + j + '-' + '30')
            else:
                if int(j) % 2 == 0:
                    end_date.append(str(x) + '-' + j + '-' + '31')
                else:
                    end_date.append(str(x) + '-' + j + '-' + '30')

    return start_date, end_date


def everyday_calender():
    year = [2018, 2019, 2020]
    month = ['0' + str(x + 1) for x in range(9) if len(str(x)) == 1]
    day = ['0' + str(x + 1) for x in range(9) if len(str(x)) == 1]
    for z in range(10, 13):
        month.append(str(z))
    for z in range(10, 32):
        day.append(str(z))

    total_date = []

    for x in year:
        for j in month[:7]:
            if x == 2020:
                if int(j) % 2 == 0 and int(j) != 2 and int(j) != 11 and int(j) != 12:
                    for z in range(30):
                        total_date.append(str(x) + '-' + j + '-' + day[z])
                elif int(j) == 2:
                    for z in range(29):
                        total_date.append(str(x) + '-' + j + '-' + day[z])
                else:
                    for z in range(31):
                        total_date.append(str(x) + '-' + j + '-' + day[z])
            else:
                if int(j) % 2 == 0 and int(j) != 2 and int(j) != 12:
                    for z in range(30):
                        total_date.append(str(x) + '-' + j + '-' + day[z])
                elif int(j) == 2:
                    for z in range(28):
                        total_date.append(str(x) + '-' + j + '-' + day[z])
                else:
                    for z in range(31):
                        total_date.append(str(x) + '-' + j + '-' + day[z])
        for j in month[7:]:
            if x == 2020:
                if int(j) % 2 == 0 and int(j) != 11 and int(j) != 12:
                    for z in range(31):
                        total_date.append(str(x) + '-' + j + '-' + day[z])
                elif int(j) != 11 and int(j) != 12:
                    for z in range(30):
                        total_date.append(str(x) + '-' + j + '-' + day[z])
            else:
                if int(j) % 2 == 0:
                    for z in range(31):
                        total_date.append(str(x) + '-' + j + '-' + day[z])
                else:
                    for z in range(30):
                        total_date.append(str(x) + '-' + j + '-' + day[z])

    return total_date


if __name__ == '__main__':
    print(everyday_calender())
    print(len(everyday_calender()))
    print(everyday_calender()[:882])
    print(everyday_calender()[882:])
