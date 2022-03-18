from tasks.generic_task import (
    BuildImage,
    PushImage
)

class Push(PushImage):
    image = 'python'
    alias = 'py'

    def requires(self):
        return Build(version=self.version, date=self.date)

class Build(BuildImage):
    image = 'python'
    alias = 'py'
