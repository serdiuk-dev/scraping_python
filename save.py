import csv


def save_to_csv(jobs):
    file = open('Result_scraping.csv', mode='w')
    writer = csv.writer(file)
    writer.writerow(['title', 'Company', 'Location/Salary',
                    'Link/Summary'])
    for job in jobs:
        # job.values()
        writer.writerow(list(job.values()))
    return
    # print(job.values())
