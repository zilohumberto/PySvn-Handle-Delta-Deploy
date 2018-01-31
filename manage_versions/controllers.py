#!/usr/bin/env python
#import svn.remote
import pprint
import svn
import os,sys,shutil
from pathlib import Path
class svnController:
    is_local = True
    config = None
    def __init__(self,config=None):
        self.config = config
        if self.is_local:
            self.tortoise = svn.local.LocalClient(
                self.config["source_local"])
        else:
            pass
            #for now no happend
            #self.tortoise= svn.remote.RemoteClient(config["source_local"])

    def clear_paciente(self):
        import shutil
        my_file = Path(
            self.config["destination"] + "\\")
        if my_file.exists():
            print("LIMPIANDO DIR")
            shutil.rmtree(self.config["destination"])
            os.mkdir(self.config["destination"])

    def list(self,):
        pass

    def diff(self):
        start_revision = self.config["last_revision"]
        end_revision = self.get_revision_number_of_directory()
        self.clear_paciente()
        if start_revision>= end_revision:
            print("No need update")
        print("Updating ",self.config["name"])
        _list = self.tortoise.diff_summary(start_revision, end_revision)
        self.config["last_revision"] = end_revision
        x = 0
        for _ in _list:
            if self.is_local:
                self.handleFiles(_["path"],_["kind"],_["item"])

    def handleFiles(self,path, kind,item):
        #get the diferrent with the local
        self.dir_toGenerate = self.config["destination"]
        dif = self.getDifEnd(path)
        self.dir_toGenerate=self.config["destination"]
        #print(self.dir_toGenerate," - ",dif)
        new_path = self.generate(os.path.dirname(dif))

        #print(os.path.dirname(dif),os.path.basename(dif))
        self.moveToDeploy(path,new_path+"\\"+os.path.basename(dif))


    def getDifEnd(self,path):
        return path[len(self.config["source_local"]):]

    def generate(self,path):
        x =0
        if path[0]=="\\":
            x=1
        xpath = self.dir_toGenerate + r"\\" + path[x:len(path)]
        try:
            my_file = Path(xpath)
            if not my_file.exists():
                print("creando ",xpath)
                os.makedirs(xpath)
        except Exception as E:
            print(E)

        return xpath

    def moveToDeploy(self,_from,_to):
        try:
            print("moviendo from: ",_from," to:",_to)
            shutil.copy(_from, _to)
        except Exception as E:
            print(E)


    def get_revision_number_of_directory(self):
        # Extended information.
        entries = self.tortoise.list(extended=True)
        max_rev = 0
        for entry in entries:
            # pprint.pprint(entry)
            max_rev = max(max_rev, entry["commit_revision"])
        return max_rev
