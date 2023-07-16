systemctl edit jenkins
sudo systemctl edit jenkins
sudo apt update
sudo apt install openjdk-17-jre
java --version
curl -fsSL https://pkg.jenkins.io/debian-stable/jenkins.io-2023.key | sudo tee   /usr/share/keyrings/jenkins-keyring.asc > /dev/null
echo deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc]   https://pkg.jenkins.io/debian-stable binary/ | sudo tee   /etc/apt/sources.list.d/jenkins.list > /dev/null
sudo apt-get update
sudo apt-get install jenkins
netstat
sudo netstat | grep "java"
sudo netstat | grep "jen"
ps | grep "jen"
sudo ufw allow 8080
sudo ufw allow OpenSSH
sudo ufw enable
sudo ufw status
sudo systemctl status jenkins
whoami
hostname
hostnamectl
pwd
systemctl hostname
hostname
uname
username
hostnamectl
hostnamectl -l
hostnamectl -help
grep "java"
ps
netstat
netstat | grp "java"
netstat | grep "java"
whoami
ssh-keygen -R hostname
