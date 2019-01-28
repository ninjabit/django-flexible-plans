from django.contrib import admin
import swapper

admin.site.register(swapper.load_model('flexible_plans', 'Subscription'))
