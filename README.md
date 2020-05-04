# nethserver-automx
NethServer configuration for automx

## Description
This package configures Nethserver 7 for automx.  It contains templates for the automx config file and Apache configuration, as well as events to rebuild those files and restart the relevant services.  For further information on the purpose and usage of this package, see [the NethServer wiki](https://wiki.nethserver.org/doku.php?id=email_autoconfig_module).

## Configuration
This package defines one configuration database key, `automx`.

### automx properties

|Property|Default|Description|
|-----|-----|-----|
|CertPath||If enabling SignMobileConfig (see below), this must be set to the path to a full certificate chain (leaf certificate and any intermediate certs) that automx can read.|
|Debug|disabled|Set to "enabled" to log verbosely.|
|ImapHost||Set if you want to specify the IMAP server name.  If not set, will default to your server's FQDN as configured in the server manager.|
|KeyPath||If enabling SignMobileConfig (see below), this must be set to the path to the corresponding private key that automx can read.|
|SignMobileConfig|disabled|Sign .mobileconfig profiles with a TLS certificate/key, set to "enabled" to enable.|
|SmtpHost||Set if you want to specify the SMTP server name.  If not set, will default to your server's FQDN as configured in the server manager.|
|UseLdap|disabled|Attempt to pull users' display names from the system LDAP service.  Set to "enabled" to enable.|

After changing any configuration properties, rebuild the configuration file and restart the services with `signal-event nethserver-automx-update`.

## Known issues
* Signed mobile config files only include the leaf-certificate, not intermediate certs.  As a result, they appear as "unverified".
* Pulling users' display names from the LDAP server doesn't seem to work properly.

## To do

* Migrate to [automx2](https://gitlab.com/automx/automx2), as automx is EOL.
