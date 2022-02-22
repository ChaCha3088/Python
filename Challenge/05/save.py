import csv

def save_to_file(name1, details_list):
    file = open(f'D:/OneDrive - konkuk.ac.kr/바탕 화면/작업/동계/코딩/Python/Challenge/05/{name1}.csv', mode = 'w', encoding='UTF-8', newline="")
    writer = csv.writer(file)
    writer.writerow(['place', 'title', 'time', 'pay', 'date'])
    for job in details_list:
        try:
            writer.writerow(list(job.values()))
        except:
            pass
    return