# -*- coding: utf-8 -*-
from collective.dynamicvocab.interfaces import IVocabulary

from plone.dexterity.content import Container

from zope.interface import implements


class Vocabulary(Container):
    implements(IVocabulary)
