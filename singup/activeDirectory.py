import ldap
import sys
def create_user_activedirectory(username , password , name ):
    SCRIPT = 1
    ACCOUNTDISABLE = 2
    HOMEDIR_REQUIRED = 8
    PASSWD_NOTREQD = 32
    NORMAL_ACCOUNT = 544
    DONT_EXPIRE_PASSWORD = 65536
    TRUSTED_FOR_DELEGATION = 524288
    PASSWORD_EXPIRED = 8388608

#    conn=ldap.open("192.168.10.32")
    conn = ldap.initialize('ldap://192.168.10.42:389')
    conn.protocol_version=ldap.VERSION3
    conn.set_option(ldap.OPT_REFERRALS, 0)
    ldap.set_option(ldap.OPT_X_TLS_REQUIRE_CERT, ldap.OPT_X_TLS_NEVER)
    conn.simple_bind_s("administrator@xaas.local" , "function92")
    mymodlist = {
            "objectClass": ["top".encode('utf-8'), "person".encode('utf-8'), "organizationalPerson".encode('utf-8'), "user".encode('utf-8')],
            "cn": [str(username).encode('utf-8')],
            #"uid": [str(username).encode('utf-8')],
            "userPassword": [str(password).encode('iso-8859-1')],
            "userPrincipalName": [str(username+"@XaaS.local").encode('iso-8859-1')],
            "sAMAccountName": [str(username).encode('utf-8')],
            "givenName": [str(name).encode('iso-8859-1')],
            "sn": [str(name).encode('iso-8859-1')],
            "displayName": [str(name).encode('iso-8859-1')],
            "userAccountControl": [str(NORMAL_ACCOUNT).encode('iso-8859-1')],
        }
    dn="CN="+username+",OU=DaaSUsers,DC=XaaS,DC=local"
    conn.add_s(dn, ldap.modlist.addModlist(mymodlist))
    conn.unbind_s()

