==============
Coming version
==============

These are the :term:`release notes` for the coming :ref:`weleup` version, which
will probably be 20.2.0.

This release is mainly for technical reasons to migrate from Python 2 to 3 and
from Debian Lenny to Buster.

.. contents::
  :local:

TODO
====

- remove the new calendar view (to reduce number of unrequested changes)? If
  yes: how? For example by moving the calendar view into a separate plugin
  "calview")

- check cron jobs

- add a Partners.detail_layout (to reduce number of unrequested changes) ?

- presences by client : any changes?

- change 3rd language from nl to en?



Summary for end users
=====================

- Tx25 funktioniert wieder

- Bugfix "Falsche Altersberechnung" Steve 20190404.

- Vermerk "zzgl. MWSt." in Bescheinigung Schatztruhe (:ticket:`3142`).

- Man kann jetzt Texte direkt aus Word kopieren, ohne deshalb potentielle
  Probleme beim Ausdruck zu riskieren.
  (:ticket:`3026` "bleaching")

- Partner haben jetzt keine Detail-Ansicht mehr und man kann in der
  Partnerliste nicht mehr direkt einen abstrakten Partner erstellen, sondern muss
  dafür in Organisationen, Haushalte oder Personen oder Klienten gehen.

- Neue Tabelle :class:`lino.modlib.users.UserRoles` könnte
  hilfreich sein beim Formulieren von Änderungswünschen
  bzgl. Zugriffsrechten. (20181008)

- Vertragspartner einer VSE per Doppelklick eingeben (:ticket:`2619`). Hier
  kommt jetzt ein kleines Fenster mit den Feldern company und contact_person.
  Ein summary view mit Insert-Button (wie bei den Notizen) scheint Overkill,
  weil es selten mehr als 15 Vertragspartner gibt.



Technologisch bedingte Änderungen

- Die neue Version wird auf einem neuen Server laufen unter Debian 10 und Python
  3.

Zukunft / Vorschläge für neue Features

- Lino hat eine neue Kalenderansicht, die irgendwann das momentane System
  (:mod:`lino_xl.lib.extensible`) ersetzen wird.

- Irgendwann kommt der Umstieg auf die neue Benutzeroberfläche (:ref:`react`).
  Das könnten wir bei Gelegenheit mal testen.

- Desktop Notifications (:ticket:`923`).  Vorteile: (1) akustisches
  Signal, (2) kommt auch dann, wenn Lino minimiert ist, (3) belastet
  den Server nicht unnötig.
  Diese Änderung sollte vor der Einführung von den Benutzern
  ausprobiert werden können, denn DN bedeuten eine Änderung des
  Benutzerverhaltens: statt den Lino-Bildschirm offen zu halten und ab
  und zu drauf zu schauen, müssen sie sich daran gewöhnen, auf
  Desktop-Notifications zu achten. Davon abgesehen ist die
  Konfiguration der Clients nicht trivial: Wie lange bleiben sie am
  Bildschirm sichtbar? Kann man ihre Dauer auf "endlos" stellen?  Wie
  kann man ein akustisches Signal einstellen? Wie gehen die Benutzer
  bisher mit "Meine Mitteilungen" in Lino um?

- Lino könnte jetzt row-level edit locking für Klienten machen.

- intelligente Ansicht Termine auch für cal.EntriesByClient?


Requested changes
=================

- The Tx25 works again.  :mod:`lino_welfare.modlib.cbss`

- Fixed :ticket:`2946` (Wrong age display (leap year bug))

- Added a text "Tous les montants sont mentionnés hors T.V.A." in the
  :xfile:`aids/Confirmation/clothing_bank.body.html` template.

- Bleaching has been activated (:ticket:`3026`).

Unrequested changes
===================

The ordering of toolbar buttons changed slightly.

The actions "Merge" and "Duplicate" are no longer available on all models and
for everybody.  Only for "experts" and only for certain database models.

New database field :attr:`lino_xl.lib.cal.RecurrenceSet.positions` in the tables
:class:`cal.EventPolicy <lino_xl.lib.cal.EventPolicy>` (Recurrency policies),
:class:`cal.RecurrentEvent <lino_xl.lib.cal.RecurrentEvent>` and
:class:`isip.ExamPolicy <lino_welfare.modlib.isip.ExamPolicy>`.
Fixes :ticket:`3225`. (book 2019-10-08)

Fixed two unreported minor bugs:  The detail view of a calendar presence is now
in a smaller window than before. Because the biggest part of that window was not
used. In some views of a presence, Lino didn't show a pointer to "Client" but to
"Partner" (although in welfare the guest of a calendar entry are always
clients). (20181008)

The header of a detail view is now clickable and returns to the grid view.

Calendar entries by contract are now sorted in *descending* order (newest first).

The properties.PersonProperty model was renamed to cv.PersonProperty


Migration notes
===============

Migration is done as follows:

- on old site, run::

    $ go prod
    $ python manage.py dump2py -o snapshot2preview

  Note that there is a file :xfile:`restore2preview.py` in the :xfile:`snapshot2preview`
  directory which will not be touched. You can say::

    diff restore.py restore2preview.py

  to see the database changes that need a manual patch.

- on the new site, run::

    $ go prod
    $ a
    $ pull.sh
    $ ./initdb_from_prod.sh
    ¤ restart_services.sh





Technical notes
===============

>>> from lino import startup
>>> startup('lino_welfare.projects.gerd.settings.doctests')
>>> from lino.api.doctest import *

>>> from lino_xl.lib.cal.mixins import RecurrenceSet
>>> rt.models_by_base(RecurrenceSet)
[<class 'lino_xl.lib.cal.models.EventPolicy'>, <class 'lino_xl.lib.cal.models.RecurrentEvent'>, <class 'lino_welfare.modlib.isip.models.ExamPolicy'>]
