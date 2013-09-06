from github import Github
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User


class ProjectManager(models.Manager):
    """Project manager"""

    def _get_remote_projects(self, user):
        """Get remote projects"""
        token = user.social_auth.get().extra_data['access_token']
        github = Github(token)
        github_user = github.get_user()
        return github_user.get_repos('public')

    def get_or_create_for_user(self, user):
        """Get or create for user"""
        for repo in self._get_remote_projects(user):
            Project.objects.get_or_create(
                owner=user,
                name=repo.full_name,
                url=repo.url,
            )
        return self.filter(owner=user)


class Project(models.Model):
    """Github project"""
    owner = models.ForeignKey(User, verbose_name=_('owner'))
    name = models.CharField(max_length=300, verbose_name=_('name'))
    url = models.URLField(verbose_name=_('url'))
    is_enabled = models.BooleanField(
        default=False, verbose_name=_('is enabled'),
    )

    objects = ProjectManager()

    class Meta:
        verbose_name = _('Project')
        verbose_name_plural = _('Projects')
        ordering = ('-id',)

    def __unicode__(self):
        return self.name
