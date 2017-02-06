'''
Created on 6 Feb 2017

@author: David Fottrell
'''
from setuptools import setup
from setuptools.dist import check_entry_points

setup(name="Sysinfo",
      version="0.1",
      description="Basic System Information - Practical 1 Question2",
      url="",
      author="David Fottrell",
      author_email="david.fottrell@ucdconnect.ie",
      licence="GPL3",
      packages=["Sysinfo"],
      entry_points={
          'console_scripts':['workspaceComp30670_Sysinfo=Sysinfo.main:main']
          }
    
    )
