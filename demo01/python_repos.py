import requests

url = 'https://api.github.com/search/repositories?q=language:java&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f'Status code:{r.status_code}')
response_dict = r.json()
print(f"total repositories:{response_dict['total_count']}")
# 探索有关仓库的信息
repo_dicts = response_dict['items']
print(f"Respositories returned:{len(repo_dicts)}")
# 研究第一个仓库
repo_dict = repo_dicts[0]
print(f"\nKeys:{len(repo_dict)}")
for key in sorted(repo_dict.keys()):
    print(key)
print(response_dict.keys())
