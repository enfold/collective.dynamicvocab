# -*- coding: utf-8 -*-
from persistent.list import PersistentList
from persistent.mapping import PersistentMapping
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

        self.by_value = PersistentMapping()
        self.by_token = PersistentMapping()
        self._obj = obj
        self._terms = PersistentList()

        if interfaces:
            directlyProvides(self, *interfaces)

    @property
    def __doc__(self):
        return self._obj.description

    def addTerm(self, obj):
        if not isinstance(self._terms, PersistentList):
            terms = PersistentList()
            for term in self._terms:
                terms.append(term)
            self._terms = terms
        for attr_id in ['by_value', 'by_token']:
            attr = getattr(self, attr_id)
            if not isinstance(attr, PersistentMapping):
                new_attr = PersistentMapping()
                for k, v in attr.items():
                    new_attr[k] = v
                setattr(self, attr_id, new_attr)
        term = SimpleTerm(obj.id, obj.id, obj.title)
        self._terms.append(term)
        # XXX: No need to check if the item already exists in the vocabulary
        self.by_value[term.value] = term
        self.by_token[term.token] = term

    def clearTerms(self):
        self.by_value = PersistentMapping()
        self.by_token = PersistentMapping()
        self._terms = PersistentList()
