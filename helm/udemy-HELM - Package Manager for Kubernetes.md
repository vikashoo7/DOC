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
	- Template functions
	- Template functions
