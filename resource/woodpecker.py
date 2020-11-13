#!/usr/bin/python

import lldb
import sys
import os

WoodPeckerSupportDirectory = os.path.expanduser("~/Documents/WoodPecker")

def localWoodPeckerServerBinaryPath():
        return os.path.join(WoodPeckerSupportDirectory, "WoodPeckeriOS.framework/WoodPeckeriOS")

def doload(debugger, command, exe_ctx, result, dict):
	# path to the framework binary file
    path = localWoodPeckerServerBinaryPath()
    exists = os.path.exists(path)
    if not exists:
    	print ("Woodpecker framework not exists: {0}".format(path))
    	return
    imagePath = lldb.SBFileSpec(path)
    error = lldb.SBError()
    process = exe_ctx.process
    process.LoadImage(imagePath, error)
    if error.Success():
    	print ("🌿Woodpecker load succeed")
    else:
    	print(error)
