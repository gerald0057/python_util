
class Command(object):
    def __init__(self, name: str, func, desc: str):
        self.name = name
        self.func = func
        self.desc = desc


class Console(object):
    def __init__(self):
        self.welcome = "Simple Console based on Python"
        self.prompt = "> "
        self.cmds = {}

    def run(self):
        print(self.welcome)
        self.register("help", self._help, "show help table")
        while True:
            i = input(self.prompt)
            if i == "exit":
                break
            if i in self.cmds.keys():
                self.cmds[i].func()

    def _help(self):
        print("help table")
        for key in self.cmds.keys():
            c = self.cmds[key]
            print("{:8}{:8}{}".format(c.name, '-', c.desc))
        print("{:8}{:8}{}".format("exit", '-', "exit from console"))

    def register(self, name: str, func, desc: str):
        c = Command(name, func, desc)
        if name in self.cmds.keys():
            print("cmd {} exist".format(name))
        self.cmds[name] = c

if __name__ == "__main__":
    c = Console()
    c.run()