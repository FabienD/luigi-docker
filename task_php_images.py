from tasks.generic_task import (
    BuildImage,
    PushImage
)

class Push(PushImage):
    image = 'php'

class Build(BuildImage):
    image = 'php'

    def requires(self):
        match self.sub:
            case 'dev':
                return Build(version=self.version, sub='fpm', date=self.date)
            case 'blackfire':
                return Build(version=self.version, sub='dev', date=self.date)
            case 'cli-consumer':
                return Build(version=self.version, sub='cli', date=self.date)
