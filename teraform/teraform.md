    SSH into your cloud server
    sudo yum install -y zip unzip (if these are not installed)
    wget https://releases.hashicorp.com/terraform/0.9.8/terraform_0.9.8_linux_amd64.zip
    unzip terraform_0.9.8_linux_amd64.zip
    sudo mv terraform /usr/local/bin/
    Confirm terraform binary is accessible: terraform --version

Terforrm command
----------------
    #terraform init - to initialize terraform this is idempotent
    #terraform apply - to plan then apply out project to AWS
    #terraform destroy - to destroy out project from AWS



Terraform Resources
-------------------
    Resource are a component of your infrastructure. 
    They might be a low level componet like a physical server, virtual machine or container or 
    they could be higher level componetnt like a DNS record or email provider.


Resource Argument & Exported Attributes
----------------------------------------
    Resource have a set of arguments.
      somne are required
      Some are optional

    Resource can have exported attributes
	

    Example of Exported Attributes

      resource "aws_s3_bucket" "my_bucket" {
       bucket = "my-first-bucket"
      }

    The aws_s3_bucket above returns the ARN created as one of its exported attributes


Interpolation Syntax
--------------------

    Interpolcation syntax is a way of having an expression that will be evaluated when terraform runs and replaced with the value.

    For example, you may want the ARN(Amazon Resource Name) of a created AWS object to use in an AWS IAM policy, the ARN is unkown before you create the resource so you can use interpolcation syntax to replace the ARN at runtime.

    To reference an exported attribute from a resource use the interpolation syntax format:
     "${<resource_type>.<resource_name>.<exported_attribute>}"

    For example if we created a resource

      resource "aws_s3_bucket" my_bucket" {
       bucket = "hello-world"
      }

    Reference the created s3 bucket ARN using "${aws_s3_bucket.my_bucket.arn}"


Importance of Inrerpolcation Syntax
-----------------------------------
    Helps Terraform work out dependency order
    Makes refactoring easier as you only have a value a value defined in a single place


Data types
----------
    There are 4 main data types for resource attributes:
      int - defined using - port = 21
      String - defined using - host = "localhost"
      List - defined using - security_groups = ["abc", "def"]
      Bool - defined using - enabled = false



      Example:

            # vi main.tf

            provider "aws" {
              region = "eu-west-2"
            }

            resource "aws_s3_bucket" "my_bucket" {
              bucket = "vikash-myfirst-bucket"
            }

            resource "aws_iam_policy" "my_bucket_policy" {
              name = "my-bucket-policy"

              policy = <<POLICY
            {
              "Version": "2012-10-17",
              "Statement": [
                {
                  "Action": [
                    "s3:ListBucket"
                  ],
                  "Effect": "Allow",
                  "Resource": [
                    "${aws_s3_bucket.my_bucket.arn}"
                  ]
                }
              ]
            }
            POLICY
            }

Terraform Data Sources
----------------------

    Data source allow data to be fetched or computed from external sources such as another Terraform project or a resource that exits on AWS.
    The fetched data can then be used your Terraform project using interpolation syntax.

    data source always stat with the
      data "name of the data source" "name" {
      }

    Example of data source
    ----------------------

      data "aws_db_instance" "database" {
       db_instance_identifier = "my-test-database"
      }

    The data resource above returns many attributes about the database (in this case) that can be used in your terraform project such as the address of the instance, availability zone and instance size.


Using Attribute from a data resource
--------------------------------------
    To use a attribute from a data resource use the formate
      "${data.<resource_type>.<resource_name>.<exported_attribute>}"

    For example if we had the following data source:

      data "aws_s3_bucket" "my_bucket" {
       bucket = "vikash-bucket"
      }

    Reference the s3 bucket ARN using "${data.aws_s3_bucket.my_bucket.arn}"

    lab:
    -----

    #vi main.tf

    provider "aws" {
      region = "ap-south-1"
    }

    data "aws_s3_bucket" "my_bucket" {
      bucket = "vikash-already"
    }

    resource "aws_iam_policy" "my_bucket_policy" {
      name = "my-bucket-policy"

      policy = <<POLICY
    {
      "Version": "2012-10-17",
      "Statement": [
        {
          "Action": [
            "s3:ListBucket"
          ],
          "Effect": "Allow",
          "Resource": [
            "${data.aws_s3_bucket.my_bucket.arn}"
          ]
        }
      ]
    }
    POLICY
    }


Terraform Locals
-----------------
      Terraform Locals allow you to assign a name to an expression, you cvan think of them like a variable
      you can use a local value multuple times with in a module.
      LOcal values can be combined  to make mode local values.
      Locals are created in a locals block, you can have one or more values in a locals bloack and one or more locals in a modules.
      LOcals allow you to define a value in one place and then you can use the local in your project. This means if you change the value of the local you only have to update it in a single place.

      Example:

        locals{
         bucket_name_prefix = "kevin"
         default_instance_tag = "my-instance"
        }
	

Interpolation Syntax for Locals
-------------------------------
    Format for interpolation syntax is "${local.<variable_name>}"
    For example for the local
      locals{
       bucket_name_prefix = "vikash-"
      }

           Would be reference by "${local.bucket_name_prefix}"


Combining Locals
----------------

    locals{
     first = "Vikash"
     last = "kumar"
     name = "${local.first}-${local-last}"
    }

    Name = "Vikash-kumar"


locals As value of Exported Attribute
-------------------------------------

    local can be assigned to the value of an exported attribute from a resource

      resource "aws_s3_bucket" "my_bucket" {
       bucket = "vikash-first-bucket"
      }

      locals{
       bucket_arn = "${aws_s3_bucket.my_bucket.arn}"
      }

    Lab:
    -----

    #vi main.tf

    provider "aws" {
      region = "ap-south-1"
    }

    locals {
      bucket_prefix = "vikash"
    }

    resource "aws_s3_bucket" "my_bucket" {
      bucket = "${local.bucket_prefix}-first-bucket"
    }

Terraform Outputs
-----------------
    Output give you a way to tell Terraform which values are important so Terraform can output them when you run "apply"
    Output can also be used to return values from a modules.
    You can have as many outputs as you want but each output variables has to be given a unique name within a module
    Output are really useful way to log valuable pieces of information back to the user as the IP address of a newly created instance or the DNS name of a load balancer.

    Example:
      output "my_value" {
       value = "hello vikash"
      }

      Output would be : my_value = hello viaksh


    Output can be results of expressions. For example:
      output "my_value"{
       value = "${aws_s3_bucket.mybucket.arn}"
      }
    Output can be values of locals. For example:
      output "my_value" {
       value = "${local.bucket_name}"
      }

    lab:

    # vi main.tf

    locals {
      name = "vikash"
    }

    output "my_name" {
      value = "${local.name}"
    }


Terraform Templates And Files
-----------------------------
    Terraform allows you to use a file as a parameter to a resource
    This can be useful for a big bloack of data e.g. for a config file or a big black JSON for an AWS IAM Policy.
    To use a file's content as the value for a resource attributes you can use the "file" function which is accessible using 
      "${file("<path_to_file>")}"
    For example you could define as AWS IAM user policy like:
      resource "aws_iam_user_policy" "my_bucket_policy"{
       name = "my-bucket-policy"
       user = "vikash-kumar"
      policy = "${file("policy.json")}"
      }

    If you want to have values that change in a file then you can do this using a Terraform template data source.
    Anywhere in your file you can add a placeholder using the syntax
      ${place_holder_name} 
      where place_holder_name is any name you want
    To set the value for the place holders you set them using the vars property on the template data source.

    Example:
    #vi say_hello.tpl

    Hello ${name}

    #vi main.tf
      data "template_file" "say_hello"{
       template = "${file{"say_hello.tpl")}"

       vars{
        name="Vikash"
       }
      }

    Interpolation syntax to get the value 
      "${data.template_file.<name>.rendered}"
      In the above "${data.template_file.say_hello.rendered}"

    Lab:
    ----

    # vi policy.json

    {
      "Version": "2012-10-17",
      "Statement": [
        {
          "Action": [
            "s3:ListBucket"
          ],
          "Effect": "Allow",
          "Resource": [
            "${bucket_arn}"
          ]
        },
        {
          "Action": [
            "s3:GetObject"
          ],
          "Effect": "Allow",
          "Resource": [
            "${bucket_arn}"
          ]
        }
      ]
    }

    --------
    # vi main.tf

    provider "aws" {
      region = "ap-south-1"
    }

    resource aws_s3_bucket "my_bucket" {
      bucket = "kevholditch-bucket"
    }

    resource "aws_iam_user" "kevin" {
      name = "Kevin-Holditch"
    }

    data "template_file" "bucket_policy" {
      template = "${file("policy.json")}"

      vars {
        bucket_arn = "${aws_s3_bucket.my_bucket.arn}"
      }
    }

    resource "aws_iam_user_policy" "my_bucket_policy" {
      name = "my-policy"
      user = "${aws_iam_user.kevin.name}"
      policy = "${data.template_file.bucket_policy.rendered}"

    }

    output "policy" {
      value = "${aws_iam_user_policy.my_bucket_policy.policy}"
    }


Terraform Providers
-------------------

    A terraform providers enables Terraform to talk to an API manage resource.
    For example the AWS terraform provider allows Terraform to talk to and manage resource in AWS

    Terraform allows you to configure multiple providers in a single project allowing you to use resource from multiple places for example  you could configure the AWS, Azure and GCP provider all in a single project allowing  you define resource on multiple clouds in a single project

    Terraform allows you to define a single provider more than once. if you do this you must provide an alias for the second provider.
    Terraform allows you to manage resource that live in multiple AWS accounts in a single project.
    Terraform allows you to create in multiple AWS regions in a single project

    To configure a second AWS provider you need to provide an alias:
      provider "aws" {
       region = "ap-south-1"
       alias = "mumbai"
      }


    As well as setting tyhe region the AWS provider also allows you to set the AWS access key id and AWS secret key on the provider:
      provider "aws" {
       region = "ap-south-1"
       alias = "mumbai"
       access_key = "AAAAA"
       secret_key = "asdfasd"
      }

    This is how you can configure a second provider to point to a different account. Generally through you dont want to put your access key and secret key inline like this as it will cause them to get checked into source control in plan text.

    you can pin a provider to a certain version or add version requirements for a provider. This can be helpful when a bug fix in a certain version of a provider that your Terraform project depends on
      provider "aws" {
       region = "ap-south-1"
       version = "1.8"
      }

      Provider "aws" {
       region = "ap-south-1"
       version = "~>1.8"		##greater than 1.8
      }

    By default if you do not specify a provider on your resource then the default provider will be used (the one with no alias)
    TO tell Terraform to use a fifferent instance of a provider for a resource use the "provider" property with the syntax "<provider_name>.<alias>". for example:
      provider "aws" {
       region = "ap-south-1"
       alias = "mumbai"
      }

      resource aws_s3_bucket "london_bucket" {
       bucket = "london"
       provider = "aws.london"
      }

    lab:
    -----

    #vi main.tf

    provider "aws" {
      region = "ap-south-1"
    }

    provider "aws" {
      region = "ap-southeast-1"
      alias  = "singapore"
    }

    resource aws_s3_bucket "mumbai_bucket" {
      bucket = "vikash-mumbai"
    }

    resource aws_s3_bucket "Singapore_bucket" {
      bucket   = "vikash-singapore"
      provider = "aws.singapore"
    }


Terraform Variables
--------------------
    Variable serve as  parameter to a terraform module
    When used at the top level they enable you to pass parameter into your Terraform project.
    The variable can pass in 3 ways:
      command line
      File
      Environment variables
    3 properties can be defined on a variable:
      Type: (optional) - if this is set it defines the type of the variable, if no type is set then the type of the default value will be used if neither are set then the type will be assumed to be string. Allow values "string", "list" and "map"
      Default: (optional) - if this is set then the variable will take this value if you do not pass one in. if no default value is set and value is not passwd in then Terraform will raise an error
      Description: (optional) - purrely to give the user of the Terraform project some information as to what this variable is used for. Terrform ignores this field.

    Default value of a variable must be a literal value for example 1, "foo" or ["a", "b"]. Interpolcation syntax is not allowed.

    Examples of variable declearations:
      variable "key" {
       type = "sting"
      }

      variable "image" {
       type = "map"

       default = {
        us-east-1 = "image-1234"
        us-west-2 = "image-4567"
       }
      }

      variable "zone" {
       default = ["us-east-1a", "us-east-1b"]
      }


    There may be some properties that are secret and do not want to put in source control, variables gives you a neat way of passing those values into your project as you run Terraform.

    To use the value of a variable in your project you use interpolation syntax of the formate "${var.<variable_name}"
      variable "my_name"{}
       "${var.my_name}"

    Map variable allow you to define values for Terraform to use in different cases for example you could define a map to specify which instances size to use depending on your environment type:
      variable "instance_size_map" {
       type = "map"
         default = {
        dev = "t2.micro",
        test = "t2.medium",
        prod = "m4.large"
       }
      }

    To lookup a map value use the lookup function by:
      "${lookup(<map_name>,<map_key>)}"

      variable "instance_size_map" {
       type = "map"
         default = {
        dev = "t2.micro",
        test = "t2.medium",
        prod = "m4.large"
       }
      }

      variable "instance_size" {}
      "${lookup(var.instance_size_map,var.instance_size)}"

    To set the value of a variable in via the command line use the "--var <name>=<value>syntax
      variable "my_name" {}
       terraform apply --var my_name=vikash

    To set the value of a variable using an environemnt variable, define an environment variable called TF_VAR_<variable_name>
      variable "my name" {}
       env TF_VAR_my_name=vikash terraform apply

    To set the value of a variable using a file, create a file with the extension "tfvars" then give the variable a value using "name"="value"
      variable "my_name"{}
       inside myvalues.tfvars
      my_name = "vikash"

    lab:
    -----

    #vi main.tf


    provider "aws" {
      region = "eu-west-1"
    }

    variable "tag_map" {
      type = "map"
      default = {
        dev	  = "dev-queue",
        test  = "test-queue",
        prod  = "prod-queue"
      }
    }

    variable "env_type" {}

    variable "queue_name" {}

    resource "aws_sqs_queue" "queue" {
      name = "${var.queue_name}"

      tags {
        environment_type = "${lookup(var.tag_map, var.env_type)}"
      }
    }

    #terraform apply --var env_type=dev --var queue_name=myqueue
    #env TF_VAR_env_type=test env TF_VAR_queue_name_name=updatedqueue terraform apply


Project Layout
---------------
    Every project has had a single file called "main.tf"
    Terraform does not mind what you call any file as long as it ends with the ".tf" extension.

    You are also free to break up your resource, variables, data source etc across one or more files as you wish

    Terraform will take every file in  the folder which it is run from that ends in ".tf" and combine it internally.

    Terraform will ignore files in any directory above or below the current one where it is being executed from.

    Example:
      PrajectA/
       main.tf
       s3.tf
       data.txt
       ProjectB/
        snstf
      ProjectC
       sqs.tf/

      So the terraform will look only to the file "main.tf and s3.tf" other than this file, it will ignore rest all other.

Terraform custom Modules
-------------------------

    A modules is a self contained configuration package that can be used to logically group a configuation together.

    You can use a module one or more times in a project making modules an excellent way of packaging up some useful configuration.

    Modules are created by creating a sub folder in your Terraform project and placing your Terraform configutation files in there. Any files in the sub folder will be part of the module.

    Modules can take input parameters it does this by defining variables

    Modules can return values by defining outputs

    Standard Layout
      main.tf - where you place yout terraform configuration (resource, data source etc)
      variables.tf - where you define variables (these will be inputs to your modules)
      output.tf - where you define yout outputs (these will be return by your modules)


    When defining input values for a module we simply define variables as we have learnt. As these variables are defined inside a module Terraform will require you to pass a value for these variables when using the modules.

    To define an instance of a module use the "module" keyword. The source property is required and is used to set the path of where the module is located.
    For example:
      module "queue1" {
       source = "./queue"
       queue_name = "my_queue"
      }

    To make an input parameter to a module optional then simply give the variable a default value. The default value for the variable will then be used if the user does not supply one when referencing the module.

    To reference a file inside a Terraform module you cannot use the relativce path this is because all paths in terraform are assumed to be from the project root

    Therefore, if you want to use a file inside your custom module then you need to use the "${path.module}" to get the path of where your module lives then you can put the path to your file after that for example:
      resource "aws_iam_user_policy" "my_bucket_policy" {
       name = " my-bucket-policy"
       user = "vikash-kumar"
       policy = "${file"${path.module}/policy.json")}"
      }

    To reference an output from a module use interpolation syntax:
      "${module.<module_identifier>.<output_name>}"
      module "queue1" {
       source = "./queue"
       queue_name = "my_queue"
      }
      "${module.queue1.queue_arn}"

Terraform Registry Modules
--------------------------

    A registry module is module that someone else has written and uploaded to the terraform registry

    You can use these pre written modules to very quickly build complex infrastructure setup for example these are modules that can spin up a consul cluster in AWS

    https://registry.terraform.io/

    to reference a terraform registry module, we use below 
      module "user_queue" {
       source = "terraform-aws-modules/sqs/aws"
       name = "user"

       tags = {
        Service = "user"
        Environment = "dev"
       }
      }


Terraform State
---------------- 

Terraform Plan
---------------
    The terraform apply command is multi stage first does a plan then gives you the change to review that plan and apply it.

    You can just do a plan with the apply by running the "terraform plan"

    if you want to apply no matter what then you can use the "-auto-approve" parameter "terraform apply --auto-approve" -not recommended.

    There are 4 different actions Terraform will plan to do with a resource
      create
      change
      change with force recreate (destroy then create)
      Destroy

    At the bottom of the plan Terraform will give you a summary for the total amount of resource to be added, changed and destroyed.

    When an update required the resource to be destroyed and then created both the creation and destroy will be include in the summary. For example, if you were changing one resource that required a recreation then the plan summary would read: 1 to add, 0 to change, 1 to destroy.

    The AWS provider documentation will tell you when changing a field will require a change with force recreate.

    Create - depicted by +
    Change - depicted by ~
    change with force recreate - depicted by -/+
    Destroy - depicted by -

    Lab:
    ----
    example: https://github.com/kevholditch/terraform-course-examples/blob/master/example11/main.tf


Terraform Remote State
-----------------------
    Terraform keeps track of the infrastructure it has created in s state file

    Without ists state file Terraform will not know it has created anything.

    By default Terraform will store state locally in a file called "terraform.tfstate"

    To view Terraform's state you can run the "terraform state show" command


Terraform State
----------------
    Terraform has many different backends available that can store state, making it available remotely.
      s3
      consul

    Using remote state has the advantage that you can share state accross machines making this advisable when working in a team on a terraform project.

    Some terraform state backends additionally provide state locking, meaning thast terraform will ensure that two users cannot modify state at the same time.

    To configure terraform to use remote state create a file called "state.tf" in the root of your project in the following format:
      terraform {
       backend = "terraform-state-bucket"
       key = "project.state"
       region = "eu-west-1"
      } 


Managing Terraform state
-------------------------
    Terraform allows you to manage its state

    You can import existing resource into Terraform's state meaning Terraform will take over the ownership of thaqt resource.

    you can remove resource from Terraform's state to stop Terraform from managing a resource.

    By managing Terraform's state it is possible to import your existing IT infrastructure into Terraform piece by piece.
      create a resource in your Terraform project
      Import the resource into Terrafrom's state
      Run a plan to ensure that terraform does not want to change the resource.

    Each resource is free to implement import differently and in a way that makes sense  for that resource so it is important to consult the documentatiion before importing resource

    In general the command to import a resource is:
      terraform import <resource_path><id>

    To remove an item from terraform's state you can use the "terraform state rm" comamnd:
      terraform state rm <resource_path>




Terraform Workspaces
---------------------

    Terraform allows you to create multiple instances a single project by using Terraform workspace.

    You can think of a Terraform workspace as a complete separate copy of you Terraform satate file.

    You can use Terraform workspace to manage multiple environemnts from a single Terraform project e.g. dev, staging and production.    

    To get access to Terraform workspace you have to be using one of the following  state backends:
      AzureRM
      Consul
      GCS
      Local(default)
      Manta
      S3

    Every Terraform project has at least one workspace

    When Terraform initialises it creates a workspace called "default" which you will have been working in uo until now

    The default workspace is always there and connot be deleted

    To create a new Terraform workspace:
      terraform workspace new <name>

    When you run the command it will create a new workspace and instantly switch you into it.

    To list all available workspaces
      #terraform workspace list
        default
        *dev
      The "*" indicates the currently selected workspace.

    To switch workspace
      #terraform workspace select <name>

    To delete a workspace
      #terraform workspace delete <name>

    Note you will need to perform a "terraform destroy" before delecting the workspace

    To use the current workspace to make decisions you can use the current workspace in interpolation syntax:
      "${terraform.workspace}"

    Lab:
    ----

    #vi main.tf

    provider "aws" {
      region = "eu-west-1"
    }

    data "aws_ami" "image" {
      most_recent = true
      filter {
        name = "name"
        values = ["amzn-ami-hvm-????.??.?.????????-x86_64-gp2"]
      }
      filter {
        name = "root-device-type"
        values = ["ebs"]
      }
      owners = ["amazon"]
    }

    resource "aws_instance" "web" {
      ami           = "${data.aws_ami.image.id}"
      instance_type = "t2.micro"

      tags {
        Name = "WebServer-${terraform.workspace}"
      }
    }

    output "instance_ip" {
      value = "${aws_instance.web.public_ip}"
    }

    #terraform init
    #terraform apply
    #terraform workspace list
    #terraform workspace new qa
    #terraform workspace list
    #terraform apply
    #terraform workspace select default
    #terraform delete qa			###error will show while deleteting
    #terrafrom workspace select qa
    #terraform destroy
    #terraform workspace select default
    #terraform workspace delete qa



Resource Meta Parameters
------------------------
    All Terraform resource have the following 4 parameters defined on them:
      count
      depends_on
      provider
      lifecycle

    The count attribute tells Terraform how many of a resource to create. you can use this to create multiple copies of a resource.
      resource "aws_instance" "web" {
       ami = "${data.aws_ami.image.id}"
       instance_type = "t2.micro"
       count = 3
      }

    For some resource you will not be able to create multiple copies by simply increasing the count e.g. an s3 bucket as you cannot create more then one bucket with the same name.

    To get around this you can use the count by using the interpolation syntax "${count.index}" to give you the count for that instance. you can than use this in your attributes to make each instance unique
      resource "aws_s3_bucket" "bucket" {
       bucket = "vikash-${count.index}"
       count = 2
      }

    Count is also useful for not creating a resource under certain conditions by setting the count to 0

    You many not want to create a database backup for your dev environemnt.

    The depends_on attributes allow you to specifically tell teraform tha this resource depends on another resource
      resource "aws_s3_bucket" "bucket2" {
       depends_on = ["aws_s3_bucket.bucket"]
      }

    Generally you should use interpolation syntax where possible to let Terraform work out the dependency order for resources. However, there are some senarios where Terraform cannot work out the dependency order so you can use the "depends_on" attribute to enforce a dependency.

    The provider attributes allows you to specify that this resource is created with a certain provider

    If you only have one instance of a provider then this can be omitted but when you have multiple instances of a provider and you want to use the non default instance you have to set the provider attribute.
      provider "aws" {
       region = "eu-west-2"
       alias = "london"
      }
      resource aws_s3_bucket "london_bucket" {
       bucket = "london"
       provider = "aws.london"
      }


    The lifecycle attributes lets you change the way that terraform updates, destroys ot change the resource
      create_before_destroy - for example create the new DNS record before removing the old one
      prevent_destroy - extra safety guard to prevent the destruction of a resource
      ignores_change-specified as a list to allow you to ignore certain resource attributes that may change which you want Terraform to ignore.


    lab:
    -----
    provider "aws" {
      region = "eu-west-1"
    }

    resource "aws_s3_bucket" "bucket" {
      bucket = "kevholditch-${count.index}"
      count = 3
    }

    resource "aws_s3_bucket" "bucket2" {
      bucket = "kevholditch-next-bucket"

      depends_on = ["aws_s3_bucket.bucket"]
    }
