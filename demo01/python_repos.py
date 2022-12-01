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
# repo_dict = repo_dicts[0]
# print(f"\nKeys:{len(repo_dict)}")
# for key in sorted(repo_dict.keys()):
#     print(key)
# print(response_dict.keys())
# print('-------拉取repo_dict中一些关键的值--------')
# print("\n Selected ninformation about first repositories")
# print(f"Name :{repo_dict['name']}")
# print(f"html_url :{repo_dict['html_url']}")
# print(f"stargazers_count:{repo_dict['stargazers_count']}")
print("\n Selected information about each repository")
for repo_dict in repo_dicts:
    print(f"\nName:{repo_dict['name']}")
    print(f"\nOwner:{repo_dict['owner']['login']}")


