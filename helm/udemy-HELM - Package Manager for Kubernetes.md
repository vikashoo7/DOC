Introduction
-------------	
	- In Helm 3, Tiller is removed and access id provided by RBAC.
	- Public Repository - https://helm.sh
	- list all the charts in the public hub
		#helm search hub
	- search for a specific Charts in the hub
		#helm search hub <chart-name
		#helm search hub mysql 				###example
	- Add the repository to helm
		#helm repo add <repository-name> <URL>
		#helm repo add stable https://kubernetes-charts.storage.googleapis.com/		#Example
	- Searchh the repository
		#helm search repo stable
	- List all the repository
		#helm repo list
	- Search for a chart in a repository
		#heml search repo <repository-name>/<Chart-Name>
		#helm search repo stable/mysql					#Example
	- Update the repository
		#helm repo update
	- Install the helm charts
		#helm install <repository-name>/<Charts-name>
		#helm install stable/mysql --generate-name		##Generate a name for the installation
	- List of the charts that is deployed to the K8s
		#helm ls
	- Delete a specific Chart
		#helm uninstall <chartname>
		#helm uninstall mysql
		
Installing the helm
------
	get the desired version from this URL - https://github.com/helm/helm/releases
	#tar -zxvf helm-v3.6.2-linux-amd64.tar.gz
	#mv linux-amd64/helm /usr/local/bin/helm
	#helm version				##tell the version of the helm
	
Create new helm chart
------------------------
	- Create a new chart
		#helm create <chartname>
		#helm create mychart
	- This will create the following diretory structure
		charts -> A directory containing any charts upon which this chart depends.
		Chart.yaml -> This will contain information about the charts
		templates -> A directory of template that, when combined with values will generate valid Kubernetes manifest files.
		values.ymal -> this will provide the values for the template. This is the default configuration values for this chart
		values.schemas.json -> This is optional file. it is a JSON schema for imposing a structure on the values.yaml file
		crds -> Custom Resources Definaitions


Template
----------
	- Install a chart
		#helm install <name-of-chart> <location of chart resource>
		#helm install helm-demo ./mychart			##Example
	- Uninstall the charts
		#helm uninstall <name-of-chart>
		#helm uninstall helm-demo
	- Built-in objects
		* we use {{ }} -> to get the value 
		* There are 2 ways we can get the value for template
			1. values file
			2. with builtin objects which can provide the value.
		* There are number of built in objects present. we can get it from the documentation
		* DOC URL -> https://helm.sh/docs/chart_template_guide/builtin_objects/
		* To get the details of deployed manifest file
			#helm get manifest <manifest-name>
			#helm get manifest releasename-test
	- Read values for templates
		* Mention the variables in the "value.yml" file in the key value pair.
			#vi value.yaml
				myvar: myvalue
		* calling the variable variable in the template
			#vi template/configmap.yml			
			data
			  newValue: {{ .Values.myvalue }}
		* Dry Run the Release
			#helm install --debug --dry-run <path-to release> <path to the chart>		##This will generate the manifest file
			#helm install --debug --dry-run firstrelease ./mychart
		* Set a specific value at run time
			#helm install --debug --dry-run --set cost=33333 firstrelease ./mychart
	- Template functions
		* There are n number of pre-defined functions available as part of go template.
		* URL -> 
			https://godoc.org/text/template
			https://masterminds.github.io/sprig/
		* Example
			i) #vi values.yml
				projectCode: aazzxxyy
				infra:
			 	 zone: a,b,c
			 	 region: us-e
			ii) then call the these values in the template/helmTemplaste.yml
			#vi template/helmTemplaste.yml
				Zone: {{ quote .Values.infra.zone }}
				Region: {{ quote .Values.infra.region }}
				ProjectCode: {{ upper .Values.projectCode }}

			Note: quote, upper -> is the pre defined template.
			iii) then run the below command to install
				#helm instal --debug --dry-run helm-poroject ./mycharts
	- Template pipeline and default
		* pipeline ->Same link linux concept
		* Example
			pipe: {{ upper .Values.projectCore | quote }}
			now: {{ now | date "2016-01-02" | quote }}
		* default -> This will list the default vaule
		* Example
			contact: {{ .Values.contact | default "1800-19-21-22" | quote }}
				if contact is not defined or there is no output for contacts then "1800-19-21-22" will take the value by default
	- Control flow if-else
		* Syntax:
			{{ if PIPELINE }}
			  # Do Something
			{{ else if OTHER PIPELINE }}
			  # Do something else
			{{ else }}
			  # Default case
			(( end }}
		* A pipeline is evaluated as false if the value is:
			1. A Boolean false
			2. A numeric zero
			3. An empty string
			4. A nil (empty or null)
			5. An empty collection(map, slice, tuple, dict, array)
		* Example:
			{{ if eq .Values.infra.region "India" }}ha: true {{end}}
			{{- if eq .Values.infra.region "India" }}
			ha: true 
			{{end}}
				"-"-> is used to remove the new line
	- Defining scope using with
		* modifying scope using with
		* the value evaluated within that specific block
		* Syntax
			{{ with PIPELINE }}
			  # restricted scope
			{{end}} 	
	- Range
		* looping using range
		* syntax
		lang Used: |-
		  {{-range.Values.LangUsed}}
		  - {{ .|title|quote }}
		  {{-end}}

		* whereas
		LangUsed:
		  - python
		  - Jave
  		  - go

	- variables
		* variables will start with "$" and asigned with a special assignment operator ":="
		* Variable will have the scope accross the template
		* Eg: {{ - $relname := .Release.Name -}}
	- Include content from same file
		* starting with "_" may not have manifest.
		* Example
			{{- defin "mychart.labels"}}
			labels:
			  generate: helm
			date: {{now|htmlDate }}
			{{-end}}
			{{-template "mychart.lanels"}}
	- Include scope
		* Template as a part of saparate file and include in another template.
		* Example:
		i) #vi _helpers.tpl
			{{- define "mychart.systemlables" }}
     			labels:
       			  drive: ssd
       			  machine: frontdrive
       			  rack: 4c
       			  vcard: 8g
			  app.kubernetes.io/instance: "{{ $.Release.Name }}"
			  app.kubernetes.io/version: "{{ $.Chart.AppVersion }}"
			  app.kubernetes.io/managed-by: "{{ $.Release.Service }}"
   			{{- end }}
			
		ii) Passing the scope. So that the value of the current template will populate to the template.
			{{- template "mychart.systemlables" . }}
			{{- template "mychart.systemlables" $ }}
		iii) Run the helm
			helm install --dry-run --debug templatedemo ./mychart
	- Include template using keyword include
		* Include provide additional option of mentioning how much indentation I wanted for particular template.
		* Eg: {{ include "mychart.version" . | indent 4 }}
	- Notes
		* notes.txt contains note for the file and other helper templates within it. we can give instruction on what are all the notes that should get displayed once the chart is dosplayed.
		* This act as another template where the normal template syntax can be included within the notes as well.
	- Sub Charts
		* it is chart under chart.
		* Creating the sub Chart
			#cd <chartname>/charts
			#helm create <sub-chart-name>		##this will create a charts directory under the existing chart
			#cd mycahrt/charts && helm create subchart		##Example
	- Sub Chart global
		* it is used to provide the same value accross all the cahrts and subcharts.
		* Define the value in the "value.yml" file in the manin charts with the "global" keyword.
		* Example:
			global:
			  orgdomain: com.example
			  
Repository Management
-------------
	- Repository Workflow
		* Chart Repositories
			1) An HTTP server hosting index.yaml file along with chart packages
			2) When charts are ready, can be uploaded to the server and shared
			3) Multiple charts with dependency control system in a common location
			4) can be hosted as part of
				i) Google Compute Cloud Bucket
				ii) AWS S3 Bucket
				iii) Github Pages
				iv) Own webserver(chartmuseum)

	- Chartmuseum installation
		* COD URL -> https://chartmuseum.com/docs/
		* follow the below steps for installation
			#curl -LO https://s3.amazonaws.com/chartmuseum/release/latest/bin/linux/amd64/chartmuseum
			#chmod +x ./chartmuseum
			#mv ./chartmuseum /usr/local/bin
			#chartmuseum --version		##display the version

		* Creating the chartmuseum locally
			# chartmuseum --debug --port=8080 --storage="local" --storage-local-rootdir="./chartstorage"
			note: "chartstorage" -> this is storage for charmuseum

		* Access the below link if chartmuseum installed successfully
			https://<server-name>:8080

	- Add Chartmuseum repository
		# helm repo list	##List the repository
		# helm repo add <name-of-repository> http://<server-ip>:8080	##Add the repository
		#helm repo add chartmuseum http://localhost:8080	##Example
		#helm search repo nginx		##this will search for the nginx in the helm repository
		#helm search repo <repository-name> ###list all the package of the repository

	- Add Chart to Chartmuseum repository 
		* Create a plugin to add the charts to the repository
			#mkdir helm_demo_repo
			#cd helm_demo_repo
			#helm create repotest		###create the charts
		* Push the charts to the repository	
			Add the files under the repotest
			#helm package repotest		###package the charts
			#curl --data-binary "@<package-name-from-above" http://<server-ip>:8080/api/charts
			#curl --data-binary "@repotest-0.1.1.tgz" http://192.168.0.52:8080/api/charts	##Example
			#helm repo update		##update the repository with the latest package
			#helm search repo <repo-name>	##list all the charts in the repository

	- Maintain Chart version
		* URL-> https://semver.org/ -> tells about the versioning
		* The version information will mention in the "Chart.yml"
		* we need to mention version in 2 placces.One is for chart and other is for application.
		* Package the chart
			#helm package repotest/
		* Add the chart to the repository
			#curl --data-binary "@repotest-0.1.1.tgz" http://localhost:8080/api/charts
		* list the chart
			#helm repo update
			#helm search repo <repo-name>
			# helm search repo -l <repo-name>		##list all version of the chart

	- Chart push plugin
		* Run the below command to install
			#helm plugin install https://github.com/chartmuseum/helm-push.git
		* List all the helm plugin
			#helm plugin list
		* Push the charts in the repository
			#helm push <chart-directory> <repository-name>
			#helm puch helmpushdemo/ mychartmuseumrepo

	- Maintain github as repository
		* Create a repository to the git
		* package the repository 
		* create the index file
			#helm repo index .
		* Commint everything to the git now
		* Chartmuseum automatically generate the index.yml file once we add the zipped content to the storage location.

	- Add Charts to github repository
		* run the below command
			#helm repo add --username myusername@gmail.com --password <<acccess token>> <repo-name> 'https://raw.githubusercontent.com/muthu4all/helm_git_repo/master'
			#helm search repo <repo-neme>
		* Now i can add any number of charts in the git. Whenever we are upadting the charts, we need to update the index.yml also
		* Add another charts
			#helm create gitrepotest2
			#cd gitrepotest2
			#helm package /root/helm_demo/gitrepotest2
			#helm repo index .
			#commit this to the repository
