from plone.dexterity.utils import createContentInContainer


def on_install(context):
    if context.readDataFile('collective_dynamicvocab.txt') is None:
        return
    site = context.getSite()
    addRepository(site)

def addRepository(site):
    if 'vocabularies' not in site:
        repository = createContentInContainer(
            site, 'collective.dynamicvocab.repository',
            title=u"Vocabularies", checkConstraints=False
        )
        repository.exclude_from_nav = True
