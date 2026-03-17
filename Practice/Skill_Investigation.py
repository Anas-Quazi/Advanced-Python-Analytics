
#! find out which job you are getting based on skill set

#* Define data science job roles and required skills
job_roles = [
    {'role': 'Data Analyst', 'skills': ['Python', 'SQL', 'Excel']},
    {'role': 'Data Scientist', 'skills': ['Python', 'R', 'Machine Learning', 'Deep Learning']},
    {'role': 'Machine Learning Engineer', 'skills': ['Python', 'TensorFlow', 'PyTorch', 'Scikit-Learn']},
    {'role': 'Data Engineer', 'skills': ['Python', 'Apache Spark', 'Hadoop', 'SQL']},
    {'role': 'Business Intelligence Analyst', 'skills': ['Python', 'SQL', 'Tableau', 'Power BI', 'Excel']},
    {'role': 'Quantitative Analyst', 'skills': ['R', 'Python', 'MATLAB', 'Statistics']},
    {'role': 'Operations Analyst', 'skills': ['Python', 'SQL', 'Data Visualization', 'Process Improvement']},
    {'role': 'Database Administrator', 'skills': ['SQL', 'Oracle', 'MySQL', 'Database Management']},
    {'role': 'AI Engineer', 'skills': ['Python', 'TensorFlow', 'PyTorch', 'Computer Vision']},
    {'role': 'Statistician', 'skills': ['R', 'SAS', 'Python', 'Statistical Modeling']}
]

#? my skill set
mySkills = ['Python', 'SQL', 'Excel']

#~ job roles list
qualified_jobs = []

#todo go through the job_role list
for job in job_roles:

    #^ track qualification
    qualified = True
    for skill in job['skills']:
        
        #^ check if my skill in that job skill
        if skill not in mySkills:
            qualified = False
            break

    if qualified:
        qualified_jobs.append(job['role'])

print(qualified_jobs)

qualified_job = [
    job['role']
    for job in job_roles
    if all(skill in mySkills for skill in job['skills'])
]

print(qualified_job)