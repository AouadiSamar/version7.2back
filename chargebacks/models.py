from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.conf import settings


class Chargeback(models.Model):
    is_active = models.BooleanField(default=True)


    title = models.CharField(max_length=100)
    description = models.TextField()
    authorization_number = models.CharField(_("Authorization Number"), max_length=255,null=True,  blank=False,unique=True)
    amount = models.DecimalField(_("Amount"), max_digits=10, unique=True, null=True,decimal_places=2)
    merchant_number = models.CharField(_("Merchant Number"), null=True,max_length=255)
    merchant_email = models.EmailField(_("Merchant Email"),unique=True,null=True)
    merchant_name = models.CharField(_("Merchant Name"), null=True,max_length=255)

    assigned_to = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='assigned_chargebacks',
        verbose_name=_("Assigned To")
    )

    STATUS_CHOICES = [
        ('created', _('Created')),
        ('sent_to_merchant', _('Sent to Merchant')),
        ('processing_by_paymee', _('Processing by Paymee')),
        ('processing_by_bank', _('Processing by Bank')),
        ('won', _('Won')),
        ('lost', _('Lost')),
        ('desactivated', _('Desactivated')),
        ('reactivate', _('Reactivate')),


    ]

    status = models.CharField(_("Status"), max_length=100, choices=STATUS_CHOICES, null=True)
    
    reason = models.TextField(_("Reason"),null=True)
    creation_date = models.DateTimeField(_("Creation Date"), default=timezone.now)
    modification_date = models.DateTimeField(_("Modification Date"), auto_now=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,null=True, on_delete=models.CASCADE, related_name='created_chargebacks')

    class Meta:
        verbose_name = _("Chargeback")
        verbose_name_plural = _("Chargebacks")
    def toggle_active(self):
        self.is_active = not self.is_active
        self.save()

    def __str__(self):
        return f"Chargeback{self.title} - {self.authorization_number} - {self.status}"
    
    
 

from django.db import models




from django.db import models
from django.conf import settings

from users.models import User
class Comment(models.Model):
    text = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)  # Automatically set the field to now when the object is first created.

    chargeback = models.ForeignKey(Chargeback, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User,null=True,on_delete=models.CASCADE) 

    def __str__(self):
        return self.text[:50]



    

from django.db import models
from django.conf import settings

from django.db import models
from django.conf import settings

# models.py
from django.db import models
from django.conf import settings

class ActionLog(models.Model):
    chargeback = models.ForeignKey('Chargeback', related_name='logs', on_delete=models.CASCADE)
    action = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='action_logs')

    def __str__(self):
        return f'{self.created_at.strftime("%Y-%m-%d %H:%M:%S")} - {self.action} by {self.user.email}'



from django.db import models

from django.conf import settings
from django.db import models

class File(models.Model):
    chargeback = models.ForeignKey(Chargeback, related_name='files', null=True,on_delete=models.CASCADE)
    file = models.FileField(upload_to='uploads/')  # Ensure your field is correctly defined
