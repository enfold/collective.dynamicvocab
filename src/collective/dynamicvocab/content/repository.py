# -*- coding: utf-8 -*-
from collective.dynamicvocab.interfaces import IVocabularyRepository

from plone.dexterity.content import Container

from zope.interface import implementer


@implementer(IVocabularyRepository)
class VocabularyRepository(Container):
    pass
