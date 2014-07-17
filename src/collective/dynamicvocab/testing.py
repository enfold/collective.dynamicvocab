from plone.app.testing import PloneSandboxLayer
from plone.app.testing import applyProfile
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting

from plone.testing import z2

from zope.configuration import xmlconfig


class CollectivedynamicvocabLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load ZCML
        import collective.dynamicvocab
        xmlconfig.file(
            'configure.zcml',
            collective.dynamicvocab,
            context=configurationContext
        )

        # Install products that use an old-style initialize() function
        #z2.installProduct(app, 'Products.PloneFormGen')

#    def tearDownZope(self, app):
#        # Uninstall products installed above
#        z2.uninstallProduct(app, 'Products.PloneFormGen')

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'collective.dynamicvocab:default')

COLLECTIVE_DYNAMICVOCAB_FIXTURE = CollectivedynamicvocabLayer()
COLLECTIVE_DYNAMICVOCAB_INTEGRATION_TESTING = IntegrationTesting(
    bases=(COLLECTIVE_DYNAMICVOCAB_FIXTURE,),
    name="CollectivedynamicvocabLayer:Integration"
)
COLLECTIVE_DYNAMICVOCAB_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(COLLECTIVE_DYNAMICVOCAB_FIXTURE, z2.ZSERVER_FIXTURE),
    name="CollectivedynamicvocabLayer:Functional"
)
