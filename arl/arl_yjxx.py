from re import S
from cryptography.hazmat.primitives.asymmetric.ec import BrainpoolP256R1
import requests
import readline
import json
from prettytable import PrettyTable
import urllib3
from os import system, name
import urllib.request
print('''

        ██╗   ██╗   ██╗██╗  ██╗██╗  ██╗     ███████╗██╗  ██╗██████╗ ██╗      █████╗ ███╗   ██╗ ██████╗ 
        ╚██╗ ██╔╝   ██║╚██╗██╔╝╚██╗██╔╝     ██╔════╝╚██╗██╔╝██╔══██╗██║     ██╔══██╗████╗  ██║██╔════╝ 
         ╚████╔╝    ██║ ╚███╔╝  ╚███╔╝█████╗█████╗   ╚███╔╝ ██████╔╝██║     ███████║██╔██╗ ██║██║  ███╗
          ╚██╔╝██   ██║ ██╔██╗  ██╔██╗╚════╝██╔══╝   ██╔██╗ ██╔═══╝ ██║     ██╔══██║██║╚██╗██║██║   ██║
           ██║ ╚█████╔╝██╔╝ ██╗██╔╝ ██╗     ███████╗██╔╝ ██╗██║     ███████╗██║  ██║██║ ╚████║╚██████╔╝
           ╚═╝  ╚════╝ ╚═╝  ╚═╝╚═╝  ╚═╝     ╚══════╝╚═╝  ╚═╝╚═╝     ╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ 

                                                                                        ---\033[1;31mInfo：ExpLang\033[0m
                                                                                        ---\033[1;32mTeam:Secpt\033[0m
                            \033[1;35me = 退出脚本 \033[0m
                            \033[1;35mc = 清空控制台内容 \033[0m
                            \033[1;35mrm = 删除指定任务 \033[0m
                            \033[1;35madd = 添加新的任务 \033[0m
                            \033[1;35maddfile = 批量添加任务 \033[1;35m
                            \033[1;35mls = 查看当前任务列表 \033[0m
                            \033[1;35mstop = 暂停指定任务（可多次,英文逗号分割ID）\033[0m 
                            \033[1;35mipsf = 通过ip搜索资产 \033[0m
                            \033[1;35murlsf = 通过域名搜索资产 \033[0m
                            \033[1;35mtitlesf = 通过标题搜索资产 \033[0m''')
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
        print('''
        ██╗   ██╗   ██╗██╗  ██╗██╗  ██╗     ███████╗██╗  ██╗██████╗ ██╗      █████╗ ███╗   ██╗ ██████╗ 
        ╚██╗ ██╔╝   ██║╚██╗██╔╝╚██╗██╔╝     ██╔════╝╚██╗██╔╝██╔══██╗██║     ██╔══██╗████╗  ██║██╔════╝ 
         ╚████╔╝    ██║ ╚███╔╝  ╚███╔╝█████╗█████╗   ╚███╔╝ ██████╔╝██║     ███████║██╔██╗ ██║██║  ███╗
          ╚██╔╝██   ██║ ██╔██╗  ██╔██╗╚════╝██╔══╝   ██╔██╗ ██╔═══╝ ██║     ██╔══██║██║╚██╗██║██║   ██║
           ██║ ╚█████╔╝██╔╝ ██╗██╔╝ ██╗     ███████╗██╔╝ ██╗██║     ███████╗██║  ██║██║ ╚████║╚██████╔╝
           ╚═╝  ╚════╝ ╚═╝  ╚═╝╚═╝  ╚═╝     ╚══════╝╚═╝  ╚═╝╚═╝     ╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ 
                                                                                               
                                                                                        ---\033[1;31mInfo:ExpLang\033[0m
                                                                                        ---\033[1;32mTeam:云剑侠心\033[0m
                            \033[1;35me = 退出脚本 \033[0m
                            \033[1;35mc = 清空控制台内容 \033[0m
                            \033[1;35mrm = 删除指定任务 \033[0m
                            \033[1;35madd = 添加新的任务 \033[0m
                            \033[1;35maddfile = 批量添加任务 \033[1;35m
                            \033[1;35mls = 查看当前任务列表 \033[0m
                            \033[1;35mstop = 暂停指定任务（可多次,英文逗号分割ID）\033[0m 
                            \033[1;35mipsf = 通过ip搜索资产 \033[0m
                            \033[1;35murlsf = 通过域名搜索资产 \033[0m
                            \033[1;35mtitlesf = 通过标题搜索资产 \033[0m''')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')
        print('''
        ██╗   ██╗   ██╗██╗  ██╗██╗  ██╗     ███████╗██╗  ██╗██████╗ ██╗      █████╗ ███╗   ██╗ ██████╗ 
        ╚██╗ ██╔╝   ██║╚██╗██╔╝╚██╗██╔╝     ██╔════╝╚██╗██╔╝██╔══██╗██║     ██╔══██╗████╗  ██║██╔════╝ 
         ╚████╔╝    ██║ ╚███╔╝  ╚███╔╝█████╗█████╗   ╚███╔╝ ██████╔╝██║     ███████║██╔██╗ ██║██║  ███╗
          ╚██╔╝██   ██║ ██╔██╗  ██╔██╗╚════╝██╔══╝   ██╔██╗ ██╔═══╝ ██║     ██╔══██║██║╚██╗██║██║   ██║
           ██║ ╚█████╔╝██╔╝ ██╗██╔╝ ██╗     ███████╗██╔╝ ██╗██║     ███████╗██║  ██║██║ ╚████║╚██████╔╝
           ╚═╝  ╚════╝ ╚═╝  ╚═╝╚═╝  ╚═╝     ╚══════╝╚═╝  ╚═╝╚═╝     ╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ 
                                                                                               
                                                                                        ---\033[1;31mInfo:ExpLang\033[0m
                                                                                        ---\033[1;32mTeam:云剑侠心\033[0m
                            \033[1;35me = 退出脚本 \033[0m
                            \033[1;35mc = 清空控制台内容 \033[0m
                            \033[1;35mrm = 删除指定任务 \033[0m
                            \033[1;35madd = 添加新的任务 \033[0m
                            \033[1;35maddfile = 批量添加任务 \033[1;35m
                            \033[1;35mls = 查看当前任务列表 \033[0m
                            \033[1;35mstop = 暂停指定任务（可多次,英文逗号分割ID）\033[0m 
                            \033[1;35mipsf = 通过ip搜索资产 \033[0m
                            \033[1;35murlsf = 通过域名搜索资产 \033[0m
                            \033[1;35mtitlesf = 通过标题搜索资产 \033[0m''')
    # print out some text
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
apikey = "KEY"

def task():
    table = PrettyTable(['任务名称', '目标地址', '当前状态', '开始时间', '结束时间', '任务ID'])
    headers = {
    'accept': 'application/json',
    'Token': apikey
    }
    ceshi = requests.get("https://IP:5003/api/task/", headers=headers, verify=False)
    good = ceshi.text
    res = json.loads(good.encode('latin-1').decode('unicode_escape'))
    for i in res['items']:
        table.add_row([i['name'],i['target'],i['status'],i['start_time'],i['end_time'],i['_id']])
    else:
        print(table)
    table.clear_rows()
def add(name, target):
    headers = {
    'Content-type': 'application/json',
    'Token': apikey,
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"
    }
    data = {
        "name": name,
        "task_tag": "task",
        "target": target,
        "policy_id": "策略ID",
        "result_set_id": "策略ID"}
    jsondata = json.dumps(data, separators=(',', ':'), ensure_ascii=False)
    ceshi = requests.post("https://IP:5003/api/task/policy/", headers=headers, data=jsondata, verify=False)
    good = ceshi.text
    res = json.loads(good.encode('latin-1').decode('unicode_escape'))
    if res['message'] == 'success':
        print(res['message'] + '  \033[1;31m下发任务成功！\033[0m')
    else:
        print('\033[1;32m下发任务失败！\033[0m')
def stop(task_id):
    headers = {
    'Content-type': 'application/json',
    'Token': apikey,
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"
    }
    stopdata = {
        "task_id": [task_id]}
    jsonstopdata = json.dumps(stopdata, separators=(',', ':'), ensure_ascii=False)
    rstop = requests.post("https://IP:5003/api/task/batch_stop/", headers=headers, data=jsonstopdata, verify=False)
    good = rstop.text
    resstop = json.loads(good.encode('latin-1').decode('unicode_escape'))
    if resstop['message'] == 'success':
        print(resstop['message'] + '  \033[1;31m任务暂停成功！\033[0m')
    else:
        print('\033[1;32m任务暂停失败！\033[0m')
def rm(task_id):
    headers = {
    'Content-type': 'application/json',
    'Token': apikey,
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"
    }
    rmdata = {
        "del_task_data": True,
        "task_id": [task_id]
    }
    jsonrmdata = json.dumps(rmdata, separators=(',', ':'), ensure_ascii=False)
    rrm = requests.post("https://IP:5003/api/task/delete/", headers=headers, data=jsonrmdata, verify=False)
    good = rrm.text
    resrm = json.loads(good.encode('latin-1').decode('unicode_escape'))
    if resrm['message'] == 'success':
        print(resrm['message'] + '  \033[1;31m任务删除成功！\033[0m')
    else:
        print('\033[1;32m任务删除失败！\033[0m')
def urlsf(Description):
    site = PrettyTable(['URL', 'IP', '标题', '状态'])
    headers = {
    'accept': 'application/json',
    'Token': apikey
    }
    ceshi = requests.get("https://IP:5003/api/site/?site="+ Description, headers=headers, verify=False)
    good = ceshi.text.replace('\\','\\\\')
    res = json.loads(good.encode(r'latin-1').decode(r'unicode_escape'), strict=False)
    for i in res['items']:
        site.add_row([i['site'],i['ip'],i['title'],i['status']])
    else:
        print(site)
def ipsf(Description):
    site = PrettyTable(['URL', 'IP', '标题', '状态'])
    headers = {
    'accept': 'application/json',
    'Token': apikey
    }
    ceshi = requests.get("https://IP:5003/api/site/?ip="+ Description, headers=headers, verify=False)
    good = ceshi.text.replace('\\','\\\\')
    res = json.loads(good.encode(r'latin-1').decode(r'unicode_escape'), strict=False)
    for i in res['items']:
        site.add_row([i['site'],i['ip'],i['title'],i['status']])
    else:
        print(site)
def titlesf(Description):
    site = PrettyTable(['URL', 'IP', '标题', '状态'])
    headers = {
    'accept': 'application/json',
    'Token': apikey
    }
    ceshi = requests.get("https://IP:5003/api/site/?title="+ Description, headers=headers, verify=False)
    print("https://IP:5003/api/site/?title="+ Description)
    good = ceshi.text.replace('\\','\\\\')
    res = json.loads(good.encode(r'latin-1').decode(r'unicode_escape'), strict=False)
    for i in res['items']:
        site.add_row([i['site'],i['ip'],i['title'],i['status']])
    else:
        print(site)

xunhuan = 1
while xunhuan == 1:
    a = input("\033[1;31m>> \033[0m")
    if a == 'ls':
        task()
    if a == 'addfile':
        name = input('\033[1;34m[+] >> 任务名称：\033[0m')
        file = input('\033[1;34m[+] >> 目标文件：\033[0m')
        with open(file, 'r', encoding='utf-8') as file1:
            for readFile in file1: #逐行读取
                add(name.encode("utf-8","ignore").decode("latin-1"), readFile)
    if a == 'add':
        print('\033[1;31m[+] 任务目标英文逗号分割！例：1.2.3.4,4.3.2.1\033[0m')
        print('\033[1;32m--------------------------------------------------\033[0m')
        name = input('\033[1;34m[+] >> 任务名称：\033[0m')
        target = input('\033[1;34m[+] >> 任务目标：\033[0m')
        add(name.encode("utf-8","ignore").decode("latin-1"), target)
    if a == 'rm':
        task_id = input('\033[1;34m[+] >> 任务ID：\033[0m')
        stop(task_id)
        rm(task_id)
    if a == 'stop':
        task_id = input('\033[1;34m[+] >> 任务ID：\033[0m')
        stop(task_id)
    if a == 'urlsf':
        Description = input('\033[1;34m[+] >> 搜索URL：\033[0m')
        urlsf(Description.encode("utf-8","ignore").decode("latin-1"))
    if a == 'ipsf':
        Description = input('\033[1;34m[+] >> 搜索IP：\033[0m')
        ipsf(Description.encode("utf-8","ignore").decode("latin-1"))
    if a == 'titlesf':
        Description = input('\033[1;34m[+] >> 搜索标题：\033[0m')
        url_encode = urllib.request.quote(Description, safe='/:?=&', encoding='utf-8')
        titlesf(url_encode.encode("utf-8","ignore").decode("latin-1"))
    if a == 'c':
        clear()
    if a == 'e':
        break
