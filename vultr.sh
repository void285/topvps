##### init set
cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
##### install
apt-get update
apt-get -y upgrade
apt-get install -y gcc tmux vim git python-dev python-pip
pip install shadowsocks
pip install requests
##### dirs
cd /root
##### ssh
#    pem
wget http://example.com/skey.txt
mv skey.txt your_key.pem
chmod 0400 your_key.pem
#    config
wget http://example.com/sshconfig.txt
cat sshconfig.txt > ~/.ssh/config
rm sshconfig.txt
#    known_hosts
wget http://example.com/knownhost.txt
cat knownhost.txt > ~/.ssh/known_hosts
rm knownhost.txt
##### start ss
# 如果是要自动连接
# wget http://example.com/sslocal.txt
# mv sslocal.txt sslocal.json
# sslocal -c sslocal.json &

# 如果要自动开启shadowsocks服务
wget http://example.com/ssserver.txt
mv ssserver.txt /etc/shadownsocks.json
ssserver -c /etc/shadowsocks.json -d start
