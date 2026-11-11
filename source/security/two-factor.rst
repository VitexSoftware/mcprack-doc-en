Two-factor authentication
=========================

Every account — local or LDAP — can protect its sign-in with a time-based one-time
code (TOTP, RFC 6238: FreeOTP, Aegis, Google Authenticator or any authenticator
app). **Administrators must have it.**

Signing in
----------

With two-factor authentication on, signing in has two steps: the password, then
the six-digit code (or one of the recovery codes). A correct password alone does
not create a session. The step between them lasts ``MFA_PENDING_SECONDS`` (300)
and is cancelled if the account changes meanwhile.

- A code works **once**: the time step of the last accepted code is recorded
  atomically, so the same code cannot be replayed within its validity.
- Wrong codes count toward the same lock-out as wrong passwords. A correct
  password is *not* a finished sign-in, so it does not clear the counters —
  otherwise whoever knows the password could guess the code without limit.
- Recovery codes are single-use. Typing them in any case or spacing works.

Setting it up
-------------

User menu → *Two-factor authentication* → *Set up*:

1. Confirm your password.
2. Enter the displayed key into your authenticator app (time-based, six digits),
   or import the ``otpauth://`` address shown below it. There is no QR code.
3. Enter the code the app shows.
4. Save the **ten recovery codes** that are displayed once.

Until the code is confirmed nothing is switched on, so an unfinished set-up never
locks anybody out. Switching it on ends the account's *other* sessions.

Turning it off, new recovery codes
----------------------------------

Both need the current password **and** a code, and are audited. Administrators
cannot turn it off.

Required for administrators
---------------------------

``MFA_REQUIRED_FOR_ADMINS`` (default ``true``). An administrator without a second
factor is sent to the set-up page instead of the admin area, and the admin REST API
answers ``403`` with the code ``mfa_required`` to their browser session. They also
cannot create an API token that reaches the admin API (an unrestricted token, or a
scope starting ``admin:``). API tokens that already exist are not asked for a
code. The public demo is exempt.

If a user loses the device and the recovery codes
-------------------------------------------------

An administrator resets the factor: *Admin → Users → Reset two-factor
authentication*, or ``POST /api/v1/admin/users/{id}/mfa-reset``. A locked-out
administrator uses the server:

.. code-block:: bash

   sudo mcprack user mfa-status alice
   sudo mcprack user mfa-reset alice

A reset ends the user's sessions and is audited (``mfa_change``).

Storage
-------

The shared secret is encrypted with the key hierarchy of the local secret store
(``SECRET_KEY`` and ``SECRET_KEY_FALLBACKS``). Recovery codes are stored only as
keyed hashes. Options: ``MFA_ISSUER`` (the name shown in the app),
``MFA_PENDING_SECONDS``, ``MFA_RECOVERY_CODE_COUNT``.
