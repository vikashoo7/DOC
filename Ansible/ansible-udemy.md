Inventory
--------
    - Ansible hosts file follow the below hyarchy followed by most to the least.
      1. directory from where rwe are running the playbook
      2. environemnt variable
      3. ansible host file

    - Running ansible using super user. use below variable in the inventory file
        [server]
        server1	ansible_become=true	ansible_become_pass=<password>

    - To connect to the host with a specific port. edit the inventoy file and add the host variable "ansible_port"
        [server]
        server1	ansible_become=true	ansible_become_pass=<password> ansile_port=<port_number>

    - To run the ansilble to a specific user. edit the inventory file and add the variable "ansible_user"
        [server]
        server1	ansible_become=true	ansible_become_pass=<password> ansile_user=<user_name>

    - #ansible all --list-hosts	##list all the hosts in the host file

    - we can declear variable saparately and then include in the hosts file
        [centos]
        server1 ansible_port=2222
        server2

        [centos:vars]
        ansible_user=root

        [ubuntu]
        server3
        server4

        [ubuntu:vars]
        ansible_become=true
        ansible_become_pass=password


    - we can declear the variour group under a group in terms of children.
        [centos]
        server1 ansible_port=2222
        server2

        [centos:vars]
        ansible_user=root

        [ubuntu]
        server3
        server4

        [ubuntu:vars]
        ansible_become=true
        ansible_become_pass=password

        [linux:children]
        centos
        ubuntu

    - we can set variable for all the host globally.
        [centos]
        server1 ansible_port=2222		##it will over write the global variable port and take it as port=2222 
        server2

        [centos:vars]
        ansible_user=root

        [ubuntu]
        server3
        server4

        [ubuntu:vars]
        ansible_become=true
        ansible_become_pass=password

        [linux:children]
        centos
        ubuntu

        [all:vars]
        ansible_port=1234
	

    - Host file can be written in the json or yaml formate.

Ansible Module
---------------
    setup module - Used for gathering facts when executing playbooks.
    file module - Used for file, symlinks and directory manipulation
    Idempotency - An operation is idempotent if the result of performing it once is exactly the same as the result of performing it repeatedly without any intervening action.
    copy module - Used for copying files, from the local or remote, to a location on the remote.
    fetch module - Used for copying files, from the remote locaiton to the local box.
    Command Module - Used for execute remote commands. it is the default madule that is used for ansible Ad hoc command.
    rc (return code) - it tells if a command is successful or not. 0 - means the command is successful.
    To check the information  about the ansible document.
      $ansible-doc <module name>

YAML (Yet another markup languag)
-------
    it will start with '---' and end with '...'


Ansible Playbooks, Breakdown of Sections
-----------------------------------------------------------
    - gather_facts: false	####stop gathering the facts

    - we can pass the variable in command line with "-e" and "--extra-vars="varaiable1=value1" option.
      #ansible-playbook playbook.yml -e "variable=value"
      #ansible-playbook playbook.yml --extra-vars="variable=value"

    - Handlers - it executed as a notify key from the task

Ansible Playbooks, Variables
------------------------------

    - Defining the variable using dictonary
        vars:
          dict:
            dict_key: This is a dictionary value

        tasks:
          - name: list all the entire dictornay 
            debug:
              msg: {{ dict }}

          - name: prining the specific value from the dictonary variable with dot notation
            debug:
              msg: "{{ dict.dict_key }}"

          - name: print the specific value from the dictonary variable with bracket notation
              debug:
                msg: "{{ dict['dict_key'] }}"

    - Defining the "inline_dict"
        vars:
          inline_dict:
            {inline_dict_key: This is a dictionary value}

        tasks:
          - name: list all the entire dictornay 
            debug:
              msg: {{ inline_dict }}

          - name: prining the specific value from the dictonary variable with dot notation
            debug:
              msg: "{{ inline_dict.inline_dict_key }}"

          - name: print the specific value from the dictonary variable with bracket notation
              debug:
                msg: "{{ inline_dict['inline_dict_key'] }}"

    - Definign the list in the variable section
        vars:
          named_list:
            - item1
            - item2
            - item3
            - item4


        tasks:
          - name: list all the entire list
            debug:
              msg: {{ named_list }}

          - name: prining the specific value from the list variable with dot notation
            debug:
              msg: "{{ named_list.0 }}"

          - name: print the specific value from list variable with bracket notation
              debug:
                msg: "{{ named_list[0] }}"

    - Defining the "inline_named_list"
        vars:
          inline_named_list:
            [ item1, item2, item3, item4 ]

        tasks:
          - name: list all the entire list
            debug:
              msg: {{ inline_named_list }}

          - name: prining the specific value from the list variable with dot notation
            debug:
              msg: "{{ inline_named_list.0 }}"

          - name: print the specific value from list variable with bracket notation
              debug:
                msg: "{{ inline_named_list[0] }}"

    - Accessing the variable from the external file

        vars_files:
          - external_vars.yml


        tasks:
          - name: print the external variable key value
            debug:
              msg: {{ external_example_key }}

          - name: test the external named dictonary 
            debug:
              msg: "{{external_dict }}"

          - name: est the external named dictonary with dictonary dot notation
              debug:
                msg: "{{ external_dict.dict_key }}"

          - name: est the external named dictonary with dictonary bracket notation
              debug:
                msg: "{{ external_dict[dict_key] }}"

        external_vars.yml
        ---
        external_example_key: example value

        external_dict:
          dict_key: This is dictionary value

        external_inline_dict:
          {inline_dict_key: This is an inline dictionary value}

        external_named_list:
          - item1
          - item2
          - item3
          - item4
          - item5

        external_inline_named_list:
          [ item1, item2, item3, item4 ]

    - Prompt a variable at run time
        vars_prompt:
          - name: username
            private: false	##this parameter makes input visible on the screen

        tasks:
          - name: print the username
            debug:
              msg: "{{ username }}"

    - Getting variable information using "gather_facts"
        * hostvars - anisble variable for getting the host value
        * ansible_host - provide the hostname of the server
        * ansible_port - provide the port of the server

        task:
          - name: hostvars with an ansible_fact and and colelct ansible_port using dot notation
            debug:
              msg: "{{ hostvars[ansible_hostname].ansible_port }}"

          - name: hostvars with an ansible_fact and and colelct ansible_port using bracket notation
            debug:
              msg: "{{ hostvars[ansible_hostname]['ansible_port'] }}"

          - name: hostvars with an ansible_fact and and colelct ansible_port using dot notation using filter
            debug:
              msg: "{{ hostvars[ansible_hostname].ansible_port | default('') }}"	##"|" is a filter. "default" is the filter type. if no value for the vaiable then it will go through the filter and print empty string.

    - Group variable defined in the host file can be accessed directly.


 Ansible Playbooks, Facts
---------------------------

      - under the "setup" modules
          ansible_facts - anything comes under this variable is belongs to 'root'

      - Custom Facts
          it can be written in any language and returns a JSON structure or any structure.
          it returns an INI structure
          By default, Ansible expacts custom facts under "/etc/ansible/facts.d"

        - ansible_local - under this section all the custom facts data store in setup module.
            tasks:
              - name : show Custom fact'
                debug:
                  msg: "{{ ansible_local.getdata1.date }}"		##'getdata1' is the custom script present in '/etc/ansible/fact.d/getdata1.fact'. 'date is value of the script in the dictonary formate. This custom facts script should be availabe on all the server as per above mention directory.


Templating with Jinja2
----------------------

    - template example
        tasks:
          - name: Jina2 if statement
            debug:
              msg: >			## > - provide multiple line message
                --== Ansilble Jinja2 if statement ==--		##Saparate from the code

                {# if the hostname is myHostName, include a message -#}	## jina2 starts with "{". "-" at the end of the line strip the new line.
                {% if ansible_hostname == "myHostName" -%}
            This is myHostName
                {% elif ansible_hostname == 'otherHost' -%}
                  This is the other host
                {% else -%}
                  This is the host anme {{ ansible_hostname }}
                {% endif %}

    - Defined a variable
        tasks:
          - name: Jina2 if statement
            debug:
              msg: >			## > - provide multiple line message
                --== Ansilble Jinja2 if statement ==--		##Saparate from the code
                {% set example_variable = 'myValue' -%}

                {% if example_variable is defined -%}
            example_variable is defined
                {% else -%}
                  example_variable is not defined
                {% endif %}

    - For loop
        tasks:
          - name: Jina2 if statement
            debug:
              msg: >			## > - provide multiple line message
                --== Ansilble Jinja2 if statement ==--		##Saparate from the code

                {% for entry in ansible_all_ipv4_address -%}
            IP Address entry {{ loop.index }} = {{ entry }}
                {% endfor -%}



Ansible Playbook Modules
-------------------------

    - Add the fact dynmically.
        tasks:
          - name: My fact
            set_fact:
              our_fact: My custsom fact!!


          - name: display the fact
            debug:
              msg: "{{ our_fact }}"

    - Override the existing facts
        tasks:
          - name: My fact
            set_fact:
              our_fact: My custsom fact!!

          - name: display the fact
            debug:
              msg: "{{ our_fact }}"
              ansible_distribution: " {{ ansible_distribution | upper  }}"

    - pause module - it will pause the ansible execution for given time.
        tasks:
          - name: pause the playbook for 10 sec
            pause:
              seconds: 10

    - prompt module - it is helpfule when some task need to varify manually. it will prompt to countinue or abort.
        tasks:
          - name: prompt uesr to verify before countinue
            pause:
              prompt: check the user. Press enter the to continue.

    - wait_for module- wait for scpecific time time
        tasks:
          - name: wait for the webserver to be running on port 80
            wait_for:
              port: 80

    - ansible-doc module_name: provide the detail information about the module

    - assemble module - it allow the collection of file asseble into one file
        tasks:
          - name: Assemble conf.d to sshd_config
            assemble:
              src: conf.d
              dest: sshd_config

    - add_host module - it will allow us to dynamically add host to a subsequent playbook
        tasks:
          - name: Add the server1 to the exisitng group
            add_host:
              name: server1
              groups: existing_group1, existing group2
        hosts: existing_group1
        tasks:
          - name: ping all existing_group1
            ping:

    - group_by - this allow us to add a group based on key
        tasks:
          - name: Create group based on ansible_distribution
            group_by:
              key: "custom_{{ ansible_distribution | lower }}

        hosts: custom_server1
        tasks:
          - name: ping all custom_server1
            ping:

    - fetch module - it allow to access the remote file
        tasks:
          - name: fetch /etc/redhat-release
            fetch:
              scr: /etc/redhat-release
              dest: /tmp/redhat-release


Dynamic Inventories
--------------------

register and when
------------------
