Docker
--------
- how can we find in which port  applicaio  is map to?
    1. run the command
      #docker ps -l 	//it will list the last run cointainer only.
    2. Another way to find the post is using 'docker port' command
      #docker port applicaiton_name
    
- with the help of "-e" option we will pass the environment variable to cointainer.
	 Example:
		  #docker run -e "HELLO=VIKASH" ubuntu /bin/bash -c export
   passing the variable at the run time while creating the application
      #docker run  -d -e "REDIS_PORT_6379_TCP_ADDR=172.17.0.3" --name web -p 80:4567 rickfast/orelly-simple-web
      
- cointainer life cycle
    #docker stop --time  10 web	//it will wait for the 10s and then it will stop the application
    
    
- what happen when unexpacted cause a cointainerise process to fail?
    To avoid above, we can use restart policy.
      #docker run --name timebomb -d -p 80:4567 --restart unless-stopped  rickfast/oreilly-time-bomb		
        Note:it will restart the applicaiton once it is exit everytime. The only way to make the cointainer not restart automatically is to explictly  "kill" or  stop the applicatoin.

- by default, the docker takes the latest image
- images is store in the "/var/lib/docker/containers"

Docker File

Docker Build
---------------
- "docker build" command is another way to build the dockre images. it rely on a file called "Dockerfile", which spacify the list of istruction used to bild the docker images. The command that we manully run inside a cointainer to produce an image, can be specified in the "Dockerfile". This gives us sharable, reproducable, and automatable recepic for the building a docker images.

- carating a file using "Dockerfile"

    FROM alpine 			### this is the first instruction for the file. this is for which image we are going to use.
    MAINTAINER  viksh		###this is the maintainer instruction. this indecates the owner of the docker image.
    RUN apk update && apk add nodejs	### it is use to run a command it cointainer
    RUN mkdir average 
    ADD average.js average/				### we can add file from the local matchine to the image
    WORKDIR average			###we can set the current working directory to the "average" working directory
    ENTRYPOINT ["node","average.js"]	###it defines main process will run with the cointaner
	


	#docker build -t vikash/average .	###it will create a docker image. "-t" is use to provide the name of the name of the image
	#docker run vikash/average 3 3 3	###to test the image. now we have image to calculate average

--------------------------------------------------------------
######Docker Example
    we will build the ruby application using the natural frame work and build the docker image cointaing it. The web applicaion was store the count of number of page views in "redis" and display the number of hits on the page.

    1.create the redis cointainer.

    # docker run -d -p 80:6379 --name redis redis

    #vi counter.rb

    require 'sinatra'
    require  'redis'

    set :bind, '0.0.0.0'

    configure do
      $redis = Redis.new(:host => 'redis')
    end

    get '/' do
      count = $redis.incr('count')

      "<h1>Hello O'Reilly!</h1>"\
      "<p> This page has been viewed #{count} times!</p>"
    end


    #vi Dockerfile

    FROM alpine
    MAINTAINER vikash
    RUN apk update && apk add ruby
    RUN gem install sinatra --n0-ri --no-rdoc
    RUN gem install redis --no-ri  --no-rdoc
    ADD counter.rb counter.rb
    EXPOSE 4567
    ENTRYPOINT ["ruby","counter.rb"]

    2. run the docker build command to build the image.

    #docker build -t vikash/counter .

-------------------------------------------------------------------------

-----------------------------------------------------------------------------------------------------
######Pushing the image to the docker hub
--------------------------------------
      1. python applicaiotn


      #vi hello.py

      from flask import Flask
      app = Flask(__name__)

      @app.route('/')
      def hello():
              return 'Hello from Docker Hub!'

      if __name__ == '__main':
              app.run(debug=True,host='0.0.0.0')

      2. Docker file

      #vi Dockerfile

      FROM alpine
      run apk add --update \
              python \
              python-dev \
              py-pip

      RUN pip install flask
      COPY hello.py /
      EXPOSE 8080
      ENTRYPOINT ["python", "hellp.py"]


      3. build the docker image
        #docker build .


      4.tag a image
        #docker tag 387 vikashoo7/hello-dockerhub:1.0		###vikashoo7 - username of the dockerhub
        #docker tag 387 vikash/hello-dockerhub:latest		//it is specified  latest

      5. login to the dockerhub
        #docker login

      6. push the image to the dockerhub
        #docker push vikashoo7/hello-dockerhub
	

--------------------------------------------------------------------------------

Docker Images
---------
- If tag is not mention in the cammand, then it will pull the latest image from the docker hub.
  #docker pull rabbitmq

- run the docker image with the tag
    #docker run -d -p 80:15672 rabbitmq:3.6.12-management
- Building image
    #docker search alpine 		//it will search the images in the docker hub
    1. dowload the base os from the dokcer hub locally.
      #docker pull alpine
    2. there is 2 way to create docker images.
      a. create a image from the running cointainer
      b. create the image automatically from the Dockerfile.
    3. we will be using 2(a), to create the docker images.
    4. run the images into the interactive mode.
      #docker run  -it alpine /bin/sh
    5. After login, update the os and install the 'nodejs'
       #apk update
       #apk add nodejs
       #node --version	//we can very the installation of nodejs
    6. Now we can create a java script application or node applicaiotn and it takes series of number of argument and return its average.
      #mkdir average
      #cd average/
      #vi average.js
        #!/usr/bin/env node
        var sum = 0;
        var count = 0;
        process.argv.forEach(function (val, index, array) {
                if(index > 1) {
                   sum += parseInt(val);
                   count ++;
                }
        });
        console.log(sum /count);
      #chmod +x average.js
      #./average.js
      #./average.js  2 2 2
    7. we can now commit changes to our running cointainer which will create a new image that cointains that cointain new directory and java script file. To commit changes from a cointainer  we need the "container id". Remember, cointaner internal  host name is the cointainer id. so we can the id by simply typing the hostname.
      #hostname
    8. to commit our changes to the cointainer, we can use the "docker commit" comamnd
      #docker commit -m "installed node and wrote application" 877842cfc2d5	
        where: docker commit ecepts a view flag one of is "-m" flag which allow us to commit message for the command.	
    9. test the new image 
      #docker run 2e03 average/average.js 4 4 4 4		//where: 2e03 - in the first few letters of the image id


-------------------------------------------------------------------------------------------------

Dokcer Volume
--------------

	- one way to create the volume is to create "-v" option when executing the docker run
	- date volumes and directory donot used NFS.
	- volumes can also be mounted  to directory on the host machines.
	- When mounting the volume to the localhost machine, we need to suppliy to absolute paths delimited by ":" "absolute path of the base machine:dircetory inside the cointainer to mount"

	- data volume cointainer using the "docker create" command
	- data volume cointainer are  the docker cointainer that dont run a applicaion. They just have the volume that can be shared.
	- "docker create" is very similar to the "docker run" except that the created cointainer is never started.
		#docker create -v /usr/local/var/lib/couchdb --name db-data debian:jessie /bin/true


	- Using volume from the already created volume cointainer
		#doceker run -d -p 5984:5984 -v /usr/local/var/lib/couchdb --name db1 --volume-from db-data klaemo/clouchdb

---------------------------------------------------------------------------------------------------------------------
Docker Network
---------------

- Docker bydefault runs three network on the docker host. we can see there network by running the below comamnd.
		#docker network ls
	1. Default network or bridge network
		Any cointainer running with a bridge network, cannot to access to the outside  docker host unless the host is mapped with "-t" parameter in the docker run.
	2. None network
		its actually nothing.
		to lauch a cointainer on a network other than the deafult bridge the network, we can use the "--net" option in specifying the name of the network to use. eg:
		#
	3.host network
		it is the same networking that the docker host is using.
		in this case, we no need to bound the host with port because it is directly bounding on the host network.
		so if we run 2 applicaiotn with the same port then there wil be the port conflict. Since both dound witht the same host.
			#docker run -d -P --net host --name host-network-app rickfast/hello-oreilly-http

- User defined network
	1.bridge type - basic type of the network. it is similar to 'docker0' or the 'default network'
		a user defined network allows us to create a complietely isolated network on a single machine that a number of cointaner run it. we can easily create a new name bridge netwwork on a docker host. using the 'docker network create' commmand. This command simply accepts the driver type and a unique network name as argument.
			#docker network create --driver bridge my-network

- to launch cointaner with the user defined network, we can specify the network name using the "--net" option with "docker run"
		#docker run -d -P --net my-network --name hello	rickfast/hello-oreilly-http	


--------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------

Docker Compose
--------------
- it uses a yml file that describe multiple cointainer to manage as a cointaier as a whole. 
- There are 2 different specification of the docker-compose-yml file.
- Example1: setting up the cointainer

        version: "2"			#####docker compose specification
        service:			#####service declearation
          kv-store-1:		#####cointainer name 1
            image: redis	#####operatoin perform in the 1st cointainer
          kv-store-2:		#####cointainer name 2
            image: redis	#####operatoin perform in the 1st cointainer


    #docker-compose up 		#####to run the docker file
    #docker-compose up -d 		#####to run the docker compose in the detach mode.
    #deocker-compose rm 		#####it will remove all the cointainer

    Note: if we run the above docker-compose file then it will create 2 cointaner.
	
- Example2: Setting up the cointer and establishing the relation between them. (elk stack)
      version: '2'
      service:
        elasticsearch:
          image: elasticsearch:2.2.1
        kibana:
          image: kibana:4.4.2
          ports:
            - "5601:5601"
          environment:
            - ELASTICSEARCH_URL=http://elasticsearch:9200
          depends_on:
            - elasticsearch
        logstash:
          image: logstash:2.2.2
          command: -e 'input { tcp { port => 5555 }} output {  elasticsearch { hosts => ["elasticsearch:9200"] } }'
          ports:
            - "5555:5555"
          depends_on:
            - elasticsearch
----------------------------------------------------------------------------------------
