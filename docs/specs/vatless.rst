.. doctest docs/specs/vatless.rst
.. _welfare.specs.vatless:

=================
Incoming invoices
=================


This document is based on and extends :ref:`welfare.specs.ledger`.

.. contents::
   :depth: 1
   :local:

Code snipptest in this document are tested on the
:mod:`lino_weleup.demo` demo project.

>>> from lino import startup
>>> startup('lino_weleup.demo.settings.doctests')
>>> from lino.api.doctest import *
>>> from lino.api import rt


Incoming invoices
=================

In Lino Welfare, **incoming invoices** are different from "real"
incoming invoices in that their recipient is some client of the
center, not to the center itself. The center has no direct legal
obligation, it just agrees (or not) to pay these invoices in the name
of their client.

There are two types of incoming invoices: "simple" and "collective".
The demo database has two journals with *incoming invoices*, one for
each type, referenced as "REG" (for German *Rechnungseingang*) and
SREG (*Sammelrechnungen*).

>>> REG = ledger.Journal.get_by_ref('REG')
>>> REG.voucher_type.table_class
lino_xl.lib.vatless.ui.ProjectInvoicesByJournal

>>> SREG = ledger.Journal.get_by_ref('SREG')
>>> SREG.voucher_type.table_class
lino_xl.lib.vatless.ui.InvoicesByJournal

The REG journal contains the following invoices:

>>> rt.show(REG.voucher_type.table_class, REG)
======================= =============== ============================ =============================== ============ ============== ================== =================
 Nr.                     Buchungsdatum   Klient                       Zahlungsempfänger               Betrag       Zahlungsziel   Autor              Workflow
----------------------- --------------- ---------------------------- ------------------------------- ------------ -------------- ------------------ -----------------
 1/2013                  28.12.13        EVERS Eberhart (127)         Leffin Electronics              12,50        27.01.14       Wilfried Willems   **Registriert**
 19/2014                 07.01.14        EVERS Eberhart (127)         Ethias s.a.                     5,33         06.02.14       Wilfried Willems   **Registriert**
 18/2014                 12.01.14        COLLARD Charlotte (118)      Electrabel Customer Solutions   120,00       11.02.14       Wilfried Willems   **Registriert**
 17/2014                 22.01.14        EVERS Eberhart (127)         Maksu- ja tolliamet             120,00       21.02.14       Wilfried Willems   **Registriert**
 16/2014                 27.01.14        COLLARD Charlotte (118)      IIZI kindlustusmaakler AS       29,95        26.02.14       Wilfried Willems   **Registriert**
 15/2014                 06.02.14        COLLARD Charlotte (118)      AS Matsalu Veevärk              12,50        08.03.14       Wilfried Willems   **Registriert**
 14/2014                 11.02.14        EMONTS Daniel (128)          AS Express Post                 10,00        13.03.14       Wilfried Willems   **Registriert**
 13/2014                 21.02.14        COLLARD Charlotte (118)      Niederau Eupen AG               10,00        23.03.14       Wilfried Willems   **Registriert**
 12/2014                 26.02.14        EMONTS Daniel (128)          Ethias s.a.                     5,33         28.03.14       Wilfried Willems   **Registriert**
 11/2014                 08.03.14        EMONTS Daniel (128)          Ragn-Sells AS                   29,95        07.04.14       Wilfried Willems   **Registriert**
 10/2014                 13.03.14        DOBBELSTEIN Dorothée (124)   Maksu- ja tolliamet             25,00        12.04.14       Wilfried Willems   **Registriert**
 9/2014                  23.03.14        EMONTS Daniel (128)          Eesti Energia AS                25,00        22.04.14       Wilfried Willems   **Registriert**
 8/2014                  28.03.14        DOBBELSTEIN Dorothée (124)   AS Matsalu Veevärk              12,50        27.04.14       Wilfried Willems   **Registriert**
 7/2014                  07.04.14        DOBBELSTEIN Dorothée (124)   Leffin Electronics              5,33         07.05.14       Wilfried Willems   **Registriert**
 6/2014                  12.04.14        AUSDEMWALD Alfons (116)      Niederau Eupen AG               120,00       12.05.14       Wilfried Willems   **Registriert**
 5/2014                  22.04.14        DOBBELSTEIN Dorothée (124)   Electrabel Customer Solutions   120,00       22.05.14       Wilfried Willems   **Registriert**
 4/2014                  27.04.14        AUSDEMWALD Alfons (116)      Ragn-Sells AS                   29,95        27.05.14       Wilfried Willems   **Registriert**
 3/2014                  07.05.14        AUSDEMWALD Alfons (116)      IIZI kindlustusmaakler AS       12,50        06.06.14       Wilfried Willems   **Registriert**
 2/2014                  12.05.14        EVERS Eberhart (127)         Eesti Energia AS                10,00        11.06.14       Wilfried Willems   **Registriert**
 1/2014                  22.05.14        AUSDEMWALD Alfons (116)      AS Express Post                 10,00        21.06.14       Wilfried Willems   **Registriert**
 **Total (20 Zeilen)**                                                                                **725,84**
======================= =============== ============================ =============================== ============ ============== ================== =================
<BLANKLINE>



Collective invoices
===================

The SREG journal contains the following invoices:

>>> rt.show(SREG.voucher_type.table_class, SREG)
======================= =============== =============================== ============== ============== ================== =================
 Nr.                     Buchungsdatum   Zahlungsempfänger               Betrag         Zahlungsziel   Autor              Workflow
----------------------- --------------- ------------------------------- -------------- -------------- ------------------ -----------------
 10/2014                 02.01.14        Niederau Eupen AG               212,78         01.02.14       Wilfried Willems   **Registriert**
 9/2014                  17.01.14        Ragn-Sells AS                   82,78          16.02.14       Wilfried Willems   **Registriert**
 8/2014                  01.02.14        Eesti Energia AS                227,78         03.03.14       Wilfried Willems   **Registriert**
 7/2014                  16.02.14        Leffin Electronics              192,78         18.03.14       Wilfried Willems   **Registriert**
 6/2014                  03.03.14        Electrabel Customer Solutions   322,78         02.04.14       Wilfried Willems   **Registriert**
 5/2014                  18.03.14        IIZI kindlustusmaakler AS       177,78         17.04.14       Wilfried Willems   **Registriert**
 4/2014                  02.04.14        AS Express Post                 212,78         02.05.14       Wilfried Willems   **Registriert**
 3/2014                  17.04.14        Ethias s.a.                     82,78          17.05.14       Wilfried Willems   **Registriert**
 2/2014                  02.05.14        Maksu- ja tolliamet             227,78         01.06.14       Wilfried Willems   **Registriert**
 1/2014                  17.05.14        AS Matsalu Veevärk              192,78         16.06.14       Wilfried Willems   **Registriert**
 **Total (10 Zeilen)**                                                   **1 932,80**
======================= =============== =============================== ============== ============== ================== =================
<BLANKLINE>


Incoming invoices, partners and clients
=======================================

Let's have a closer look at an incoming invoice:
    
>>> obj = SREG.voucher_type.model.objects.get(number=3, journal=SREG)

The partner of this invoice is Ethias:

>>> obj.partner
Partner #227 ('Ethias s.a.')

It is a collective invoice whose costs are distributed over five
clients:

>>> rt.login('wilfried').show(rt.models.vatless.ItemsByInvoice, obj)
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE +REPORT_UDIFF
============================ =================================== =========== ============== ============
 Klient                       Haushaltsartikel                    Betrag      Beschreibung   Bearbeiten
---------------------------- ----------------------------------- ----------- -------------- ------------
 EMONTS Daniel (128)          (832/330/01) Allgemeine Beihilfen   5,33
 AUSDEMWALD Alfons (116)      (832/330/01) Allgemeine Beihilfen   10,00
 COLLARD Charlotte (118)      (832/330/01) Allgemeine Beihilfen   12,50
 DOBBELSTEIN Dorothée (124)   (832/330/01) Allgemeine Beihilfen   25,00
 EVERS Eberhart (127)         (832/330/01) Allgemeine Beihilfen   29,95
 **Total (5 Zeilen)**                                             **82,78**
============================ =================================== =========== ============== ============
<BLANKLINE>


This invoice is registered, and ledger movements have been created:

>>> obj.state
<VoucherStates.registered:20>
>>> rt.show(rt.models.ledger.MovementsByVoucher, obj)
=================================== ============================ =================== =========== =========== ================= ===========
 Haushaltsartikel                    Klient                       Zahlungsempfänger   Debit       Kredit      Match             Beglichen
----------------------------------- ---------------------------- ------------------- ----------- ----------- ----------------- -----------
 (4400) Lieferanten                  AUSDEMWALD Alfons (116)      Ethias s.a.                     10,00       **SREG 3/2014**   Nein
 (4400) Lieferanten                  COLLARD Charlotte (118)      Ethias s.a.                     12,50       **SREG 3/2014**   Nein
 (4400) Lieferanten                  DOBBELSTEIN Dorothée (124)   Ethias s.a.                     25,00       **SREG 3/2014**   Nein
 (4400) Lieferanten                  EVERS Eberhart (127)         Ethias s.a.                     29,95       **SREG 3/2014**   Nein
 (4400) Lieferanten                  EMONTS Daniel (128)          Ethias s.a.                     5,33        **SREG 3/2014**   Nein
 (832/330/01) Allgemeine Beihilfen   AUSDEMWALD Alfons (116)                          10,00                                     Ja
 (832/330/01) Allgemeine Beihilfen   COLLARD Charlotte (118)                          12,50                                     Ja
 (832/330/01) Allgemeine Beihilfen   DOBBELSTEIN Dorothée (124)                       25,00                                     Ja
 (832/330/01) Allgemeine Beihilfen   EVERS Eberhart (127)                             29,95                                     Ja
 (832/330/01) Allgemeine Beihilfen   EMONTS Daniel (128)                              5,33                                      Ja
                                                                                      **82,78**   **82,78**
=================================== ============================ =================== =========== =========== ================= ===========
<BLANKLINE>


The first five movements are *cleared* because their account is not
:attr:`clearable <lino_xl.lib.ledger.Account.clearable>`.

>>> cost_account = rt.models.ledger.Account.objects.get(ref="832/330/01")
>>> cost_account.clearable
False

The other five movements go into the suppliers account, which is
clearable:

>>> suppliers_account = rt.models.ledger.Account.objects.get(ref="4400")
>>> suppliers_account.clearable
True

The match rules table defines how to clear these movements:

>>> rt.show(ledger.MatchRulesByAccount, suppliers_account)
==========================
 Journal
--------------------------
 Ausgabeanweisungen (AAW)
==========================
<BLANKLINE>

This rule means: "Uncleared amounts in the suppliers account may be
cleared by the AAW (disbursement instructions) journal".

Since AAW is a financial journal, our story continues in :doc:`finan`.





Registering new incoming invoices
=================================

It is possible to create new invoices from the detail view of a partner.

The partner is usually some company.

>>> obj.partner
Partner #227 ('Ethias s.a.')

>>> rt.login('rolf').show(rt.models.vatless.VouchersByPartner, obj.partner)
Beleg erstellen in Journal **Sammelrechnungen (SREG)**, **Rechnungseingänge (REG)**

Our partner has 11 movements which are not yet *cleared*.

>>> rt.show(rt.models.ledger.MovementsByPartner, obj.partner)
**15 offene Bewegungen (-93.44 €)**

Let's look at the detail of these movements:

>>> rt.show(rt.models.ledger.MovementsByPartner, obj.partner, nosummary=True)
========== =============== ==================================================================== =========== ============ ================= ===========
 Valuta     Beleg           Beschreibung                                                         Debit       Kredit       Match             Beglichen
---------- --------------- -------------------------------------------------------------------- ----------- ------------ ----------------- -----------
 21.04.14   *ZKBC 4/2014*   *(4300) Offene Zahlungsaufträge* / *EMONTS Daniel (128)*                         5,33         **REG 12/2014**   Nein
 21.04.14   *ZKBC 4/2014*   *(4450) Auszuführende Ausgabeanweisungen* / *EMONTS Daniel (128)*    5,33                     **REG 12/2014**   Ja
 17.04.14   *SREG 3/2014*   *(4400) Lieferanten* / *AUSDEMWALD Alfons (116)*                                 10,00        **SREG 3/2014**   Nein
 17.04.14   *SREG 3/2014*   *(4400) Lieferanten* / *COLLARD Charlotte (118)*                                 12,50        **SREG 3/2014**   Nein
 17.04.14   *SREG 3/2014*   *(4400) Lieferanten* / *DOBBELSTEIN Dorothée (124)*                              25,00        **SREG 3/2014**   Nein
 17.04.14   *SREG 3/2014*   *(4400) Lieferanten* / *EVERS Eberhart (127)*                                    29,95        **SREG 3/2014**   Nein
 17.04.14   *SREG 3/2014*   *(4400) Lieferanten* / *EMONTS Daniel (128)*                                     5,33         **SREG 3/2014**   Nein
 21.03.14   *ZKBC 3/2014*   *(4300) Offene Zahlungsaufträge* / *EMONTS Daniel (128)*                         5,33         **REG 12/2014**   Nein
 21.03.14   *ZKBC 3/2014*   *(4400) Lieferanten* / *EMONTS Daniel (128)*                         5,33                     **REG 12/2014**   Nein
 13.03.14   *AAW 21/2014*   *(4400) Lieferanten* / *EMONTS Daniel (128)*                         5,33                     **REG 12/2014**   Nein
 13.03.14   *AAW 21/2014*   *(4450) Auszuführende Ausgabeanweisungen* / *EMONTS Daniel (128)*                5,33         **REG 12/2014**   Ja
 26.02.14   *REG 12/2014*   *(4400) Lieferanten* / *EMONTS Daniel (128)*                                     5,33         **REG 12/2014**   Nein
 21.02.14   *ZKBC 2/2014*   *(4300) Offene Zahlungsaufträge* / *EVERS Eberhart (127)*                        5,33         **REG 19/2014**   Nein
 21.02.14   *ZKBC 2/2014*   *(4450) Auszuführende Ausgabeanweisungen* / *EVERS Eberhart (127)*   5,33                     **REG 19/2014**   Ja
 21.01.14   *ZKBC 1/2014*   *(4300) Offene Zahlungsaufträge* / *EVERS Eberhart (127)*                        5,33         **REG 19/2014**   Nein
 21.01.14   *ZKBC 1/2014*   *(4400) Lieferanten* / *EVERS Eberhart (127)*                        5,33                     **REG 19/2014**   Nein
 13.01.14   *AAW 19/2014*   *(4400) Lieferanten* / *EVERS Eberhart (127)*                        5,33                     **REG 19/2014**   Nein
 13.01.14   *AAW 19/2014*   *(4450) Auszuführende Ausgabeanweisungen* / *EVERS Eberhart (127)*               5,33         **REG 19/2014**   Ja
 07.01.14   *REG 19/2014*   *(4400) Lieferanten* / *EVERS Eberhart (127)*                                    5,33         **REG 19/2014**   Nein
                            **Saldo -93.44 (19 Bewegungen)**                                     **31,98**   **125,42**
========== =============== ==================================================================== =========== ============ ================= ===========
<BLANKLINE>

The first two movements are invoices which have been admitted for
payment (i.e. a disbursement instruction (AAW) has been registered),
but the payment has not yet been executed.

Let's look at one of these movements via its client.

>>> client = rt.models.pcsw.Client.objects.get(pk=128)
>>> print(client)
EMONTS Daniel (128)

Our client has lots of other open transactions:

>>> rt.show(ledger.MovementsByProject, client)
... #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE +REPORT_UDIFF
========== =============== ================================================================================================== =============== =============== ================== ===========
 Valuta     Beleg           Beschreibung                                                                                       Debit           Kredit          Match              Beglichen
---------- --------------- -------------------------------------------------------------------------------------------------- --------------- --------------- ------------------ -----------
 22.05.14   *AAW 1/2014*    *(832/330/01) Allgemeine Beihilfen* / Allgemeine Beihilfen / *Emonts Daniel*                                       648,91          **AAW 1:5**        Nein
 22.05.14   *AAW 1/2014*    *(4450) Auszuführende Ausgabeanweisungen* / Allgemeine Beihilfen / *Emonts Daniel*                 648,91                          **AAW 1:5**        Nein
 22.05.14   *AAW 2/2014*    *(832/330/03) Heizkosten- u. Energiebeihilfe* / Heizkosten- u. Energiebeihilfe / *Emonts Daniel*                   817,36          **AAW 2:5**        Nein
 22.05.14   *AAW 2/2014*    *(4450) Auszuführende Ausgabeanweisungen* / Heizkosten- u. Energiebeihilfe / *Emonts Daniel*       817,36                          **AAW 2:5**        Nein
 22.05.14   *AAW 3/2014*    *(832/330/03F) Fonds Gas und Elektrizität* / Fonds Gas und Elektrizität / *Emonts Daniel*                          544,91          **AAW 3:5**        Nein
 22.05.14   *AAW 3/2014*    *(4450) Auszuführende Ausgabeanweisungen* / Fonds Gas und Elektrizität / *Emonts Daniel*           544,91                          **AAW 3:5**        Nein
 22.05.14   *AAW 4/2014*    *(832/3331/01) Eingliederungseinkommen* / Eingliederungseinkommen / *Emonts Daniel*                                800,08          **AAW 4:5**        Nein
 22.05.14   *AAW 4/2014*    *(4450) Auszuführende Ausgabeanweisungen* / Eingliederungseinkommen / *Emonts Daniel*              800,08                          **AAW 4:5**        Nein
 ...
 08.03.14   *REG 11/2014*   *(4400) Lieferanten* / *Ragn-Sells AS*                                                                             29,95           **REG 11/2014**    Nein
 26.02.14   *REG 12/2014*   *(4400) Lieferanten* / *Ethias s.a.*                                                                               5,33            **REG 12/2014**    Nein
 21.02.14   *ZKBC 2/2014*   *(4400) Lieferanten* / *AS Express Post*                                                           10,00                           **REG 14/2014**    Nein
 21.02.14   *ZKBC 2/2014*   *(4300) Offene Zahlungsaufträge* / *AS Express Post*                                                               10,00           **REG 14/2014**    Nein
 21.02.14   *ZKBC 2/2014*   *(4300) Offene Zahlungsaufträge* / *Eesti Energia AS*                                                              54,95           **SREG 8/2014**    Nein
 21.02.14   *ZKBC 2/2014*   *(4300) Offene Zahlungsaufträge* / *Ragn-Sells AS*                                                                 29,95           **SREG 9/2014**    Nein
 13.02.14   *AAW 20/2014*   *(4400) Lieferanten* / *AS Express Post*                                                           10,00                           **REG 14/2014**    Nein
 11.02.14   *REG 14/2014*   *(4400) Lieferanten* / *AS Express Post*                                                                           10,00           **REG 14/2014**    Nein
 21.01.14   *ZKBC 1/2014*   *(4300) Offene Zahlungsaufträge* / *Niederau Eupen AG*                                                             120,00          **SREG 10/2014**   Nein
                            **Saldo -493.29 (78 Bewegungen)**                                                                  **17 129,40**   **17 622,69**
========== =============== ================================================================================================== =============== =============== ================== ===========
<BLANKLINE>




.. _welfare.specs.r20160105:


Some choices requests
=====================

>>> kw = dict()
>>> fields = 'count rows'
>>> mt = contenttypes.ContentType.objects.get_for_model(vatless.InvoiceItem).pk
>>> demo_get(
...    'wilfried', 'choices/vatless/ItemsByProjectInvoice/account',
...    fields, 22, mt=mt, mk=1, **kw)

