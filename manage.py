import os
import sys
import svn.remote
import pprint
import svn.local
import manage_versions.controllers as mv
import manage_versions.settings as svnSettings
#python manage.py args
#args = id of projects
if __name__ == "__main__":
    try:
        mv_s = svnSettings.svnSettings()
        mv_s.load_settings()
        if len(sys.argv)>1:
            print("Generate only " + sys.argv[1] + " project")
            current = int(sys.argv[1])
            c = mv.svnController(mv_s.config[current])
            c.diff()
        else:
            print("Generate each projects")
            for i in range(0, mv_s.count):
                c = mv.svnController(mv_s.config[i],)
                c.diff()
        print("tool finish")
        mv_s.save_settings()
    except Exception as E:
        print("Error "+str(E))
