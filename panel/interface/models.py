from django.db import models
from user.models import User

class Interface(models.Model):
    id = models.AutoField(primary_key=True, help_text='Interface ID')
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    
    # -- Tunnel related information --
    public_key = models.TextField(help_text='Public Key used for this tunnel')
    private_key = models.TextField(help_text='Private Key used for this tunnel')
    listening_port = models.IntegerField(help_text='Port to be listened')
    # --------------------------------