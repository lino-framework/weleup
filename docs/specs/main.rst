.. doctest docs/specs/main.rst
.. _welfare.specs.main:

===================
The admin main page
===================

This describes the main page of :ref:`welfare`.

.. contents::
   :depth: 1

.. include:: /include/tested.rst
  
>>> from lino import startup
>>> startup('lino_weleup.demo.settings.doctests')
>>> from lino.api.doctest import *

Some tests
==========
           
Test the content of the admin main page.

>>> test_client.force_login(rt.login('rolf').user)
>>> res = test_client.get('/api/main_html', REMOTE_USER='rolf')
>>> print(res.status_code)
200
>>> result = json.loads(res.content)
>>> result['success']
True
>>> # print(html2text(result['html']))
>>> soup = BeautifulSoup(result['html'], 'lxml')

We might test the complete content here, but currently we skip this as
it is much work to maintain.

>>> print(soup.get_text(' ', strip=True))
... #doctest: +NORMALIZE_WHITESPACE +REPORT_CDIFF +SKIP

>>> links = soup.find_all('a')
>>> len(links)
120

>>> print(links[0].text)
Suchen

>>> tables = soup.find_all('table')
>>> len(tables)
4

>>> for h in soup.find_all('h2'):
...     print(h.text.strip())
Benutzer und ihre Klienten ⏏
Wartende Besucher ⏏
Meine Termine  ⏏
Meine überfälligen Termine  ⏏
Meine Benachrichtigungen ✓ ⏏


>>> test_client.force_login(rt.login('robin').user)
>>> res = test_client.get('/api/main_html', REMOTE_USER='robin')
>>> print(res.status_code)
200
>>> result = json.loads(res.content)
>>> soup = BeautifulSoup(result['html'], 'lxml')
>>> for h in soup.find_all('h2'):
...     print(h.text.strip())
Users with their Clients ⏏
Waiting visitors ⏏
My appointments  ⏏
My overdue appointments  ⏏
My Notification messages ✓ ⏏


Here is a text variant of Hubert's dashboard.
Not tested because some details are changing in the demo database.

>>> rt.login('hubert').show_dashboard()
... #doctest: +NORMALIZE_WHITESPACE +REPORT_CDIFF +SKIP
---------------------------------------------------------
Users with their Clients `⏏ <Users with their Clients>`__
---------------------------------------------------------
<BLANKLINE>
==================== ============ ============ ======== ======== ========= ================= ================ ========
 Coach                Auswertung   Ausbildung   Suchen   Arbeit   Standby   Primary clients   Active clients   Total
-------------------- ------------ ------------ -------- -------- --------- ----------------- ---------------- --------
 Alicia Allmanns      **4**        **1**                 **1**    **1**     **3**             **3**            **7**
 Hubert Huppertz      **5**        **4**        **6**    **1**    **1**     **14**            **14**           **17**
 Mélanie Mélard       **2**        **4**        **6**    **4**    **3**     **10**            **10**           **19**
 **Total (3 rows)**   **11**       **9**        **12**   **6**    **5**     **27**            **27**           **43**
==================== ============ ============ ======== ======== ========= ================= ================ ========
<BLANKLINE>
-------------------------------------------------------
Visitors waiting for me `⏏ <Visitors waiting for me>`__
-------------------------------------------------------
<BLANKLINE>
==================================== ===================== ========== =================== =======================================================
 Since                                Client                Position   Short description   Workflow
------------------------------------ --------------------- ---------- ------------------- -------------------------------------------------------
 `... <Detail>`__   EMONTS Daniel (128)   1                              [Receive] [Checkout] **Waiting** → [Absent] [Excused]
 `... <Detail>`__   JONAS Josef (139)     2                              [Receive] [Checkout] **Waiting** → [Absent] [Excused]
 `... <Detail>`__   LAZARUS Line (144)    3                              [Receive] [Checkout] **Waiting** → [Absent] [Excused]
==================================== ===================== ========== =================== =======================================================
<BLANKLINE>
-----------------------------------------
Waiting visitors `⏏ <Waiting visitors>`__
-----------------------------------------
<BLANKLINE>
==================================== ========================= ================= ========== =================== =======================================================
 Since                                Client                    Managed by        Position   Short description   Workflow
------------------------------------ ------------------------- ----------------- ---------- ------------------- -------------------------------------------------------
 `... <Detail>`__   EMONTS Daniel (128)       Hubert Huppertz   1                              [Receive] [Checkout] **Waiting** → [Absent] [Excused]
 `... <Detail>`__   EVERS Eberhart (127)      Mélanie Mélard    1          Urgent problem      **Waiting** → [Absent] [Excused]
 `... <Detail>`__   HILGERS Hildegard (133)   Alicia Allmanns   1          Beschwerde          **Waiting** → [Absent] [Excused]
 `... <Detail>`__   JACOBS Jacqueline (137)   Judith Jousten    1          Information         **Waiting** → [Absent] [Excused]
 `... <Detail>`__   JONAS Josef (139)         Hubert Huppertz   2                              [Receive] [Checkout] **Waiting** → [Absent] [Excused]
 `... <Detail>`__   KAIVERS Karl (141)        Alicia Allmanns   2          Beschwerde          **Waiting** → [Absent] [Excused]
 `... <Detail>`__   LAMBERTZ Guido (142)      Mélanie Mélard    2          Urgent problem      **Waiting** → [Absent] [Excused]
 `... <Detail>`__   LAZARUS Line (144)        Hubert Huppertz   3                              [Receive] [Checkout] **Waiting** → [Absent] [Excused]
==================================== ========================= ================= ========== =================== =======================================================
<BLANKLINE>
-----------------------------------------------
My appointments **New** `⏏ <My appointments>`__
-----------------------------------------------
<BLANKLINE>
====================================== ======================== ===================== =================== ===============================
 When                                   Client                   Calendar entry type   Short description   Workflow
-------------------------------------- ------------------------ --------------------- ------------------- -------------------------------
 `Mon 20/04/2015 at 09:00 <Detail>`__   BRECHT Bernd (177)       Evaluation            Auswertung 10       [▽] **? Suggested** → [☼] [☒]
 `Thu 09/04/2015 at 09:00 <Detail>`__   JEANÉMART Jérôme (181)   Evaluation            Auswertung 9        [▽] **? Suggested** → [☼] [☒]
 `Thu 19/03/2015 at 09:00 <Detail>`__   BRECHT Bernd (177)       Evaluation            Auswertung 9        [▽] **? Suggested** → [☼] [☒]
 `Mon 09/03/2015 at 09:00 <Detail>`__   JEANÉMART Jérôme (181)   Evaluation            Auswertung 8        [▽] **? Suggested** → [☼] [☒]
 `Tue 03/03/2015 <Detail>`__            DENON Denis (180*)       Evaluation            Auswertung 4        [▽] **? Suggested** → [☼] [☒]
 `Thu 19/02/2015 at 09:00 <Detail>`__   BRECHT Bernd (177)       Evaluation            Auswertung 8        [▽] **? Suggested** → [☼] [☒]
 `Mon 09/02/2015 at 09:00 <Detail>`__   JEANÉMART Jérôme (181)   Evaluation            Auswertung 7        [▽] **? Suggested** → [☼] [☒]
 `Mon 19/01/2015 at 09:00 <Detail>`__   BRECHT Bernd (177)       Evaluation            Auswertung 7        [▽] **? Suggested** → [☼] [☒]
 `Thu 08/01/2015 at 09:00 <Detail>`__   JEANÉMART Jérôme (181)   Evaluation            Auswertung 6        [▽] **? Suggested** → [☼] [☒]
 `Wed 17/12/2014 at 09:00 <Detail>`__   BRECHT Bernd (177)       Evaluation            Auswertung 6        [▽] **? Suggested** → [☼] [☒]
 `Mon 08/12/2014 at 09:00 <Detail>`__   JEANÉMART Jérôme (181)   Evaluation            Auswertung 5        [▽] **? Suggested** → [☼] [☒]
 `Wed 03/12/2014 <Detail>`__            DENON Denis (180*)       Evaluation            Auswertung 3        [▽] **? Suggested** → [☼] [☒]
 `Mon 17/11/2014 at 09:00 <Detail>`__   BRECHT Bernd (177)       Evaluation            Auswertung 5        [▽] **? Suggested** → [☼] [☒]
 `Wed 12/11/2014 <Detail>`__            RADERMECKER Rik (173)    Evaluation            Auswertung 3        [▽] **? Suggested** → [☼] [☒]
 `Thu 06/11/2014 at 09:00 <Detail>`__   JEANÉMART Jérôme (181)   Evaluation            Auswertung 4        [▽] **? Suggested** → [☼] [☒]
====================================== ======================== ===================== =================== ===============================
<BLANKLINE>
---------------------------------------------------------------
My overdue appointments **New** `⏏ <My overdue appointments>`__
---------------------------------------------------------------
<BLANKLINE>
=========================================================================== ========================================================== ===================== ===============================
 Description                                                                 Controlled by                                              Calendar entry type   Workflow
--------------------------------------------------------------------------- ---------------------------------------------------------- --------------------- -------------------------------
 `Évaluation 14 (19.05.2014 09:00) with JEANÉMART Jérôme (181) <Detail>`__   `ISIP#32 (Jérôme JEANÉMART) <Detail>`__                    Evaluation            [▽] **? Suggested** → [☑] [☒]
 `Auswertung 1 (12.05.2014) with RADERMECKER Rik (173) <Detail>`__           `Art60§7 job supplyment#14 (Rik RADERMECKER) <Detail>`__   Evaluation            [▽] **? Suggested** → [☑] [☒]
... 
 `Évaluation 10 (16.01.2014 09:00) with JEANÉMART Jérôme (181) <Detail>`__   `ISIP#32 (Jérôme JEANÉMART) <Detail>`__                    Evaluation            [▽] **? Suggested** → [☑] [☒]
=========================================================================== ========================================================== ===================== ===============================
<BLANKLINE>
---------------------------------------------------------
My Notification messages `⏏ <My Notification messages>`__
---------------------------------------------------------
<BLANKLINE>
===================== ==================================== ============== ==========
 Created               Subject                              Message Type   Workflow
--------------------- ------------------------------------ -------------- ----------
 2014-05-22 05:48:00   Die Datenbank wurde initialisiert.   System event   [✓]
===================== ==================================== ============== ==========
<BLANKLINE>
