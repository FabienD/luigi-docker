from tasks.generic_task import (
    BuildImage,
    PushImage
)

class Push(PushImage):
    image = 'python'
    alias = 'py'

class Build(BuildImage):
    image = 'python'
    alias = 'py'
