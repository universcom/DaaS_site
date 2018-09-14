import ldap
import ldap.modlist as modlist
import string
import os , binascii

server = 'ldap://192.168.10.74:389'
ldap_pass = '123456q@'
ldap_bind = 'ou=users,dc=xaas,dc=local'

def create_user_ldap(username , password , name ):
    username = str(username)
    password=str(password)
    name=str(name)
    con = ldap.initialize(server)
    con.simple_bind_s("cn=admin,dc=xaas,dc=local", "123456q@")
    dn = "uid="+username+",ou=users,dc=xaas,dc=local"
    mymodlist = {
         "objectClass": ["account".encode('utf-8'), "posixAccount".encode('utf-8'), "shadowAccount" .encode('utf-8')],
        #"objectClass": [str("inetOrgPerson").encode('utf-8')],
        "cn":[str(name).encode('utf-8')],
        "uid": [str(username).encode('utf-8')],
        "uidNumber": [str("5025").encode('utf-8')],
        "gidNumber": [str("30033").encode('utf-8')],
        "homeDirectory": [str("/home/"+name).encode('utf-8')],
        "loginShell": ["/bin/bash".encode('utf-8')],
        "gecos" : [str(username).encode('utf-8')],
        "userPassword": [password.encode('utf-8')] ,
        "shadowLastChange": [str("0").encode('utf-8')],
        "shadowMax": [str("0").encode('utf-8')],
        "shadowWarning": [str("0").encode('utf-8')],
        #"sn": [str(name).encode('utf-8').encode('utf8')],
        #"givenName": [str(name).encode('utf-8')],
        #"displayName": [str(name).encode('utf-8')],
    }
    con.add_s(dn, ldap.modlist.addModlist(mymodlist))
    con.unbind_s()
    # l = ldap.initialize("ldap://31.184.135.5:389/")
    # l.simple_bind_s("cn=admin,dc=xaas,dc=local", "123456q@")
    # dn = "ou=users,dc=xaas,dc=local"
    # #a = '{CRYPT}' + '123'
    # top=str("top").encode('utf-8')
    # attrs = {}
    # attrs['objectClass'] = [top]
    # #attrs['objectclass'] = [str('organizationalRole'), str('simpleSecurityObject')]
    # #attrs['cn'] = str(username).encode('utf-8')
    # #attrs['userPassword'] = str(a)
    # #attrs['description'] = str('User object for replication using slurpd')
    # ldif = modlist.addModlist(attrs)
    # l.add_s(dn, ldif)
    # l.unbind_s()

def add_connection_to_user(connection_name , username , password):
    con = ldap.initialize(server)
    con.simple_bind_s("cn=admin,dc=xaas,dc=local", "123456q@")
    if connection_name == 1 :
        dn = " cn=matlab_"+username+",ou=groups,dc=xaas,dc=local"
        mymodlist = {
            "objectClass": ["guacConfigGroup".encode('utf-8') ,"groupOfNames".encode('utf-8')],
            "cn": [str("matlab_"+username).encode('utf-8')],
            "guacConfigProtocol": ["rdp".encode('utf-8')],
            "guacConfigParameter": [str("name=matlab_"+username).encode('utf-8'), "hostname=192.168.10.43".encode('utf-8'), "port=3389".encode('utf-8'),
                                    str("enable-drive=true").encode('utf-8'),
                                    str("drive-path=/drive/" + username).encode('utf-8')],
            "member": [str("uid=" + username + ",ou=users,dc=xaas,dc=local").encode('utf-8')],
        }
    if connection_name == 2 :
        dn = " cn=revite_" + username + ",ou=groups,dc=xaas,dc=local"
        mymodlist = {
            "objectClass": ["guacConfigGroup".encode('utf-8'), "groupOfNames".encode('utf-8')],
             "cn": [str("revite_"+username).encode('utf-8')],
             "guacConfigProtocol": ["rdp".encode('utf-8')],
             "guacConfigParameter": [str("name=revite_"+username).encode('utf-8'),"hostname=192.168.10.44".encode('utf-8'), "port=3389".encode('utf-8') ,
                                     str("enable-drive=true").encode('utf-8'),
                                     str("drive-path=/drive/" + username).encode('utf-8')],
             "member": [str("uid=" + username + ",ou=users,dc=xaas,dc=local").encode('utf-8')],
        }
    if connection_name == 3 :
        dn = " cn=photoshop_" + username + ",ou=groups,dc=xaas,dc=local"
        mymodlist = {
            "objectClass": ["guacConfigGroup".encode('utf-8'), "groupOfNames".encode('utf-8')],
             "cn": [str("photoshop_"+username).encode('utf-8')],
             "guacConfigProtocol": ["rdp".encode('utf-8')],
             "guacConfigParameter": [str("name=photoshop_"+username).encode('utf-8'),"hostname=192.168.10.45".encode('utf-8'), "port=3389".encode('utf-8') ,
                                     str("enable-drive=true").encode('utf-8'),
                                     str("drive-path=/drive/" + username).encode('utf-8')],
             "member": [str("uid=" + username + ",ou=users,dc=xaas,dc=local").encode('utf-8')],
        }
    if connection_name == 4 :
        dn = " cn=max3d_" + username + ",ou=groups,dc=xaas,dc=local"
        mymodlist = {
            "objectClass": ["guacConfigGroup".encode('utf-8'), "groupOfNames".encode('utf-8')],
             "cn": [str("max3d_"+username).encode('utf-8')],
             "guacConfigProtocol": ["rdp".encode('utf-8')],
             "guacConfigParameter": [str("name=max3d_"+username).encode('utf-8'),"hostname=192.168.10.46".encode('utf-8'), "port=3389".encode('utf-8') ,
                                     str("enable-drive=true").encode('utf-8'),
                                     str("drive-path=/drive/" + username).encode('utf-8')],
             "member": [str("uid=" + username + ",ou=users,dc=xaas,dc=local").encode('utf-8')],
        }

    con.add_s(dn, ldap.modlist.addModlist(mymodlist))
    con.unbind_s()

