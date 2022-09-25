import os
import luigi
import logging

from datetime import datetime
from .container import Container

container = Container()

class ImageTask(luigi.Task):
    version = luigi.Parameter()
    image = luigi.Parameter()
    sub = luigi.Parameter(default=None)
    alias = luigi.Parameter(default=None)
    date = luigi.Parameter()

    def __init__(
            self, *args, **kwargs
    ):
        super().__init__(*args, **kwargs)
        self.client = container.docker_client()
        self.date = self.date if self.date else datetime.utcnow().strftime("%Y%m%d_%H%M%S")

        if self.sub:
            self.hub_path = f"{self.image}/{self.sub}"
            self.tag = f"{self.version}-{self.sub}"
        else:
            self.hub_path = f"{self.image}"
            self.tag = f"{self.version}"

        self.image_name = self.alias if self.alias else self.image

class PushImage(ImageTask):

    def output(self):
        return luigi.LocalTarget(
            f"/var/www/state/push_{self.image}_{self.tag}_{self.date}.log"
        )

    def requires(self):
        return BuildImage(image=self.image, alias=self.alias, version=self.version, sub=self.sub, date=self.date)

    def run(self):
        with self.output().open("w") as out_file:
            self.client.login(
                os.getenv("DOCKER_REGISTRY_USER"),
                password=os.getenv("DOCKER_REGISTRY_PASSWORD"),
            )

            log = self.client.images.push(
                f"{os.getenv('DOCKER_REPOSITORY')}/{self.image_name}",
                tag=f"{self.tag}",
            )

            for gen_log in log:
                out_file.write(gen_log)

class BuildImage(ImageTask):

    def output(self):
        return luigi.LocalTarget(
            f"/var/www/state/build_{self.image}_{self.tag}_{self.date}.log"
        )

    def run(self):
        with self.output().open("w") as out_file:
            image, _ = self.client.images.build(
                path=f'{os.getenv("DOCKER_HUB_PATH")}/{self.hub_path}/{self.version}',
                tag=f'{os.getenv("DOCKER_REPOSITORY")}/{self.image_name}:{self.tag}',
                forcerm=True,
                nocache=True,
                pull=True,
            )

            out_file.write(image.id)
