import requests
from plotly import offline

url = 'https://api.github.com/search/repositories?q=language:java&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f'Status code:{r.status_code}')
response_dict = r.json()
print(f"total repositories:{response_dict['total_count']}")
# 探索有关仓库的信息
repo_dicts = response_dict['items']
repo_names, stars = [], []
for repo_dict in repo_dicts:
    repo_names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

# 可视化
data = [{
    'type': 'bar',
    'x': repo_names,
    'y': stars
}]
my_layout = {
    'title': 'GitHub上最受欢迎的Python项目',
    'xaxis': {'title': 'Repository'},
    'yaxis': {'title': 'Stars'}
}
fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename = 'python.repos_html')



print(f"Respositories returned:{len(repo_dicts)}")

# 研究第一个仓库
print("\n Selected information about each repository")
for repo_dict in repo_dicts:
    print(f"\nName:{repo_dict['name']}")
    print(f"\nOwner:{repo_dict['owner']['login']}")


