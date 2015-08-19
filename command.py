# List of All CLA commands available in the RESTFUL API

##############
# userconfig #
##############

# Add a user, Password case sensitive
# params = role. Comma separated list. Example : SYSADMIN,NTWKADMIN,APROVR
ADD_USER = "<clacommand>"+\
                "<act>userconfig</act>"+\
                    "<ur_add>username</ur_add>"+\
                    "<ur_pwd>password</ur_pwd>"+\
                    "<ur_rl>params</ur_rl>"+\
                "</clacommand>"
# Delete a user
DEL_USER = "<clacommand>"+\
                "<act>userconfig</act>"+\
                "<ur_del>username</ur_del>"+\
            "</clacommand>"+\

#############
# devconfig #
############# 

# Add a device
# device address is IPV4, IPV6 or Hostname
# dev_to = TimeOut (Available in Advanced Add Device Web GUI)
# dev_rt = Retries (Available in Advanced Add Device Web GUI)

DEVICE_ADD =                "<clacommand>"+\
                                "<act>devconfig</act>"+\
                                "<add_ip>deviceaddress</add_ip>"+\
                                "<dev_rc>read community string</dev_rc>"+\
                                "<dev_wc>write community string</dev_wc>"+\
                                "<dev_name>devicename</dev_name>"+\
                                "<dev_alias>devicealias</dev_alias>"+\
                                "<dev_to>n</dev_to>"+\
                                "<dev_rt>n</dev_rt>"+\
                                "<dev_cp>protocol</dev_cp>"+\
                            "</clacommand>"

#Enter the device IP address of the device to delete (IPv4, IPv6 or host name).
DEVICE_DEL =                "<clacommand>"+\
                                "<act>devconfig</act>"+\
                                "<del_ip>deviceaddress</del_ip>"+\
                            "</clacommand>"

#Enter the IP Address of the device to modify (IPv4, IPv6 or host name) and device write community string.
DEVICE_MODIFY_COMMUNITY =   "<clacommand>"+\
                                "<act>devconfig</act>"+\
                                "<mod_ip>deviceaddress</mod_ip>"+\
                                "<dev_wc>write community string</dev_wc>"+\
                            "</clacommand>"

#Enter the IP address of the device to relearn (IPv4, IPv6 or host name).
DEVICE_RELEARN =            "<clacommand>"+\
                                "<act>devconfig</act>"+\
                                "<relearn_ip>deviceaddress</relearn_ip>"+\
                            "</clacommand>"

# Activate the specified device (IPv4, IPv6 or host name) and its interfaces.
DEVICE_ACTIVATE =           "<clacommand>"+\
                                "<act>devconfig</act>"+\
                                "<act_ip>deviceaddress</act_ip>"+\
                            "</clacommand>"

# Deactivate the specified device (IPv4, IPv6 or host name) and its interfaces.
DEVICE_DEACTIVATE =         "<clacommand>"+\
                                "<act>devconfig</act>"+\
                                "<deact_ip>deviceaddress</deact_ip>"+\
                            "</clacommand>"

# Rename current VLANs or add alias names using the addresses in the specified file and required input content.
# Format of lines in <inputContent> :
# 192.168.176.137:3,VLAN-33,VLAN-33-a1
# 192.168.176.137:3,VLAN-32,VLAN-32-a1,New York
DEVICE_MODIFY_VIFN =        "<clacommand>"+\
                                "<act>devconfig</act>"+\
                                "<update_vifn_list>VLAN</update_vifn_list>"+\
                                "<fn>update_vifn_list.txt</fn>"+\
                                "<inputContent></inputContent>"+\
                            "</clacommand>"

READ_ALL_MEG =               "<clacommand>"+"<act>siteconfig</act>"+\
                                 "<get_site>getsites.txt</get_site>"+\
                             "</clacommand>"
                

