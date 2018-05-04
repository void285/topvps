# coding: utf-8

import sys
import requests
import logging
import argparse
import platform
import socket

if platform.platform().startswith("Windows"):
    import win_inet_pton

class VultrManager():

    def __init__(self, apikey, ssh_keyid=None, scriptid=None, proxy=None):
        self.name = socket.gethostname()
        self.proxies = {"http": proxy, "https": proxy}  # default no proxy
        self.api = {"API-KEY": apikey}
        self.ssh_keyid = ssh_keyid
        self.scriptid = scriptid

    def listServers(self):
        url = "https://api.vultr.com/v1/server/list"
        res = requests.get(url, headers=self.api, proxies=self.proxies)
        servers = res.json()
        return servers

    def getServerInfo(self, mid):
        servers = self.listServers()
        for serverId, server in servers.iteriterms():
            hostname = server["label"]
            hostId = hostname.split("-")[-1]
            if hostId == mid:
                for info in server:
                    print info + "\t" + str(server[info])

    def getServersInfo(self):
        infos = []
        servers = self.listServers()
        for serverId, server in servers.iteritems():
            hostname = server["label"]
            ip = server["main_ip"]
            info = [serverId, hostname, ip]
            infos.append(info)
            print serverId + "\t" + hostname + "\t" + ip
        return infos

    def getOneId(self, mid):
        servers = self.listServers()
        for serverId, server in servers.iteritems():
            hostname = server["label"]
            hostId = hostname.split("-")[-1]
            if hostId == mid:
                return serverId, hostname
        return None, None

    def createOne(self, mids):
        if not type(mids) == list:
            mids = [mids]
        url = "https://api.vultr.com/v1/server/create"
        serverId = None
        for mid in mids:
            name = hostGroup + "-" + str(mid)
            argvs = {
                "DCID": 19,
                "OSID": 160,
                "VPSPLANID": 29,
                "SCRIPTID": self.scriptid,
                "SSHKEYID": self.ssh_keyid,
                "hostname": name,
                "label": name
            }
            res = requests.post(url, headers=self.api, data=argvs, proxies=self.proxies)
            if res.status_code != 200:
                log = "create server " + name + " failed, " + res.text
                logging.error(log)
            else:
                serverId = res.json()["SUBID"]
                log = "server " + name + " created, its id is " + serverId
                logging.info(log)
        return serverId

    def createMany(self, start, end):
        for i in range(start, end+1):
            self.createOne(i)

    def destroyOne(self, mids):
        if not type(mids) == list:
            mids = [mids]
        result = None
        for mid in mids:
            serverId, hostname = self.getOneId(mid)
            url = "https://api.vultr.com/v1/server/destroy"
            data = {"SUBID": serverId}
            res = requests.post(url, headers=self.api, proxies=self.proxies, data=data)
            if res.status_code == 200:
                log = hostname + " destroyed"
                logging.info(log)
                result = True
            else:
                log = "Failed, status code: " + str(res.status_code)
        return result

    def rebootOne(self, mids):
        if not type(mids) == list:
            mids = [mids]
        result = None
        for mid in mids:
            serverId, hostname = self.getOneId(mid)
            url = "https://api.vultr.com/v1/server/reboot"
            data = {"SUBID": serverId}
            res = requests.post(url, headers=self.api, proxies=self.proxies, data=data)
            if res.status_code == 200:
                log = hostname + " rebooted"
                logging.info(log)
                result = True
            else:
                log = "Failed, status code: " + str(res.status_code)
        return result

    def destroyMe(self):
        hostId = self.name.split("-")[-1]
        serverId, hostname = self.getOneId(hostId)
        if not serverId:
            log = "can not find you, misson failed"
            logging.error(log)
            return
        else:
            sd = self.destroyOne(hostId)
            return sd

    def destroyAll(self):
        servers = self.getServersInfo()
        for server in servers:
            serverId, hostname, ip = server
            hostId = hostname.split("-")[-1]
            self.destroyOne(hostId)

    def rebootAll(self):
        servers = self.getServersInfo()
        for server in servers:
            serverId, hostname, ip = server
            hostId = hostname.split("-")[-1]
            self.rebootOne(hostId)

    def updateScript(self):
        url = "https://api.vultr.com/v1/startupscript/update"
        script = open("vultr.sh", "r").read()
        data = {
            "SCRIPTID": self.scriptid,
            "name": "default",
            "script": script
        }
        res = requests.post(url, headers=self.api, proxies=self.proxies, data=data)
        if res.status_code == 200:
            log = str(self.scriptid) + " updated"
            logging.info(log)
        else:
            print res.status_code

def collect_mids():
        mids = []
        for i in range(len(sys.argv)-3):
            mid = sys.argv[i+3]
            mids.append(mid)

if __name__ == "__main__":
    argParser = argparse.ArgumentParser()
    argParser.add_argument('-k', '--key', dest='key', type=str, required=True, help='key')
    # 如果连接有问题，需要设置代理，支持http/socks代理，默认无代理
    # http://127.0.0.1:1081
    # socks5://127.0.0.1:1081
    argParser.add_argument('-p', '--proxy', dest='proxy', type=str, help='proxy')
    argParser.add_argument('-t', '--task', dest='task', type=str, help='task', choices=["list_all", "list_one", "create_one", "create_many", "destroy_one", "destroy_many", "destroy_all", "reboot_one", "reboot_all", "update_script", "la", "lo", "co", "cm", "do", "dm", "da", "ro", "ra", "us"])
    args = argParser.parse_args()
    # init manager
    apikey = "you api key here"
    vultrManager = VultrManager(apikey, ssh_keyid=args.ssh_keyid, scriptid=args.scriptid, proxy=args.proxy)
    # run task
    task = args.task
    if task == "list_all" or task == "la":
        vultrManager.getServersInfo()
    elif task == "list_one" or task == "lo":
        vultrManager.getServerInfo(args.sid)
    elif task == "create_one" or task == "co":
        mids = collect_mids()
        vultrManager.createOne(mids)
    elif task == "create_many" or task == "cm":
        mid_s = int(sys.argv[3])
        mid_e = int(sys.argv[4])
        vultrManager.createMany(mid_s, mid_e)
    elif task == "destroy_one" or task == "do":
        mids = collect_mids()
        vultrManager.destroyOne(mids)
    elif task == "destroy_many" or task == "dm":
        vultrManager.destroyMe()
    elif task == "destroy_all" or task == "da":
        vultrManager.destroyAll()
    elif task == "reboot_one" or task == "ro":
        mids = collect_mids()
        vultrManager.rebootOne(mids)
    elif task == "reboot_all" or task == "ra":
        vultrManager.rebootAll()
    elif task == "update_script" or task == "us":
        vultrManager.updateScript()
