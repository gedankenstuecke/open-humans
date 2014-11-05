from django.contrib.auth.models import User
from django.db import models

from ..models import BaseActivityDataFile, BaseDataExtractionTask
from common import fields


class ActivityUser(models.Model):
    """Used as key when a 23andme User has DataSets associated with a study."""
    user = fields.AutoOneToOneField(User, related_name='23andme')


class ActivityDataFile(BaseActivityDataFile):
    """Storage for a 23andme data file."""
    study_user = models.ForeignKey(ActivityUser)


class DataExtractionTask(BaseDataExtractionTask):
    """Data extraction task for a 23andme data file."""
    data_file = fields.OneToOneField(ActivityDataFile, null=True)

    @classmethod
    def get_task(cls, filename):
        print "In get task"
        try:
            print "going to return objects"
            return cls.objects.get(data_file__file=filename)
        except cls.DoesNotExist:
            print "fial"
            return None
