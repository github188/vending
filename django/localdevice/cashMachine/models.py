from datetime import date, datetime

from django.db import models



class CashMachineManager(models.Manager):
    def byName(self, *args, **kwargs):
        date.string
        return super(CashMachineManager, self).filter(operateName=args[0])
    def byPeriod(self, *args):
        return super(CashMachineManager, self).filter(operateTime__gte=args[0]).filter(orderTime__lte=args[1])

