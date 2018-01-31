import codecs
import json
#all vars for default to start!
class svnSettings:
    count = 2
    dir_local = []
    dir_server = []
    concurrent_id = 0
    dir_toGenerate = []
    last_revison = []
    config = None
    source_config_file = "C:\Desarrollo-Practica\PySvn\manage_versions\config.json"
    def load_settings(self,):
        configFile = open(
            self.source_config_file).read()
        self.config = json.loads(configFile)
        self.change_settings()

    def change_settings(self,):
        self.count = len(self.config)
        for i in range(0,len(self.config)):
            self.dir_server.append(self.config[i]["source_server"])
            self.dir_local.append(self.config[i]["source_local"])
            self.dir_toGenerate.append(self.config[i]["destination"])
            self.last_revison.append(int(self.config[i]["last_revision"]))
        

    def save_settings(self):
        with open(self.source_config_file, 'w') as fp:
            json.dump(self.config, fp)

    def generate_info(self):
        pass
