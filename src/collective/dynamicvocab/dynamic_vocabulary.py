# -*- coding: utf-8 -*-
from zope.interface import implements
from zope.interface import directlyProvides
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary


class DynamicVocabulary(SimpleVocabulary):
    implements(IVocabularyFactory)

    def __call__(self, context):
        return self

    def __init__(self, obj, *interfaces):

        self.by_value = dict()
        self.by_token = dict()
        self._obj = obj
        self._terms = list()

        if interfaces:
            directlyProvides(self, *interfaces)

    @property
    def __doc__(self):
        return self._obj.description

    def addTerm(self, obj):
        term = SimpleTerm(obj.id, obj.id, obj.title)
        self._terms.append(term)
        # XXX: No need to check if the item already exists in the vocabulary
        self.by_value[term.value] = term
        self.by_token[term.token] = term

    def clearTerms(self):        
        self.by_value = dict()
        self.by_token = dict()
        self._terms = list()
