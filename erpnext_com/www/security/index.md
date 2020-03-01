<section class='top-section'>
<h1>Reporting Security Vulnerabilities</h1>
</section>

While we try to be proactive in preventing security problems, we do not assume they’ll never come up.

It is standard practice to responsibly and privately disclose a security problem to the vendor i.e. Frappe core development team before publicising, so a fix can be prepared, and damage from the vulnerability minimised.

#### Policy

You are responsible for complying with all applicable laws and must only ever use or otherwise access your own test accounts when researching vulnerabilities in any of our products or services. Access to, or modification of user data is explicitly prohibited without prior consent from the account owner.

#### Qualifying Vulnerabilities

Any reproducible vulnerability that affects the security of our users is likely to be in scope.

Common examples include:

* Remote Code Execution (RCE)
* SQL Injection (SQLi)
* Code Injection
* Buffer Overflow
* Unvalidated Input
* Access-Control Problem
* Race Condition
* Remote Code Execution
* Weaknesses in Authentication, Authorization, or Cryptographic Practices


#### Security Vulnerability Submission

If you find any security breaches, please report the issue to <a href='/security/report'>via this form</a>

It is important to include at least the following information in the email:

* Organization and contact name
* Your Reference / Advisory Number
* Description of the potential vulnerability
* Supporting technical details (such as system configuration, traces, description of exploit/attack code, sample packet capture, proof of concept, steps to reproduce the issue)
* Information about known exploits
* Disclosure plans, if any
* If you want public recognition

Please allow a reasonable time (2-4 days) for us to confirm and respond to the issue after reporting.

#### Tentative Rewards

Type of vulnerability| Award
------|--------
Unvalidated Input | $100
Access-Control Problem | $200
Weaknesses in Authentication, Authorization, or Cryptographic Practices | $300
Remote Code Execution (RCE) | $500
SQL Injection (SQLi) | $700

#### List of Known Vulnerabilities

To view a list of known vulnerabilities that have already been fixed in the system, please visit the [CVE References Page](/security/references).

<p class='text-center'>
    <a href='/security/report' class='btn btn-secondary'>
    Report a Vulnerability</a>
</p>
