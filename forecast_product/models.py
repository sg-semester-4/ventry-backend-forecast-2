# # This is an auto-generated Django model module.
# # You'll have to do the following manually to clean this up:
# #   * Rearrange models' order
# #   * Make sure each model has one field with primary_key=True
# #   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
# #   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# # Feel free to rename the models, but don't rename db_table values or field names.
# from django.db import models


# class Account(models.Model):
#     id = models.UUIDField(primary_key=True)
#     name = models.TextField(blank=True, null=True)
#     password = models.TextField(blank=True, null=True)

#     class Meta:
#         managed = True
#         db_table = 'account'


# class InventoryControl(models.Model):
#     id = models.UUIDField(primary_key=True)
#     account = models.ForeignKey(
#         Account, models.DO_NOTHING, blank=True, null=True)
#     item = models.ForeignKey('Item', models.DO_NOTHING, blank=True, null=True)
#     quantity = models.DecimalField(
#         max_digits=65535, decimal_places=65535, blank=True, null=True)
#     created_at = models.DateTimeField(blank=True, null=True)
#     updated_at = models.DateTimeField(blank=True, null=True)

#     class Meta:
#         managed = True
#         db_table = 'inventory_control'


# class Item(models.Model):
#     id = models.UUIDField(primary_key=True)
#     code = models.TextField(blank=True, null=True)
#     name = models.TextField(blank=True, null=True)
#     description = models.TextField(blank=True, null=True)
#     quantity = models.DecimalField(
#         max_digits=65535, decimal_places=65535, blank=True, null=True)
#     max_quantity = models.DecimalField(
#         max_digits=65535, decimal_places=65535, blank=True, null=True)
#     unit_type = models.TextField(blank=True, null=True)
#     unit_cost_price = models.DecimalField(
#         max_digits=65535, decimal_places=65535, blank=True, null=True)
#     image_url = models.TextField(blank=True, null=True)
#     account = models.ForeignKey(
#         Account, models.DO_NOTHING, blank=True, null=True)

#     class Meta:
#         managed = True
#         db_table = 'item'


# class ItemCombination(models.Model):
#     parent_item = models.ForeignKey(
#         Item, models.DO_NOTHING, blank=True, null=True)
#     child_item = models.ForeignKey(
#         Item, models.DO_NOTHING, blank=True, null=True)
#     quantity = models.DecimalField(
#         max_digits=65535, decimal_places=65535, blank=True, null=True)

#     class Meta:
#         managed = True
#         db_table = 'item_combination'


# class Product(models.Model):
#     id = models.UUIDField(primary_key=True)
#     code = models.TextField(blank=True, null=True)
#     name = models.TextField(blank=True, null=True)
#     description = models.TextField(blank=True, null=True)
#     quantity = models.DecimalField(
#         max_digits=65535, decimal_places=65535, blank=True, null=True)
#     unit_type = models.TextField(blank=True, null=True)
#     unit_cost_price = models.DecimalField(
#         max_digits=65535, decimal_places=65535, blank=True, null=True)
#     unit_sell_price = models.DecimalField(
#         max_digits=65535, decimal_places=65535, blank=True, null=True)
#     image_url = models.TextField(blank=True, null=True)
#     account = models.ForeignKey(
#         Account, models.DO_NOTHING, blank=True, null=True)

#     class Meta:
#         managed = True
#         db_table = 'product'


# class ProductItem(models.Model):
#     product = models.ForeignKey(
#         Product, models.DO_NOTHING, blank=True, null=True)
#     item = models.ForeignKey(Item, models.DO_NOTHING, blank=True, null=True)
#     quantity = models.DecimalField(
#         max_digits=65535, decimal_places=65535, blank=True, null=True)

#     class Meta:
#         managed = True
#         db_table = 'product_item'


# class ProductTransaction(models.Model):
#     id = models.UUIDField(primary_key=True)
#     account = models.ForeignKey(
#         Account, models.DO_NOTHING, blank=True, null=True)
#     product = models.ForeignKey(
#         Product, models.DO_NOTHING, blank=True, null=True)
#     quantity = models.DecimalField(
#         max_digits=65535, decimal_places=65535, blank=True, null=True)
#     total_sell_price = models.DecimalField(
#         max_digits=65535, decimal_places=65535, blank=True, null=True)
#     created_at = models.DateTimeField(blank=True, null=True)
#     updated_at = models.DateTimeField(blank=True, null=True)

#     class Meta:
#         managed = True
#         db_table = 'product_transaction'
