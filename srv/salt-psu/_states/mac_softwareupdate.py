# -*- coding: utf-8 -*-
'''
State for some software update settings.

.. code-block:: yaml
	set_catalog_to_default:
	  softwareupdate.set_catalog:
		- name: Default

.. code-block:: yaml
	set_catalog_to_internal_catalog:
	  softwareupdate.set_catalog:
		- name: https://sweeturl

.. code-block:: yaml
	turn_update_schedule_on:
	  softwareupdate.schedule:
		- name: 'on'
'''

import salt.utils.platform
import logging

log = logging.getLogger(__name__)


__virtualname__ = 'softwareupdate'


def __virtual__():
	if salt.utils.platform.is_darwin():
		return __virtualname__

	return (False, 'states.softwareupdate is only available on macOS.')


def set_catalog(name):
	'''
	Make sure a software update catalog is set.

	name
		The URL of the software update catalog you wish to set, or "Default"
		to ensure the default catalog.
	'''

	ret = {'name': name,
		   'result': True,
		   'changes': {},
		   'comment': ''}

	# get our current catalog value.
	old_catalog = __salt__['softwareupdate.get_catalog']()

	# check if we are set correctly
	if old_catalog == name:
		ret['comment'] = 'Softwareupdate catalog is already set correctly.'
		return ret

	# we are not set correctly so we need set it.
	if name == 'Default':
		set_cat = __salt__['softwareupdate.reset_catalog']()
	else:
		set_cat = __salt__['softwareupdate.set_catalog'](name)

	if not set_cat:
		ret['result'] = False
		ret['comment'] = 'Failed to set softwareupdate'\
			'catalog "{0}"'.format(name)
	else:
		ret['comment'] = 'Successfully set softwareupdate '\
			'catalog to "{0}"'.format(name)
		ret['changes'].update({'catalog': {'old': old_catalog,
									  	   'new': name}})
	return ret


def schedule(name):
	'''
	Turn softwareupdate schedule on/off.

	name
		'on' or 'off' to enable or disable automatic update scheduling.
	'''

	ret = {'name': name,
		   'result': True,
		   'changes': {},
		   'comment': ''}

	# convert yes, or no names to booleans.
	if name.lower() == 'on':
		name = True
	elif name.lower() == 'off':
		name = False

	old_schedule = __salt__['softwareupdate.schedule_enabled']()

	# check if we are set correctly
	if old_schedule == name:
		ret['comment'] = 'Software update schedule is already'\
			' set to {0}'.format(name)
		return ret

	# we are not so we need set it
	set_val = __salt__['softwareupdate.schedule_enable'](name)

	if not set_val:
		ret['result'] = False
		ret['comment'] = 'Failed to set Software update schedule.'
	else:
		ret['comment'] = 'Software update schedule has '\
			'been set to {0}'.format(name)
		ret['changes'].update({'schedule': {'old': old_schedule,
									  		'new': name}})
	return ret
