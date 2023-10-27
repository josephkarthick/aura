from django.db import models
from django.utils import timezone
from django.conf import settings
import datetime
        
class it_asset(models.Model):
    sno             = models.AutoField(primary_key=True)
    assetname       = models.CharField(max_length=50  ,null=True) 
    assetID         = models.CharField(max_length=50  ,null=True) 
    assetcat        = models.CharField(max_length=50  ,null=True) 
    purchasedate    = models.CharField(max_length=10  ,null=True) 
    purchasefrom    = models.CharField(max_length=50  ,null=True) 
    manufacturer    = models.CharField(max_length=50  ,null=True) 
    model           = models.CharField(max_length=50  ,null=True) 
    serialno        = models.CharField(max_length=50  ,null=True) 
    supplier        = models.CharField(max_length=50  ,null=True) 
    condition       = models.CharField(max_length=50  ,null=True) 
    warranty        = models.CharField(max_length=50  ,null=True) 
    value           = models.CharField(max_length=50  ,null=True) 
    dayuser         = models.CharField(max_length=50  ,null=True) 
    nightuser       = models.CharField(max_length=50  ,null=True) 
    givenby         = models.CharField(max_length=50  ,null=True) 
    Dstatus         = models.CharField(max_length=50  ,null=True) 
    Ddate           = models.CharField(max_length=10  ,null=True)  
    description     = models.CharField(max_length=100 ,null=True)

    def __str__(self):
        return self.assetname

    
class voip(models.Model):
    vendor          = models.CharField(max_length=50, null=True)
    callbacknumber  = models.CharField(max_length=50, null=True)
    usernumber      = models.CharField(max_length=50, null=True)
    domain          = models.CharField(max_length=50, null=True)
    password        = models.CharField(max_length=50, null=True)
    username        = models.CharField(max_length=50, null=True)
    dop             = models.CharField(max_length=50, null=True)
    remarks         = models.CharField(max_length=50, null=True)
    status          = models.CharField(max_length=50, null=True)

class cred(models.Model):
    emp_id = models.CharField(max_length=50, unique=True)
    username =  models.CharField(max_length=50)
    password =  models.CharField(max_length=50)
    dept = models.CharField(max_length=50)
    
    def __str__(self):
        return self.emp_id
    
      