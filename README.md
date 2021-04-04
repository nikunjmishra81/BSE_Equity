# BSE_Equity


# BSE_Equity

__This Project will fetch Equity data on daily basis from BSE Site https://www.bseindia.com/markets/MarketInfo/BhavCopy.aspx

* Requirements To run this project You need 

	1. Windows/Ubuntu instance
	2. Docker and docker-compose Installed
	3. Git Installed

* To install Docker

	On windows
	
		1. You can directly download from Docker site https://hub.docker.com/editions/community/docker-ce-desktop-windows/
		
		2. Docker compose is attached with docker while downloading from windows
		
	
	On ubuntu
	
		1. sudo apt update
		
		2. sudo apt install docker.io
		
		3. To check installed or not use command
			docker --version
			& output should be
			Docker version 19.03.8, build afacb8b7f0
		
		4. sudo systemctl status docker(docker is stopped now)
		
		5. sudo systemctl start docker
		
		6. sudo systemctl status docker
			Loaded: loaded (/lib/systemd/system/docker.service; disabled; vendor prese>
			
			Active: active (running) since Sun 2021-04-04 11:28:14 UTC; 5s ago
			
			TriggeredBy: ● docker.socket
			
			Docs: https://docs.docker.com
			
			Main PID: 15092 (dockerd)
			
			Tasks: 8
			
			Memory: 43.2M
			
			CGroup: /system.slice/docker.service
			     └─15092 /usr/bin/dockerd -H fd:// --containerd=/ru

* To install docker-compose
		
	on ubuntu
	
		1. sudo curl -L "https://github.com/docker/compose/releases/download/1.25.5/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose

		2. sudo chmod +x /usr/local/bin/docker-compose

* To Install git
	On Windows
	
		1. You can directly download from https://git-scm.com/downloads
	On Ubuntu 	
		
		1. sudo apt update 

		2. sudo apt install git

		3. To check installed or not use command
			git --version
			& output should be like
			git version 2.17.1


* To Run this project as follows


		1. Clone the git repo using:

			* git clone https://github.com/nikunjmishra81/BSE_Equity.git

		2. Make sure docker & docker-compose is Up & running
		3. Make sure port 80 of server is open
		4. Hit the below commands in CMD or terminal(ignore first command if not using ubuntu)
			* sudo su
			* cd  BSE_Equity
			* docker-compose up -d
		5. Once the containers gets build up, You can see below image
			![image](https://user-images.githubusercontent.com/35936741/113508640-cb9df500-956e-11eb-868a-8ce3faddf7c3.png)

			

![image](https://user-images.githubusercontent.com/35936741/113508670-eec8a480-956e-11eb-8338-878286d9389d.png)
		
		6. Just check that 4 containers(named as redis, scheduler, frontend, backend) are up and running using command
			* docker ps
			You can see below image
			
			![image](https://user-images.githubusercontent.com/35936741/113507869-942d4980-956a-11eb-9e55-9d6935e2343f.png)
![image](https://user-images.githubusercontent.com/35936741/113508619-ba54e880-956e-11eb-9920-9b199f6268b3.png)


		7. Once the 4 containers are up, Check the Port 80 on your machine
		8. If you need to apply SSL, you can use nginx file present in "simple-vuejs-app/nginx"


* __Note : 
* __If You get error like this for redis, frontend, backend, scheduler
	* Service 'frontend' failed to build: Get https://registry-1.docker.io/v2/: EOF
	* hit the command again
		docker-compose up -d
		
* __In Case you are using an ubuntu system and containers don't goes up, or create some issue, you need to do proper volume mapping in docker compose file. To do so:
	
	
	> Search for "./django_cache" , It has 4 occurrences
	
	> Replace it with actual path of folder i.e. "<base_path>/BSE_Equity/django_cache"
	
	> Search for "./simple-vuejs-app" , It has 2 occurrences with nginx
	
	> Replace it with actual path of folder i.e. "<base_path>/BSE_Equity/simple-vuejs-app"

* ___Scheduler will run daily at 6:10PM IST and will fetch the data
