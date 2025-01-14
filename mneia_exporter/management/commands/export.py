from django.apps import apps
from django.core.management.base import BaseCommand
from termcolor import cprint

from mneia_exporter.apps import MneiaExporterConfig


class Command(BaseCommand):
    """
    Lots of terminal printing stuff here, not very pretty. Unicode characters taken from:
    https://j2r2b.github.io/2020/07/23/text-representation-of-trees.html
    """

    help = "Exports Mneia data"

    def handle(self, *args, **options):
        cprint("MNEIA EXPORTER", "blue", attrs=["bold"])

        models = list(apps.get_app_config(MneiaExporterConfig.name).get_models())

        for model_index, model in enumerate(models):
            if model_index + 1 == len(models):  # last model in the list
                cprint("\u2514", "blue", attrs=["bold"], end="")
            else:
                cprint("\u251c", "blue", attrs=["bold"], end="")
            cprint("\u2500\u2500 Model: ", "blue", attrs=["bold"], end="")
            print(f"{model.__name__} ({model_index+1}/{len(models)})")

            instances = list(model.objects.all())
            for instance_index, instance in enumerate(instances):
                if model_index + 1 == len(models):  # last model in the list
                    print(" ", end="")
                else:
                    cprint("\u2502", "blue", attrs=["bold"], end="")
                cprint("   \u2514\u2500\u2500 Instance: ", "blue", attrs=["bold"], end="")
                print(f'{instance.id}: "{instance}" ({instance_index+1}/{len(instances)})')
                instance.export()
