from tasks.generic_task import (
    BuildImage,
    PushImage
)

class Push(PushImage):
    image = 'db'

    def requires(self):
        return Build(version=self.version, date=self.date)

class Build(BuildImage):
    image = 'db'
