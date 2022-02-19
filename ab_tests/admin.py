from typing import Iterable

from django.contrib import admin
from django.contrib.admin import register, ModelAdmin, TabularInline
from django.contrib.auth.models import Group, User
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Experiment, Variation


class VariationInlineFormset(BaseInlineFormSet):
    EXPECTED_TOTAL_PROBABILITY: int = 100

    def clean(self) -> None:
        self.validate_total_probability()

    def validate_total_probability(self) -> None:
        if sum(self.accumulate_variation_probabilities()) != self.EXPECTED_TOTAL_PROBABILITY:
            raise ValidationError(f'total probability should be {self.EXPECTED_TOTAL_PROBABILITY}')

    def accumulate_variation_probabilities(self) -> Iterable[int]:
        for form in self.forms:
            if form.cleaned_data and not form.cleaned_data.get('DELETE'):
                yield form.cleaned_data['probability']


class VariationInline(TabularInline):
    model = Variation
    formset = VariationInlineFormset
    extra = 3


@register(Experiment)
class ExperimentAdmin(ModelAdmin):
    inlines = [VariationInline]


admin.site.unregister(User)
admin.site.unregister(Group)
