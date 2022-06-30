# import imp
# from django.db.models.signals import pre_save, post_save, pre_delete
# from django.core.exceptions import ValidationError
# from django.dispatch import receiver
# # from .models import Sponsor, Student, StudentSponsor


# @receiver(pre_save, sender=StudentSponsor)
# def check_budget(sender, instance, **kwargs):
#     """"This pre_save Signal method checks the budget also adds  money or minuses"""
#     student = Student.objects.get(id = instance.student.id)
#     sponsor = Sponsor.objects.get(id = instance.sponsor.id)
#     student_reminder = student.demand - student.paid_money

#     if (sponsor.budget >= instance.money and 
#         student.demand >  student.paid_money and 
#         student_reminder >= instance.money):

#         sponsor.budget -= instance.money
#         sponsor.paid_money += instance.money
#         student.paid_money += instance.money
#         student.save()
#         sponsor.save()
#     else:
#         raise ValidationError(f"{instance.money} Bu summani Qosha olamaysiz")

# @receiver(pre_delete, sender = StudentSponsor)
# def delete_budeget(sender, instance,**kyargs):
#     """"This Signal function deletes paid_money in both Student and Sponsor"""
#     student = Student.objects.get(id=instance.student.id)
#     sponsor = Sponsor.objects.get(id=instance.sponsor.id)

#     student.paid_money -= instance.money
#     sponsor.paid_money -= instance.money
#     sponsor.budget += instance.money

#     sponsor.save()
#     student.save()
