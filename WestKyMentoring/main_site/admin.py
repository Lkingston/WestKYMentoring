from django.contrib import admin
import main_site.models as main

admin.site.register(main.Address)
admin.site.register(main.Individual)
admin.site.register(main.Mentor)
admin.site.register(main.Mentee)
admin.site.register(main.Intern)
admin.site.register(main.Volunteer)
admin.site.register(main.Event)
admin.site.register(main.Sponsor)
admin.site.register(main.Donation)
admin.site.register(main.Badge)
admin.site.register(main.Event_Worker)
