# -*- coding: utf-8 -*-
from collective.dynamicvocab.interfaces import ITerm

from plone.dexterity.content import Item

from zope.interface import implementer


@implementer(ITerm)
class Term(Item):
    pass
