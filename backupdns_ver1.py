#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
===============================================================================================================
Created on:   	03/06/2019 
Created by:   	Agustin.Lacorazza - alacorazza@primary.com.ar
Organization: 	Primary technology
Filename:     	Backup DNS Zones Route 53
--------------------------------------------------------------------------------------------------
Description:  Script to Backup the DNS Zones with Cli53 
==============================================================================================================#>
"""



import os, sys, time 

today=time.strftime('%Y%m%d')


# Path to be created
path = ("/home/infrapmy/backupdns/"+str(today))

os.mkdir( path, 0755 );
os.chdir (path)
os.system ( "cli53 export dns1.txt > dns1.txt")
os.system ( "cli53 export dns2.txt > dns2.txt")
os.system ( "cli53 export dns3.txt > dns3.txt")
os.system ( "cli53 export dns4.txt > dns4.txt")
os.system ( "cli53 export dns5.txt > dns5.txt")
os.system ( "cli53 export dns6.txt > dns6.txt")



print "Backup is done!"