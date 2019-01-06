# Item-Catalog
This is a project for Udacity's [Full Stack Web Developer Nanodegree](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd004)

This is simple web application that provides a list of items within a variety of categories and integrate third party user registration and authentication. Authenticated users have the ability to add, edit, and delete their own items.

## Set Up
1. Install [Vagrant](https://www.vagrantup.com/)
2. Install [VirtualBox](https://www.virtualbox.org/)
3. Download the vagrant setup files from [Udacity's Github](https://github.com/udacity/fullstack-nanodegree-vm)
4. Download this project and unzip it into the vagrant folder

## 2. Start VM
1. Open the terminal and navigate to the vagrant folder
2. cd into vagrant and run ``` vagrant up ``` to start the VM
3. Once done, run ``` vagrant ssh ``` to connect
4. Navigate to `cd/vagrant` as instructed in terminal
5. Setup application database `python /item-catalog/database_setup.py`
6. *Insert fake data `python /item-catalog/add_fake_data.py`
7. Run the application using `python /item-catalog/application.py`
8. Access the application locally using http://localhost:8000

## JSON Endpoints
The following are open to the public:

 `/api/v1/components.json`
    - Displays JSON of all the parts in the component.

 `/api/v1/components/<int:component_id>/part/<int:part_id>/JSON`
    - Displays JSON of a particular part in the component

 `/api/v1/components/JSON`
    - Displays JSON of all the components in the components.