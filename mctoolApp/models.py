from django.db import models

# Main Products Model
class ConstructionTools(models.Model):
    product_names = models.CharField(max_length=50)
    description = models.TextField(max_length=5000)

    class Meta:
        db_table = 'construction_tools'

    def __str__(self):
        return self.product_names


class PavingBreaker(models.Model):
    construction_tools = models.ForeignKey(
        ConstructionTools, on_delete=models.CASCADE, related_name="paving_breakers"
    )
    image = models.ImageField(upload_to='image', default='')
    product_name = models.CharField(max_length=50)
    description = models.TextField(max_length=500)

    class Meta:
        db_table = 'paving_breaker'

    def __str__(self):
        return self.product_name


class Specification(models.Model):
    paving_breaker = models.ForeignKey(
        PavingBreaker, on_delete=models.CASCADE, related_name="specifications"
    )
    key = models.CharField(max_length=100)  # e.g., "Weight"
    metric_value = models.CharField(max_length=100, blank=True, null=True)  # e.g., "31.5 kg"
    imperial_value = models.CharField(max_length=100, blank=True, null=True)  # e.g., "69 lb"
    image = models.ImageField(upload_to='specifications/', blank=True, null=True)

    class Meta:
        db_table = 'Specification'

    def __str__(self):
        return self.key


# Product Model
class Product(models.Model):
    CATEGORY_CHOICES = (
        ('bicycle', 'Bicycle'),
        ('motorcycle', 'Motorcycle'),
    )

    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    image = models.ImageField(upload_to='product_images/')

    class Meta:
        db_table = 'product'

    def __str__(self):
        return self.name
    


class Pro_name(models.Model):
      construction_tools = models.ForeignKey(
        ConstructionTools, on_delete=models.CASCADE, related_name="Pro_name"
    )
      product_name = models.CharField(max_length=255)
      description = models.TextField()
      image = models.ImageField(upload_to='product_images/')

      class Meta:
        db_table = 'product_name'

      def __str__(self):
        return self.product_name
      

class Pro_SPE(models.Model):
      Product_name = models.ForeignKey(
      Pro_name, on_delete=models.CASCADE, related_name="Pro_SPE"
    )
      product_spe_name = models.CharField(max_length=255)
      description = models.TextField()
      image = models.ImageField(upload_to='product_images/')

      class Meta:
        db_table = 'product_spe'

      def __str__(self):
        return self.product_spe_name
      

class pro(models.Model):
      construction_tools = models.ForeignKey(
        ConstructionTools, on_delete=models.CASCADE, related_name="pro"
    )
      product_name = models.CharField(max_length=255)
      description = models.TextField()
      image = models.ImageField(upload_to='product_images/')

      class Meta:
        db_table = 'pro'

      def __str__(self):
        return self.product_name
      

class spe(models.Model):
      Product_name = models.ForeignKey(
      Pro_name, on_delete=models.CASCADE, related_name="spe"
    )
      product_spe_name = models.CharField(max_length=255)
      description = models.TextField()
      image = models.ImageField(upload_to='product_images/')

      class Meta:
        db_table = 'spe'

      def __str__(self):
        return self.product_spe_name
