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
