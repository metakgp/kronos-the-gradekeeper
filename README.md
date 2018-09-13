# Grim_Reaper


This webapp displays previous year's grade distribution. It has been deployed on heroku as an app and is funcitonal.

You can go [here](https://kronos.metakgp.org) for the live version of the project.

## Installation guide

Python packages required:


- Install flask: `pip3 install Flask`

- Install PIL: `pip3 install Pillow`

- Install matplotlib: `pip3 install matplotlib`

- Install json: `pip3 install json`

## Running the app

* Commands for running flask:
  ```
  export FLASK_APP=app.py
  python3 app.py
  ```

* In a web browser, open link: http://localhost:5000/


## Example
![Example](https://github.com/metakgp/Kronos/blob/master/Kronos.gif)


# Updating / Adding new grades from erp

## Installation guide

- Install json: `pip install json`

- Install regex/re  : `pip install regex`

## Running the app

This has two steps:

##### Adding cookie:

  1. Login to your erp account. Go to Student Academic Activities (UG) section in Academic. This gives you a cookie for accesing the /Acad route. You will not be able to mine the grades without this.
  
  
  2.Get the content of the JSID#/Acad named cookie set by ERP. Most web browsers enable you to view cookies from settings . It should be something like '0906E89CA7F4BDDE983B34012BDFFA08.worker3'. Update this in getNewGrades.py under the cookie variable.
  
  
 #### Mine grades:
 
  (This will only work if done after adding cookie of your session.)
  
  Run the following code:
  
  `python getNewGrades.py <YearSemester>`
  
  The command line argument string passed should have both Year and semester for which the grades are being displayed on erp.
  Example : If you update grades at the end of spring 2019, then pass the argument as 2019Spring or prefereably something similar covering same information.
  
## Maintainer

[Ayush Kaushal](https://github.com/Ayushkaushal) (@Ayushkaushal on [metakgp Slack](https://slack.metakgp.org).)
  
  
