data_science_jobs = [
    {'job_title': 'Data Scientist', 'job_skills': "['Python', 'SQL', 'Machine Learning']", 'job_date': '2023-05-12'},
    {'job_title': 'Data Engineer', 'job_skills': "['AWS', 'Python', 'TensorFlow']", 'job_date': '2023-05-18'},
    {'job_title': 'Data Analyst', 'job_skills': "['Python', 'Data Analysis', 'SQL']", 'job_date': '2023-05-06'},
    {'job_title': 'ML Engineer', 'job_skills': "['PyTorch', 'Docker', 'Kubernetes']", 'job_date': '2023-06-01'},
    {'job_title': 'AI Researcher', 'job_skills': "['NLP', 'Computer Vision', 'PyTorch']", 'job_date': '2023-06-15'},
    {'job_title': 'BI Developer', 'job_skills': "['Power BI', 'Tableau', 'ETL']", 'job_date': '2023-05-22'},
    {'job_title': 'Cloud Architect', 'job_skills': "['Azure', 'GCP', 'Terraform']", 'job_date': '2023-06-10'},
    {'job_title': 'Database Administrator', 'job_skills': "['PostgreSQL', 'NoSQL', 'Redis']", 'job_date': '2023-05-29'}
]


#todo import date time & ast library
from datetime import datetime
import ast

print(datetime.now())

#^ temporary variable
test_date = data_science_jobs[0]['job_date']

#? format date
print(datetime.strptime(test_date, '%Y-%m-%d'))

#* clean data
for job in data_science_jobs:
    job['job_date'] = datetime.strptime(job['job_date'], '%Y-%m-%d')

    #todo clean up skills (string to list)
    #* use ast : abstract syntax trees
    job['job_skills'] = ast.literal_eval(job['job_skills'])

#~ verify...
for job in data_science_jobs:
    print(job)


