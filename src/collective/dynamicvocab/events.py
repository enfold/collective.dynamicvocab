# -*- coding: utf-8 -*-
from collective.dynamicvocab.interfaces import IDynamicVocabUtility
from zope.component import queryUtility


def register_vocabulary(obj, event):
    utility = queryUtility(IDynamicVocabUtility)
    utility.register_vocabulary(obj)


def add_term_to_vocabulary(obj, event):
    vocab = obj.aq_parent
    utility = queryUtility(IDynamicVocabUtility)
    utility.add_term_to_vocabulary(vocab, obj)


def unregister_vocabulary(obj, event):
    pass
