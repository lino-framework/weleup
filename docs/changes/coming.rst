==============
Coming version
==============

These are the :term:`release notes` for the coming :ref:`weleup` version, which
will probably be 20.2.0.

This release is mainly for technical reasons to migrate from Python 2 to 3 and
from Debian Lenny to Buster.

.. contents::
  :local:


Requested changes
=================

- The Tx25 works again.  :mod:`lino_welfare.modlib.cbss`

- Fixed :ticket:`2946` (Wrong age display (leap year bug)) (Steve 20190404
  "Falsche Altersberechnung")

- Added a text "Tous les montants sont mentionnés hors T.V.A." in the
  :xfile:`aids/Confirmation/clothing_bank.body.html` template. Vermerk "zzgl.
  MWSt." in Bescheinigung Schatztruhe (:ticket:`3142`).

- (:ticket:`3026` "bleaching")
  Man kann jetzt Texte direkt aus Word kopieren, ohne deshalb potentielle
  Probleme beim Ausdruck zu riskieren

Unrequested changes
===================

The ordering of toolbar buttons changed slightly.

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


Technologisch bedingte Änderungen

- Die neue Version wird auf einem neuen Server laufen unter Debian 10 und Python
  3.

- Lino hat eine neue Kalenderansicht, die irgendwann das momentane System
  (:mod:`lino_xl.lib.extensible`) ersetzen wird.

Ungefragte Änderungen:

- Im Titelbalken eines Detail-Fensters kann man jetzt zurück klicken.

- Termine eines Vertrags werden jetzt chronologisch absteigend
  angezeigt.

- Die Aktionen Merge und Duplicate sind jetzt nur noch für "Experten"
  sichtbar (d.h. Systemverwalter), und auch nicht mehr für alle
  Datenmodelle.

- properties.PersonProperty heißt jetzt cv.PersonProperty (erfordert
  Datenmigration)

- Partner haben jetzt keine Detail-Ansicht mehr und man kann in der
  Partnerliste nicht mehr direkt einen abstrakten Partner erstellen, sondern muss
  dafür in Organisationen, Haushalte oder Personen oder Klienten gehen.

Verschiedenes:

- Das Folgende war geplant, erwies sich dann aber als kompliziert:
  Nicht mehr mit Apache sondern mit nginx als Webserver.
  Authentifizierung wird weiterhin über den LDAP-Server, aber nicht mehr über
  die veraltete Methode "http auth", sondern man kann sich ein- und ausloggen,
  ohne den Browser neu zu starten.


TODO

- :ticket:`2619` Vertragspartner einer VSE per Doppelklick eingeben.

  Vorschlag : Für die nächste Version ein insert_layout definieren mit
  den Feldern company und contact_person. Ein summary view mit
  Insert-Button (wie bei den Notizen) scheint mir hier Overkill, weil
  es selten mehr als 15 Vertragspartner gibt.

Zu testen


- Optional auf Anfrage: intelligente Ansicht Termine auch für
  cal.EntriesByClient?

- Anwesenheiten pro Klient

Vorschläge für neue Features

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

- Neue Tabelle :class:`lino.modlib.users.UserRoles` könnte
  hilfreich sein beim Formulieren von Änderungswünschen
  bzgl. Zugriffsrechten. (20181008)

- Lino könnte jetzt row-level edit locking für Klienten machen.

- Irgendwann kommt der Umstieg auf die neue Benutzeroberfläche (:ref:`react`).
  Das könnten wir bei Gelgenheit mal testen.


Technisches:

- cron-Jobs prüfen und manuell rüber holen.


Technical notes
===============

>>> from lino import startup
>>> startup('lino_welfare.projects.gerd.settings.doctests')
>>> from lino.api.doctest import *

>>> from lino_xl.lib.cal.mixins import RecurrenceSet
>>> rt.models_by_base(RecurrenceSet)
[<class 'lino_xl.lib.cal.models.EventPolicy'>, <class 'lino_xl.lib.cal.models.RecurrentEvent'>, <class 'lino_welfare.modlib.isip.models.ExamPolicy'>]
