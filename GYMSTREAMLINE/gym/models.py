from django.db import models

# Create your models here.

class Coach(models.Model):
    CoaId = models.BigAutoField(primary_key=True)
    Name = models.CharField(max_length=60, null=True)
    Surname = models.CharField(max_length=60, null=True)
    Contact = models.CharField(max_length=10, null=True)
    Emailid = models.CharField(max_length=60, null=True)
    Age = models.CharField(max_length=40, null=True)
    Gender = models.CharField(max_length=10, null=True)
    JobTitle = models.CharField(max_length=60, null=True)

    def __str__(self):
        return str(self.CoaId)

class Plan(models.Model):
    NameId = models.CharField(max_length=60, primary_key=True, default='')
    Amount = models.CharField(max_length=40, null=True)
    Duration = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.NameId

class Member(models.Model):
    MemId = models.BigAutoField(primary_key=True)
    Name = models.CharField(max_length=60, null=True)
    Surname = models.CharField(max_length=60, null=True)
    Contact = models.CharField(max_length=10, null=True)
    Emailid = models.CharField(max_length=60, default='example@example.com')
    Age = models.CharField(max_length=40, null=True)
    Gender = models.CharField(max_length=10, default="")

    def __str__(self):
        return str(self.MemId)


class MemberPlan(models.Model):
    id = models.BigAutoField(primary_key=True)
    MemberId = models.ForeignKey(Member, on_delete=models.CASCADE)
    PlanIdName = models.ForeignKey(Plan, on_delete=models.CASCADE)
    Joindate = models.DateField()
    Expdate = models.DateField()
    State = models.CharField(max_length=20, null=True)
    CoachId = models.ForeignKey(Coach, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        constraints = [ models.UniqueConstraint(fields=['MemberId', 'PlanIdName'], name='unique_member_plan') ]