# -*- coding: utf-8 -*-
import logging
from collective.dynamicvocab.dynamic_vocabulary import DynamicVocabulary
from zope.component import getUtilitiesFor
from zope.component import queryUtility
from zope.component.hooks import getSite
from zope.schema.interfaces import IVocabularyFactory


logger = logging.getLogger('collective.dynamicvocab')


class DynamicVocabUtility(object):

    def register_vocabulary(self, obj):
        path = '/'.join(obj.getPhysicalPath())
        logger.info("Registering dynamic vocabulary: %s" % path)

        vocab_id = obj.vocabulary_id

        registered_vocabs = [i[0] for i in getUtilitiesFor(IVocabularyFactory)]

        if vocab_id and vocab_id in registered_vocabs:
            logger.warn("There is a vocabulary already registered with id: %s"
                        % vocab_id)
            return False

        if not vocab_id:
            vocab_id = 'collective.dynamicvocab.%s' % obj.id

        if vocab_id in registered_vocabs:
            index = 1
            aux_name = vocab_id
            while aux_name in registered_vocabs:
                index += 1
                aux_name = '%s.%s' % (vocab_id, index)

            vocab_id = aux_name

        vocabulary = DynamicVocabulary(obj)
        for child in obj.getChildNodes():
            vocabulary.addTerm(child)

        site = getSite()
        sm = site.getSiteManager()
        sm.registerUtility(vocabulary, IVocabularyFactory, vocab_id)
        logger.info("Vocabulary registered with id: %s" % vocab_id)

        obj.vocabulary_id = vocab_id
        return True

    def unregister_vocabulary(self, obj):

        site = getSite()
        path = '/'.join(obj.getPhysicalPath())
        logger.info("Unregistering dynamic vocabulary: %s" % path)

        vocab_id = obj.vocabulary_id

        if not vocab_id:
            logger.info(
                "This vocabulary did not have a stored vocabulary id, "
                "it may not have been registered yet. Doing nothing"
            )
            return

        vocab = queryUtility(IVocabularyFactory, vocab_id, context=site)

        if vocab is None:
            logger.info(
                "This vocabulary was not registered in the GSM, not doing "
                "anything."
            )
            return

        sm = site.getSiteManager()
        unregistered = sm.unregisterUtility(vocab)

        if unregistered:
            logger.info(
                "Vocabulary unregistered ok."
            )
        else:
            logger.warn(
                "There was an error trying to unregister vocabulary"
            )

        return unregistered

    def add_term_to_vocabulary(self, vocab, term):
        site = getSite()
        vocab_path = '/'.join(vocab.getPhysicalPath())
        term_path = '/'.join(term.getPhysicalPath())
        logger.info("Adding term %s to vocabulary: %s"
                    % (term_path, vocab_path))

        vocab_id = vocab.vocabulary_id

        if not vocab_id:
            logger.info(
                "This vocabulary did not have a stored vocabulary id, "
                "it may not have been registered yet. Doing nothing"
            )
            return

        vocabulary = queryUtility(IVocabularyFactory, vocab_id, context=site)

        if vocabulary is None:
            logger.info(
                "This vocabulary was not registered in the GSM, not doing "
                "anything."
            )
            return

        vocabulary.addTerm(term)
        sm = site.getSiteManager()
        sm.registerUtility(vocabulary, IVocabularyFactory, vocab_id)
        logger.info("Term added.")
