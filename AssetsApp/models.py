from django.db import models
from datetime import *
from django.db import utils

import AuthenticationApp


# Create your models here. 
class AssetsCategories(models.Model):
    enterprise_id = models.ForeignKey(AuthenticationApp.models.Enterprises, on_delete=models.CASCADE)
    id = models.PositiveIntegerField(primary_key=True, editable=False)
    parent_id = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=40, blank=False)
    description = models.TextField(blank=True, null=True)
    is_sub_category = models.BooleanField()
    datetime_added = models.DateTimeField()
    user = models.ForeignKey(AuthenticationApp.models.User, on_delete=models.CASCADE)
    
    class Meta:
        pass
    
    @classmethod    
    def add_category(self, enterprise, user, description):
        self.objects.create(id=self.objects.count() + 1,
                            enterprise_id = AuthenticationApp.models.Enterprises.objects.get(enterprise_id=enterprise),
                            name = description['category_name'], 
                            description = description['description'],
                            is_sub_category = 0,
                            datetime_added = datetime.now(),
                            user = AuthenticationApp.models.User.objects.get(id=user)
                            )
    @classmethod 
    def add_sub_category(self, enterprise, user, description):
        self.objects.create(id=self.objects.count() + 1,
                            enterprise_id = AuthenticationApp.models.Enterprises.objects.get(enterprise_id=enterprise),
                            parent_id = self.objects.get(id=description['parent_category_id']),
                            name = description['category_name'],
                            description = description['description'],
                            is_sub_category = 1,
                            datetime_added = datetime.now(),
                            user = AuthenticationApp.models.User.objects.get(id=user)
                            )
    @classmethod
    def all_categories(self, enterprise):
        return  self.objects.filter(enterprise_id = AuthenticationApp.models.Enterprises.objects.get(enterprise_id=enterprise)
                                    )
    
    @classmethod
    def categories(self, enterprise):
        return  self.objects.filter(enterprise_id = AuthenticationApp.models.Enterprises.objects.get(enterprise_id=enterprise)
                                    )

    @classmethod
    def sub_categories(self, enterprise):
        return  self.objects.filter(enterprise_id = AuthenticationApp.models.Enterprises.objects.get(enterprise_id=enterprise),
                            is_sub_category = 1
                                    )
      
class Assets(models.Model):
    enterprise_id = models.ForeignKey(AuthenticationApp.models.Enterprises, on_delete=models.CASCADE)
    asset_id = models.CharField(max_length=20, primary_key=True, editable=False)
    category = models.ForeignKey(AssetsCategories, on_delete=models.CASCADE)
    sub_category = models.ForeignKey(AssetsCategories, on_delete=models.CASCADE, related_name='sub_category')
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=50)
    class_term = models.CharField(max_length=15)
    status = models.CharField(max_length=20, help_text='0 Is Inservice, 1 is Inactive and 3 Under Maintaince' )
    currency = models.CharField(max_length=5, null=True)
    datetime_added = models.DateTimeField(auto_now=True)
    #item_id = models.ForeignKey(Items, on_delete=models.CASCADE, null=True)
        
    class Meta:
        pass
        
    @classmethod
    def add_asset(self, enterprise, user, description):
        asset_id = "OCASS-{0}".format(self.objects.count()+ 1)
        try:
            self.objects.create(
                enterprise_id = AuthenticationApp.models.Enterprises.objects.get(enterprise_id=enterprise),
                asset_id = asset_id,
                name = description["account_name"],
                category = AssetsCategories.objects.get(id=1),
                sub_category = AssetsCategories.objects.get(id=2),#int(description["sub_category"]),
                description = description["description"],
                class_term = description['class'],
                currency = description["currency"],
                status = description["status"],
                datetime_added = datetime.now()
                )
            return asset_id
        except utils.IntegrityError:
            return False
        except utils.OperationalError:
            return False
    @classmethod  
    def to_json(self):
        accounts_list = []
        for item in self.objects.filter(category=1):
            description = {"account_id" : item.asset_id}
            description['sub_category'] = item.sub_category.name
            description["name"] = item.name
            description["description"] = item.description
            description["currency"] = item.currency
            description["status"] = item.status
            accounts_list.append(description)
        
        return  accounts_list