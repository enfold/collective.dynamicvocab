# -*- coding: utf-8 -*-
from collective.dynamicvocab.interfaces import IVocabularyRepository

from plone.dexterity.content import Container

from zope.interface import implements


class VocabularyRepository(Container):
    implements(IVocabularyRepository)
