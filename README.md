# BSE_Equity


# BSE_Equity

This Project will fetch Equity data on daily basis from BSE Site https://www.bseindia.com/markets/MarketInfo/BhavCopy.aspx

Requirements To run this project

1. Windows/Ubuntu instance
2. Docker and docker-compose Installed
3. Git Installed

Steps to Run this project as follows


1. Clone the git repo using:
	
	git clone https://github.com/nikunjmishra81/BSE_Equity.git

2. Make sure docker & docker-compose is Up & running
3. Go inside BSE_Equity folder and make sure it has all permissions set(chmod 777)
4. Hit the command in CMD or terminal
	
	docker-compose up -d
5. Containers Going up will take sometime. Once it gets completed, Just check that 4 containers(named as redis, scheduler, frontend, backend) are up and running using command
	
	docker ps
6. In Case you are using an ubuntu system and containers don't goes up, or create some issue, you need to do proper volume mapping in docker compose file. To do so:
	
	
	a. Search for "./django_cache" , It has 4 occurrences
	
	b. Replace it with actual path of folder i.e. "<base_path>/BSE_Equity/django_cache"
	
	c. Search for "./simple-vuejs-app" , It has 2 occurrences with nginx
	
	d. Replace it with actual path of folder i.e. "<base_path>/BSE_Equity/simple-vuejs-app"
	
7. Once the project is up, Check the localhost:80 on your machine
8. If you need to apply SSL, you can use nginx file present in "simple-vuejs-app/nginx"
