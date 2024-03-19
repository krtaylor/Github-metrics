from github import Github
from github import GithubException

token = "PERSONAL_ACCESS_TOKEN" # Github personal access token

gh = Github(token)

orgs = ["ORG1", "ORG2"] # List of the Organizations to query

for org_name in orgs:

   org = gh.get_organization(org_name)
   print(" ")
   print("******************************************")
   print(org.name)
   print("******************************************")

   org_commits = 0
   repos = org.get_repos('all','full_name','asc')

   for repo in repos:
      print(" ")
      print(f"Repository:{repo.name}")
      print(f"Stars:{repo.stargazers_count}")
      try:
         commits = repo.get_commits().totalCount
         print(f"Commits:{commits}")
         org_commits = org_commits + commits
      except GithubException as e:
         #print(e.args[1]['message'])
         print("Commits:0")
         
      #print(repo.get_pulls().totalCount)
      #print(repo.get_issues().totalCount)
   print(f"Total commits for the Organization:{org_commits}")



