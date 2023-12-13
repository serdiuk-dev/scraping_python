from hh import get_jobs as hh_get_jobs
from jobsite import get_jobs as jobsite_get_jobs
from indeed import get_jobs as indeed_get_jobs
from save import save_to_csv

# hh_max_page = extract_max_page()
# hh_jobs = extract_hh_jobs(hh_max_page)

hh_jobs = hh_get_jobs()
jobsite_jobs = jobsite_get_jobs()
indeed_jobs = indeed_get_jobs()

jobs = hh_jobs + jobsite_jobs
# jobs = jobsite_jobs
save_to_csv(jobs)
# print(jobsite_jobs)
