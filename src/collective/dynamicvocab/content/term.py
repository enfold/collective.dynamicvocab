# -*- coding: utf-8 -*-
from collective.dynamicvocab.interfaces import ITerm

from plone.dexterity.content import Item

from zope.interface import implements


class Term(Item):
    implements(ITerm)
