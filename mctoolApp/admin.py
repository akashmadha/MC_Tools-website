from django.contrib import admin
from .models import ConstructionTools, PavingBreaker, Specification
from django.utils.html import format_html


class SpecificationInline(admin.TabularInline):
    model = Specification
    extra = 1  # Show one empty form by default for adding new entries 
    show_change_link = True

    class Media:
        js = ('mctoolApp/static/js/main.js',)  # Optional: Add custom JavaScript for dynamic functionality
        css = {
            'all': ('mctoolApp/admin_custom/custom_admin.css',),  # Optional: Add custom CSS
        }

    # Customize the header for the inline table
    verbose_name = "Specification"
    verbose_name_plural = "Specifications"


@admin.register(PavingBreaker)
class PavingBreakerAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'description', 'construction_tools', 'image_preview')
    inlines = [SpecificationInline]  # Attach the inline form for Specifications

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 100px; height: auto;" />', obj.image.url)
        return "No Image"

    image_preview.short_description = 'Image Preview'

    fields = ('product_name', 'description', 'construction_tools', 'image', 'image_preview')
    readonly_fields = ('image_preview',)

    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}
        extra_context['title'] = "Manage Paving Breakers"
        return super().changelist_view(request, extra_context=extra_context)


@admin.register(Specification)
class SpecificationAdmin(admin.ModelAdmin):
    list_display = ('key', 'metric_value', 'imperial_value', 'paving_breaker', 'image_preview')

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 50px; height: auto;" />', obj.image.url)
        return "No Image"

    image_preview.short_description = 'Image Preview'

    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}
        extra_context['title'] = "Manage Specifications"
        return super().changelist_view(request, extra_context=extra_context)


# from django.contrib import admin
# from .models import Product

# class ProductAdmin(admin.ModelAdmin):
#     list_display = ('name', 'category', 'price', 'image')  # Display relevant fields
#     search_fields = ('name', 'category')  # Add a search bar to filter products

# admin.site.register(Product, ProductAdmin)



# from django.contrib import admin
# from .models import Pro_name, Pro_SPE,spe,pro

# # Admin configuration for Pro_name
# @admin.register(Pro_name)
# class ProNameAdmin(admin.ModelAdmin):
#     list_display = ('product_name', 'description', 'construction_tools')
#     search_fields = ('product_name', 'description')
#     list_filter = ('construction_tools',)

# # Admin configuration for Pro_SPE
# @admin.register(Pro_SPE)
# class ProSPEAdmin(admin.ModelAdmin):
#     list_display = ('product_spe_name', 'description', 'Product_name')
#     search_fields = ('product_spe_name', 'description')
#     list_filter = ('Product_name',)
# # Admin configuration for Pro_name


# @admin.register(pro)
# class ProAdmin(admin.ModelAdmin):
#     list_display = ('product_name', 'description', 'construction_tools')
#     search_fields = ('product_name', 'description')
#     list_filter = ('construction_tools',)

# # Admin configuration for Pro_SPE
# @admin.register(spe)
# class spedmin(admin.ModelAdmin):
#     list_display = ('product_spe_name', 'description', 'Product_name')
#     search_fields = ('product_spe_name', 'description')
#     list_filter = ('Product_name',)
