.. contents::

Introduction
============

This package allows to create and mantain vocabularies.


Install
=======

Just add this package to your buildout eggs list and install it


Usage
=====

Add a "Vocabulary" and then create "Terms" inside it as you would do with
any content type.

The vocabulary id is going to be the Vocabulary object id, with
'collective.dynamicvocab.' as prefix.

The 'Summary' field from the object will be used as the description for the
vocabulary

You can go to the "Dexterity Content Types" tool, add a choice field to any
content type, and choose the newly created vocabulary to be used.


TODO
====

Vocabularies are registered as persistent utilities with the root object
(Plone Site) as context.
It remains yet to be done to unregister the utility when deleting the
Vocabulary object.

An uninstall profile that removes the persistent utilities is also missing.
