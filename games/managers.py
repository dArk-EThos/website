from django.db.models import Manager
from django.db.models import Q


class ScreenshotManager(Manager):
    def published(self, user=None, is_staff=False):
        query = self.get_queryset()
        query = query.order_by('uploaded_at')
        if is_staff:
            return query
        elif user:
            return query.filter(Q(published=True) | Q(uploaded_by=user))
        else:
            return query.filter(published=True)
