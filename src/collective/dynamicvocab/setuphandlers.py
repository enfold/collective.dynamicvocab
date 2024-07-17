
from plone import api
from plone.dexterity.utils import createContentInContainer


def post_install(context):
    site = api.portal.get()
    addRepository(site)


def addRepository(site):
    if 'vocabularies' not in site:
        repository = createContentInContainer(
            site, 'collective.dynamicvocab.repository',
            title=u"Vocabularies", checkConstraints=False
        )
        repository.exclude_from_nav = True
